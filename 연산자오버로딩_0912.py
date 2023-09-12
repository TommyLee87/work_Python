class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # (+) 연산에 대응됩니다.
        return Vector2D(self.x + other, self.y + other)

    def __mul__(self, other):
        return Vector2D((self.x * other.x) + 100, (self.y * other.y) + 100)


v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

print(100 * 200)
print(100.1 * 200.1)
v3 = v1 * v2
v4 = v1 + 100
print(v4.x, v4.y)
