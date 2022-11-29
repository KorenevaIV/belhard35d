# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать ошибку
# ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать атрибут ValueError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод update принимающий индекс категорий и новое название категории, если
# нет элемента на таком индексе, то новая категория должна добавляться с учетом того, что
# имена категорий уникальны, если новое имя категории нарушает уникальность в списке
# категорий, вызвать исключение ValueError
class Category:

    categories: list[str] = []

    @classmethod
    def add(cls, category_name: str) -> int:
        category_name = category_name.title()
        if category_name in cls.categories:
            raise ValueError
        cls.categories.append(category_name)
        return cls.categories.index(category_name)
        # return len(cls.categories) - 1

    @classmethod
    def get(cls, index: int) -> str:
    #     if index in range(0, len(cls.categories)-1):
    #         return cls.categories[index]
    #     else:
    #         return ValueError
        try:
            return cls.categories[index]
        except IndexError as (e):
            raise ValueError(e)

    @classmethod
    def delete(cls, index: int):
        try:
            del cls.categories[index]
        except IndexError:
            pass  # словит ошибку и ничего не выдаст в консоле, ничего не возвращает

    # 3.4 Написать метод update принимающий индекс категорий и новое название категории, если
    # нет элемента на таком индексе, то новая категория должна добавляться с учетом того, что
    # имена категорий уникальны, если новое имя категории нарушает уникальность в списке
    # категорий, вызвать исключение ValueError


    # @classmethod
    #     def update(cls, pk: int, new_category_name: str):
    #         new_category_name = new_category_name.title()
    #         if new_category_name in cls.categories:
    #             raise ValueError('category is not unique')
    #         try:
    #             cls.get(pk=pk)
    #         except ValueError:
    #             cls.add(category=new_category_name)
    #         else:
    #             cls.categories[pk] = new_category_name
    @classmethod
        def update(cls, pk: int, new_category_name: str):
            new_category_name = new_category_name.title()
            if new_category_name in cls.categories:
                raise ValueError('category is not unique')
            try:
                cls.categories[pk] = new_category_name
            except IndexError:
                cls.add(category=new_category_name)

# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool)
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение ValueError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# ValueError





new_list = Category()
new_list.add('first')
new_list.add('second')
new_list.add('third')
new_list.add('forth')
new_list.update(4, 'six')
print(new_list.get(4))
