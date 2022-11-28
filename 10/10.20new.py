 # 3. Реализовать класс Category

class Category:
# Создать атрибут класса categories
    categories: list[str] = []

# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать ошибку
# ValueError
    def add(self, category_name: str) -> int:
        if category_name in self.categories:
            raise ValueError
        else:
            self.categories.append(category_name)
            return self.categories.index(category_name)

# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать атрибут ValueError
    def get(self, index: int) -> str:
        if index in range(0, len(self.categories) - 1):
            return self.categories[index]
        else:
            return ValueError

# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
    def delete(self, index: int):
        for index in range(0, len(self.categories) - 1):
            del self.categories[index]

# 3.4 Написать метод update принимающий индекс категорий и новое название категории, если
# нет элемента на таком индексе, то новая категория должна добавляться с учетом того, что
# имена категорий уникальны, если новое имя категории нарушает уникальность в списке
# категорий, вызвать исключение ValueError
    def update(self, index: int, new_name: str):
        if self.categories[index] not in self.categories:
            if new_name not in self.categories:
                return self.categories.append(new_name)
        raise ValueError