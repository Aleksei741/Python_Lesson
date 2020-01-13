# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

from collections import defaultdict

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):

    start_ = start
    length = len(graph)
    is_visited = [False] * length  # пОСЕЩАЛИ ВЕРШИНУ ИЛИ НЕТ
    cost = [float('inf')] * length  # Стоимость пути до конкретной вершины
    parent = [-1] * length  # родитель вершины

    cost[start] = 0
    min_cost = 0  # Минимальная стоимост
    track = defaultdict(int)

    while min_cost < float('inf'):  # Пока минимальная стоимостьменьше бесконечности

        is_visited[start] = True  # Отметим стартовую вершину как посещенную
        for i, vertex in enumerate(graph[start]):  # Пройдемся там, где хранится значение старт
            if vertex != 0 and not is_visited[i]:  # Если есть ребро и данную вершину мы не посещали

                if cost[i] > vertex + cost[start]:  # Если расстояние до i вершины окажется больше, чем раст
                    cost[i] = vertex + cost[start]

                    track[i] = start
                    parent[i] = start  # Для i вершины новое более короткое расстояние
                    # Обошли все смежные вершины и замписали мин растояние до них

        #track.append(parent)
        #parent = [-1] * length  # родитель вершины

        min_cost = float('inf')
        for i in range(length):  # Пройти по всем вершинам графа
            if min_cost > cost[i] and not is_visited[i]:  # Минимальная стоимость окажется больше,
                # чем стоимость пути до оч вершины и эту вершину мы еще не посещали
                min_cost = cost[i]  # Запомнили тек стоимость
                start = i  # Данная вершина явл стартовой

    result = list()
    result.append(cost)
    for i in range(length):
        result.append(list())
        # result[i].append(cost[i])
        j = -1
        while j != start_ and cost[i] != float('inf'):
            if j == -1:
                result[i+1].append(i)
                j = i
            else:
                result[i+1].append(track[j])
                j = track[j]
        result[i + 1].reverse()

    return result

n = int(input('начальная точка графа: '))
result = dijkstra(g, n)
for i in range(len(result[0])):
    print(f'Расстояние до {i} = {result[0][i]}')
    print(f'Путь следования: {result[i+1]}')
