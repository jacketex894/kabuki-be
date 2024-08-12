from fastapi import APIRouter
import os
from fastapi.responses import FileResponse
from libs.Mongo_db import MongoDB

book_reader_v1_router = APIRouter(prefix='/kabuki/book_reader')


@book_reader_v1_router.get("/hello_world",tags=['book_reader'])
async def hello_world():
    return "hello this is book_reader"

@book_reader_v1_router.get("/api/get_last_book",tags=['book_reader'])
async def get_last_book_index():
    last_index = None
    with MongoDB('kabuki') as session:
        collection = session["books"]
        last_index = list(collection.find())[-1]['index']
    return last_index


@book_reader_v1_router.get("/api/get_image/{bookIndex}/{page}",tags=['book_reader'])
async def get_cover(bookIndex,page):
    path = None
    with MongoDB('kabuki') as session:
        collection = session["books"]
        path = collection.find_one({'index':bookIndex})['path']
    
    files = os.listdir(path)
    return FileResponse(f'{path}/{files[int(page)]}')

@book_reader_v1_router.get("/api/get_pages/{bookIndex}",tags=['book_reader'])
async def get_page_number(bookIndex):
    pages = None
    with MongoDB('kabuki') as session:
        collection = session["books"]
        pages = collection.find_one({'index':bookIndex})['pages']
    return pages