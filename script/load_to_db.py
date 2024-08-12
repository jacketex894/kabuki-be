import yaml
import os
import pymongo
from pymongo import MongoClient
import sys

with open('path.yaml','r') as yaml_file:
    data = yaml.load(yaml_file,Loader=yaml.FullLoader)

def get_creation_date(path):
    return os.path.getctime(path)

def load_book_to_db() -> list[str]:
    path = data['path']
    books = []
    for dirpath,dirnamem,filenames in os.walk(path):
        if dirpath and dirpath != path:
            creation_date = get_creation_date(dirpath)
            books.append({'path': dirpath, 'pages': len(filenames), 'creation_date': creation_date})
    books.sort(key=lambda x: x['creation_date'])
    client = MongoClient("localhost", 27017)
    db = client["kabuki"]
    collection = db["books"]
    
    insert_list = []
    index = 0
    for book in books:
        insert_list.append({'index':f'{index:05d}','path':book['path'],'pages':book['pages']})
        index += 1
    if not insert_list:
        print(f'error : no books')
        return 
    collection.insert_many(insert_list)

    
if __name__ == '__main__':
    load_book_to_db()
