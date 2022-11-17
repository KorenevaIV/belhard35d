# 1. Написать функцию horse принимающая координаты (два числа в диапазоне от 0 до 8)
# расположения коня на шахматной доске, вывести все позиции куда может перейти конь за 1
# шаг

# Ниже перечислены все восемь возможных движений коня.
# Не изменяйте последовательность приведенных ниже списков.
row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]


# Проверить, является ли `(x, y)` правильными координатами шахматной доски.
# Обратите внимание, что конь не может выйти за пределы доски.
def isValid(x, y):
    return not (x < 0 or y < 0 or x >= N or y >= N)


# Рекурсивная функция для выполнения рыцарского тура с Backtracking
def knightTour(visited, x, y, pos):
    # отметить текущий квадрат как посещенный
    visited[x][y] = pos

    # , если все квадраты посещены, вывести решение
    if pos >= N * N:
        for r in visited:
            print(r)
        print()
        # отступает перед возвращением
        visited[x][y] = 0
        return

    # проверка всех восьми возможных движений коня
    # и повторяться для каждого действительного движения
    for k in range(8):

        # получить новую позицию коня из текущей
        # позиция на шахматной доске
        newX = x + row[k]
        newY = y + col[k]

        # , если новая позиция действительна и еще не посещена
        if isValid(newX, newY) and visited[newX][newY] == 0:
            knightTour(visited, newX, newY, pos + 1)

    # вернуться из текущего квадрата и удалить его из текущего пути
    visited[x][y] = 0


if __name__ == '__main__':
    # `N × N` шахматная доска
    N = 5

    # Посещенный # служит двум целям:
    # 1. Отслеживает клетки, задействованные в обходе коня.
    # 2. Хранит порядок посещения квадратов.
    visited = [[0 for x in range(N)] for y in range(N)]
    pos = 1

    # начать обход конем с углового квадрата `(0, 0)`
    knightTour(visited, 0, 0, pos)