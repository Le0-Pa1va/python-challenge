from fastapi import FastAPI
from controllers import main

app = FastAPI()

@app.get('/list_products')
def list_products(best_seller=False, rating=None, name=None):
    """Returns a list with all products in the page"""
    return main.list_products(best_seller=best_seller, rating=rating, name=name)
