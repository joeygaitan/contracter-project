from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# client = MongoClient()
# db = client.Contracter

# client = MongoClient()

items = [{"image": "../assets/shirts/blueWhiteShirt.png","title":"Blue and White Shirt", "description": "This shirt is Blue and White. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly","price": 10.00, "size": ["xs","s","m","l","xl"]}
,{"image": "../assets/shirts/fendiShirt.png","title":"Fendi Shirt", "description": "This shirt is black and has a white Fendi text on it. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly", "size": ["xs","s","m","l","xl"], "price": 20.00}
,{"image": "../assets/shirts/focusShirt.png","title":"Focus Shirt", "description": "This shirt is black Focus text on it. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly","size": ["xs","s","m","l","xl"], "price": 25.00}
,{"image": "../assets/shirts/focusShirt.png","title":"Pink Shirt", "description": "This shirt is pink. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly", "size": ["xs","s","m","l","xl"], "price": 15.00},
{"image": "../assets/shirts/","title":"", "description": ""}]

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', items=items)

if __name__ == "__main__":
    app(debug=True)