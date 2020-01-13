import random

class Object:
    x = 0
    y = 0
    health = 0
    damage = 1

    def r_damage(self):
        return self.damage

    def r_health(self):
        return self.health

    def position(self):
        return [self.x, self.y]

    def position_init(self, position_object = []):
        if position_object:
            while True:
                self.x = random.randint(0, 3)
                self.y = random.randint(0, 3)
                if [self.x, self.y] not in position_object:
                    return [self.x, self.y]
        else:
            self.x = random.randint(0, 3)
            self.y = random.randint(0, 3)
            return [self.x, self.y]

    def Up(self):
        if self.x > 0:
            self.x -= 1
        return self.x

    def Down(self):
        if self.x < 3:
            self.x += 1
        return self.x

    def Left(self):
        if self.y > 0:
            self.y -= 1
        return self.y

    def Right(self):
        if self.y < 3:
            self.y += 1
        return self.y

    def was_hit(self, damage):
        self.health -= random.choice(range(damage + 1))
        return self.health