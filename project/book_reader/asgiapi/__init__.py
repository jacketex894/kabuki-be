from libs.book_db import get_all_book_path

_info = get_all_book_path()
BOOKS_INFO = {}
for book in _info:
    BOOKS_INFO[book['index']] = book