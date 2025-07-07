import pytest
from helper import *
from main import BooksCollector



class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Загадка старого замка')
        collector.add_new_book('Секреты кошачьей психологии')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_same_name(self):
        collector = BooksCollector()
        collector.add_new_book('Загадка старого замка')
        collector.add_new_book('Загадка старого замка')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['В', 'Властелин колец братство кольца и хоббит'])
    def test_add_new_book_add_book_1_and_40_len(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        list_name= collector.get_books_genre()
        assert 1 == len(list_name)

    @pytest.mark.parametrize('name', ['', 'Властелин колец братство кольца и хоббиты'])
    def test_add_new_book_not_add_0_and_41_len(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        list_name = collector.get_books_genre()
        assert 0 == len(list_name)

    def test_set_book_genre_valid_data(self):
        collector = BooksCollector()
        add_one_book_and_set_valid_genre(collector)
        assert collector.books_genre['Шерлок Холмс'] == 'Детективы'

    def test_set_book_genre_not_name(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Доктор Ватсон', 'Детективы')
        genre_draco = collector.get_book_genre('Доктор Ватсон')
        assert None == genre_draco

    def test_set_book_genre_not_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Фанфик')
        genre_gp = collector.get_book_genre('Шерлок Холмс')
        assert '' == genre_gp

    def test_get_book_genre_valid_data(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.books_genre['Шерлок Холмс'] = 'Детективы'
        genre_gp = collector.get_book_genre('Шерлок Холмс')
        assert genre_gp == 'Детективы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector_with_books(collector)
        list_genre = collector.get_books_with_specific_genre('Детективы')
        assert 'Шерлок Холмс' in list_genre

    def test_get_books_genre(self):
        collector = BooksCollector()
        add_one_book_and_set_valid_genre(collector)
        list_books_genre = collector.get_books_genre()
        assert {'Шерлок Холмс':'Детективы'} == list_books_genre

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector_with_books(collector)
        list_for_kids = collector.get_books_for_children()
        assert 'Маугли' in list_for_kids

    def test_add_book_in_favorites_add_one(self):
        collector = BooksCollector()
        add_one_book_and_add_in_favorites(collector)
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        add_one_book_and_add_in_favorites(collector)
        collector.add_book_in_favorites('Маугли')
        collector.delete_book_from_favorites('Маугли')
        list_book_in_favorites = collector.get_list_of_favorites_books()
        assert list_book_in_favorites == ['Шерлок Холмс']

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        add_one_book_and_add_in_favorites(collector)
        list_book_in_favorites = collector.get_list_of_favorites_books()
        assert 'Шерлок Холмс' in list_book_in_favorites
