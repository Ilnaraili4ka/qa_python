test_books_data = [
    ("Шерлок Холмс", "Детективы"),
    ("Война миров", "Фантастика"),
    ("Приключения Тома Сойера", "Приключения"),
    ("Маугли", "Мультфильмы")
]

def add_one_book_and_set_valid_genre(collector):
    collector.add_new_book("Шерлок Холмс")
    collector.set_book_genre("Шерлок Холмс", "Детективы")
    return collector


def add_one_book_and_add_in_favorites (collector):
    collector.add_new_book("Шерлок Холмс")
    collector.add_book_in_favorites ("Шерлок Холмс")
    return collector

def collector_with_books(collector):
    for name, genre in test_books_data:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector
