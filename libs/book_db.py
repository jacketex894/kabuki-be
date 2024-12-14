from libs.Mongo_db import MongoDB

def get_all_book_path():
    with MongoDB('kabuki') as session:
        collection = session["books"]
        books_info = list(collection.find().sort('book_index', 1))
        return books_info