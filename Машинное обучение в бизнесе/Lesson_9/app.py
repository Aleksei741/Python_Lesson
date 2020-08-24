from flask import Flask, request, jsonify
import xgboost as xgb
from process_data import process_input
import pandas as pd

# For logging
import logging
import traceback
from logging.handlers import RotatingFileHandler
from time import strftime, time

app = Flask(__name__)

model = xgb.XGBModel()
model.load_model('xgb_ClaimsCount.model')

# Logging
handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=5)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.route("/")
def index():
    return "API for predict service"


@app.route("/predict", methods=['POST'])
def predict():
    json_input = request.json

    # Request logging
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    logger.info(f'{current_datatime} request from {ip_address}: {request.json}')
    start_prediction = time()

    id = json_input['ID']
    hf = process_input(json_input)

    data = InsDataFrame_Fr()
    data.load_pd(hf)
    # Переименовываем
    data.columns_match({'DrivAge': 'driver_minage', 'LicAge': 'driver_minexp'})
    # Преобразовываем
    data.transform_age()
    data.transform_exp()
    data.transform_gender()
    data.transform_MariStat()
    data.transform_SocioCateg()
    # Пересечение пола и возраста, их квадраты
    data.transform_age_gender()
    data.polynomizer('driver_minage_m')
    data.polynomizer('driver_minage_f')
    data.get_dummies(['VehUsage', 'SocioCateg'])

    col_features = [
        'driver_minexp',
        'Gender',
        'MariStat',
        'HasKmLimit',
        'BonusMalus',
        'OutUseNb',
        'driver_minage_m',
        'driver_minage_f',
        'driver_minage_m_2',
        'driver_minage_f_2',
        'VehUsage_Private',
        'VehUsage_Private+trip to office',
        'VehUsage_Professional',
        'VehUsage_Professional run',
        'SocioCateg_CSP1',
        'SocioCateg_CSP2',
        'SocioCateg_CSP3',
        'SocioCateg_CSP4',
        'SocioCateg_CSP5',
        'SocioCateg_CSP6',
        'SocioCateg_CSP7',
        'RiskArea'
    ]

    hf = data.get_pd(col_features)

    prediction_ClaimsCount = model.predict(hf)
    value_ClaimsCount = prediction_ClaimsCount.as_data_frame()['predict'][0]

    result = {
        'ID': id,
        'value_ClaimsCount': value_ClaimsCount
    }

    # Response logging
    end_prediction = time()
    duration = round(end_prediction - start_prediction, 6)
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    logger.info(f'{current_datatime} predicted for {duration} msec: {result}\n')

    return jsonify(result)


@app.errorhandler(Exception)
def exceptions(e):
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    error_message = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                 current_datatime,
                 request.remote_addr,
                 request.method,
                 request.scheme,
                 request.full_path,
                 error_message)
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)


class InsDataFrame:

    ''' Load data method '''

    def load_pd(self, pd_dataframe):
        self._df = pd_dataframe

    ''' Columns match method '''

    def columns_match(self, match_from_to):
        self._df.rename(columns=match_from_to, inplace=True)

    ''' Person data methods '''

    # Gender
    _gender_dict = {'Male': 0, 'Female': 1}

    def transform_gender(self):
        self._df['Gender'] = self._df['Gender'].map(self._gender_dict)

    # Age
    @staticmethod
    def _age(age, age_max):
        if pd.isnull(age):
            age = None
        elif age < 18:
            age = None
        elif age > age_max:
            age = age_max
        return age

    def transform_age(self, age_max=70):
        self._df['driver_minage'] = self._df['driver_minage'].apply(self._age, args=(age_max,))

    # Age M/F
    @staticmethod
    def _age_gender(age_gender):
        _age = age_gender[0]
        _gender = age_gender[1]
        if _gender == 0:  # Male
            _driver_minage_m = _age
            _driver_minage_f = 18
        elif _gender == 1:  # Female
            _driver_minage_m = 18
            _driver_minage_f = _age
        else:
            _driver_minage_m = 18
            _driver_minage_f = 18
        return [_driver_minage_m, _driver_minage_f]

    def transform_age_gender(self):
        self._df['driver_minage_m'], self._df['driver_minage_f'] = zip(
            *self._df[['driver_minage', 'Gender']].apply(self._age_gender, axis=1).to_frame()[0])

    # Experience
    @staticmethod
    def _exp(exp, exp_max):
        if pd.isnull(exp):
            exp = None
        elif exp < 0:
            exp = None
        elif exp > exp_max:
            exp = exp_max
        return exp

    def transform_exp(self, exp_max=52):
        self._df['driver_minexp'] = self._df['driver_minexp'].apply(self._exp, args=(exp_max,))

    ''' Other data methods '''

    def polynomizer(self, column, n=2):
        if column in list(self._df.columns):
            for i in range(2, n + 1):
                self._df[column + '_' + str(i)] = self._df[column] ** i

    def get_dummies(self, columns):
        self._df = pd.get_dummies(self._df, columns=columns)

    # Вспомогательный столбец для суммирования числа полисов с убытками
    # df['ClaimCount'] = df['ClaimAmount'] > 0

    ''' General methods '''

    def info(self):
        return self._df.info()

    def head(self, columns, n=5):
        return self._df.head(n)

    def len(self):
        return len(self._df)

    def get_pd(self, columns):
        return self._df[columns]


class InsDataFrame_Fr(InsDataFrame):

    # Experience (weeks to years)
    @staticmethod
    def _exp(exp, exp_max):
        if pd.isnull(exp):
            exp = None
        elif exp < 0:
            exp = None
        else:
            exp * 7 // 365
        if exp > exp_max:
            exp = exp_max
        return exp

    # Marital status
    _MariStat_dict = {'Other': 0, 'Alone': 1}

    def transform_MariStat(self):
        self._df['MariStat'] = self._df['MariStat'].map(self._MariStat_dict)

    # Social category
    def transform_SocioCateg(self):
        self._df['SocioCateg'] = self._df['SocioCateg'].str.slice(0, 4)