from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient()
db = client.Shirtlist
cart = db.cart

items = [{"image": "/blueWhiteShirt.png","title":"Blue and White Shirt", "description": "This shirt is Blue and White. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly","price": 10.00, "size": ["xs","s","m","l","xl"],"-id":0}
,{"image": "/fendiShirt.png","title":"Fendi Shirt", "description": "This shirt is black and has a white Fendi text on it. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly", "size": ["xs","s","m","l","xl"], "price": 20.00,"-id":1}
,{"image": "/focusShirt.png","title":"Focus Shirt", "description": "This shirt is black Focus text on it. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly","size": ["xs","s","m","l","xl"], "price": 25.00,"-id":2}
,{"image": "/pinkShirt.png","title":"Pink Shirt", "description": "This shirt is pink. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly", "size": ["xs","s","m","l","xl"], "price": 15.00,"-id":3},
{"image": "/whiteShirt.png","title":"White Shirt", "description": "This shirt is white. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly", "size": ["xs","s","m","l","xl"], "price": 10.00,"-id":4},
{"image": "/circleShirt.png","title":"Design Shirt", "description": "This shirt is has a orange cirle. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly", "size": ["xs","s","m","l","xl"], "price": 20.00,"-id":5},
{"image": "/yellowStripeShirt.png","title":"Yellow Stripe Shirt", "description": "This shirt is has a nice yellow stripe on it. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly", "size": ["xs","s","m","l","xl"], "price": 16.00,"-id":6},
{"image": "/beastShirt.png","title":"Beast Shirt", "description": "This is a yellow shirt with the word Beast on it. It comes in many sizes. Theses shirts that sold here are all unisex. please pick accordingly", "size": ["xs","s","m","l","xl"], "price": 11.00,"-id":7}]

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', items=items)


@app.route('/shirt/<id>')
def shirt(id):
    id = int(id)
    item = items[id]
    return render_template('item.html', item=item)

@app.route('/cart/add/<id>')
def create_cart_item(id):
    id = int(id)
    item = items[id]
    return render_template('create_cart_item.html', item=item)

@app.route('/', methods=['POST'])
def cart_submit():
    id = request.form.get('id')
    id = int(id)
    item = items[id]
    """Submit a new playlist."""
    cart_item = {
        'quantity': request.form.get('quantity'),
        'size': request.form.get('size'),
        'image': item['image'],
        'title': item['title'],
        'price': item['price'] * int(request.form.get('quantity'))
    }
    cart.insert_one(cart_item)
    return redirect(url_for('home.html'))


if __name__ == "__main__":
    app(debug=True)