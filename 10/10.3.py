# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool)
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение ValueError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# ValueError
class Category(object):

    categories: list[dict] = []

    @classmethod
    def add(cls, category_name: str, is_published: bool) -> int:
        category_name = category_name.title()
        category = tuple(filter(lambda x: x['name'] == category_name, cls.categories))
        if category:
            raise ValueError('category is not unique')
        cls.categories.append(
            {
                'name': category_name,
                'is_published': is_published
            }
        )
        return len(cls.categories) - 1

    @classmethod
    def get(cls, pk: int) -> dict:
        try:
            return cls.categories[pk]
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def delete(cls, pk: int) -> None:
        try:
            del cls.categories[pk]
        except IndexError:
            ...  # pass

    @classmethod
    def update(cls, new_category_name: str, pk: int) -> None:
        new_category_name = new_category_name.title()
        category = tuple(filter(lambda x: x['name'] == new_category_name, cls.categories))
        if category:
            raise ValueError('category is not unique')
        try:
            cls.categories[pk]['name'] = new_category_name
        except IndexError:
            cls.add(category_name=new_category_name, is_published=False)

    @classmethod
    def make_published(cls, pk: int) -> None:
        try:
            cls.categories[pk]['is_published'] = True
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def make_unpublished(cls, pk: int) -> None:
        try:
            cls.categories[pk]['is_published'] = False
        except IndexError as e:
            raise ValueError(e)


print(Category.add('Food', True))
print(Category.add('Drink', True))
print(Category.add('food', False))