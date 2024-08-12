from project.libs.Mongo_db import MongoDB

DATABASE_NAME = "kabuki"
COLLECTION_NAME = "books"

def get_book_path_list() -> dict:
    book_path = {}
    with MongoDB(DATABASE_NAME) as session:
        collection = session[COLLECTION_NAME]
        for item in collection.find():
            book_path[item['index']] = item['path']
    return book_path
if __name__ == '__main__':
    book_path = get_book_path_list()
    for index,path in book_path.items():
        print(f'{index} : {path}')
