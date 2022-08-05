from fastapi import FastAPI

app = FastAPI()

posts = []

@app.get('/')
def read_root():
    return{"welcome": "welcome to my rest API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts') #.post es el metodo http y /posts es la ruta del host
def save_post():
    print(post)
    return "received"