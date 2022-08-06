from fastapi import FastAPI, HTTPException
from pydantic import BaseModel #para describir un modelo base
from typing import Text, Optional #typing viene en fastapi para textos largos
#Optional es otro objeto que podemos recurrir para que no todos los atributos de la clase sean obligatorios
from datetime import datetime #importamos para poder obtener datatime now 
from uuid import uuid4

app = FastAPI()

posts = []

# Post Model
class Post(BaseModel): #cuando creo un dato este es el esquema que va a tener
    id: Optional[str]
    title: str
    author:str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@app.get('/')
def read_root():
    return{"welcome": "welcome to my rest API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts') #.post es el metodo http y /posts es la ruta del host
def save_post(post: Post):
    #print(uuid4()) veo el contenido generado por uuid4

    #result=uuid4()        #con esto puedo ver que uuid4 es una clase, no es un str. POor lo que tendria que castear
    #print (type (result))

    post.id = str(uuid4()) #genera string random y asigna ese a la prop id de la publicacion
    posts.append(post.dict()) #luego va a ser guardada dentro de la lista
    return posts[-1] #retorno el ultimo elemento de la lista

@app.get('/posts/{post_id}')
def get_post(post_id:str): #recibo un parametro por la funcion q va a ser un str
    #print (post_id) muestra por consola lo que posteo en localhost:8000/posts/(1, mama, o lo que sea)
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post Not Found")

@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        #print(post)
        #print(index)
        if post["id"] == post_id:
            posts.pop(index)
            return{"message": "Post has been deleted successfully"}
    raise HTTPException(status_code=404, detail="Post Not Found")