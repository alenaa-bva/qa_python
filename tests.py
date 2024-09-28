import pytest

from data import BooksData
from main import BooksCollector

class TestBooksCollector:
    data = BooksData

    @pytest.mark.parametrize('name', data.book_names)
    def test_add_new_book_name_in_range_from_0_to_41(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert name in collector.books_genre
        for book_name in collector.books_genre:
            assert 0 < len(book_name) < 41

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'

        collector.add_new_book(book_name_1)
        collector.add_new_book(book_name_2)

        assert len(collector.books_genre) == 2

    def test_set_book_genre(self):
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')

        assert collector.books_genre[name] == 'Ужасы'

    @pytest.mark.parametrize('name', data.book_names)
    def test_get_book_genre(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')

        assert  collector.get_book_genre(name) == 'Ужасы'

    def test_get_books_with_specific_genre_horror(self):
        collector = BooksCollector()

        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'

        collector.add_new_book(book_name_1)
        collector.add_new_book(book_name_2)

        collector.set_book_genre(book_name_1, 'Ужасы')
        collector.set_book_genre(book_name_2, 'Ужасы')

        list_of_books_with_specific_genre = collector.get_books_with_specific_genre('Ужасы')

        assert book_name_1 in list_of_books_with_specific_genre
        assert book_name_2 in list_of_books_with_specific_genre

    def test_get_books_genre_one_book(self):
        collector = BooksCollector()

        book_name = 'Гордость и предубеждение и зомби'
        book_genre = 'Ужасы'

        assert collector.books_genre == {}

        collector.add_new_book(book_name)
        books_genre = collector.get_books_genre()

        assert book_name in books_genre.keys()
        assert '' in books_genre.get(book_name)

        collector.set_book_genre(book_name, book_genre)
        books_genre = collector.get_books_genre()

        assert book_genre in books_genre.get(book_name)

    def test_get_books_for_children_appropriate_genres_in_the_list(self):
        book_names = ['Тайна старого замка:ключ к древней тайне', 'Гордость и предубеждение и зомби',
                      'Что делать, если ваш кот хочет вас убить', 'Рапунцель', 'Зачарованная']
        book_genres = ['Ужасы', 'Фантастика', 'Детективы', 'Комедии', 'Мультфильмы']

        collector = BooksCollector()

        for book in book_names:
            collector.add_new_book(book)

        for book, genre in zip(book_names, book_genres):
            collector.set_book_genre(book, genre)

        list_of_books_for_children = collector.get_books_for_children()

        assert 'Гордость и предубеждение и зомби' in list_of_books_for_children
        assert 'Рапунцель' in list_of_books_for_children
        assert 'Зачарованная' in list_of_books_for_children

    def test_get_books_for_children_inappropriate_genres_not_in_the_list(self):
        book_names = ['Тайна старого замка:ключ к древней тайне', 'Гордость и предубеждение и зомби',
                      'Что делать, если ваш кот хочет вас убить', 'Рапунцель', 'Зачарованная']
        book_genres = ['Ужасы', 'Фантастика', 'Детективы', 'Комедии', 'Мультфильмы']

        collector = BooksCollector()

        for book in book_names:
            collector.add_new_book(book)

        for book, genre in zip(book_names, book_genres):
            collector.set_book_genre(book, genre)

        list_of_books_for_children = collector.get_books_for_children()

        assert 'Тайна старого замка:ключ к древней тайне' not in list_of_books_for_children
        assert 'Что делать, если ваш кот хочет вас убить' not in list_of_books_for_children

    def test_add_book_in_favorites_one_book(self):
        book_names = ['Тайна старого замка:ключ к древней тайне', 'Гордость и предубеждение и зомби', '?', 'N', ' ']
        book_genres = ['Ужасы', 'Фантастика', 'Детективы', 'Комедии', 'Мультфильмы']

        collector = BooksCollector()

        for book, genre in zip(book_names, book_genres):
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        collector.add_book_in_favorites(book_names[0])
        collector.add_book_in_favorites(book_names[1])

        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites(self):
        book_name = 'Тайна старого замка:ключ к древней тайне'
        book_genre = 'Фантастика'

        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        collector.add_book_in_favorites(book_name)

        assert 'Тайна старого замка:ключ к древней тайне' in collector.favorites, 'Книга не добавлена в избранные'

        collector.delete_book_from_favorites(book_name)

        assert 'Тайна старого замка:ключ к древней тайне' not in collector.favorites, 'Книга все еще в избранных'

    def test_get_list_of_favorites_books(self):
        book_names = ['Тайна старого замка:ключ к древней тайне', 'Гордость и предубеждение и зомби', '?', 'N', ' ']
        book_genres = ['Ужасы', 'Фантастика', 'Детективы', 'Комедии', 'Мультфильмы']

        collector = BooksCollector()

        assert collector.favorites == []

        for book, genre in zip(book_names, book_genres):
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        collector.add_book_in_favorites(book_names[0])
        collector.add_book_in_favorites(book_names[1])
        collector.add_book_in_favorites(book_names[3])

        collector.delete_book_from_favorites(book_names[0])

        list_of_favourite_books = collector.get_list_of_favorites_books()

        assert book_names[1] in list_of_favourite_books
        assert book_names[3] in list_of_favourite_books




