from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app, cart

cart_stuff = {
        'quantity': 1,
        'size': "m",
        'title': "shirt",
        'price': 10.00
}

cart.insert_one(cart_item)

cart_item = 

class cartTests(TestCase):
    """Flask tests."""

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
    
    def test_new(self,cart):
        result = self.app.get(f'/cart/add/{cart._id}')
        self.assertEqual(result.status_code, 201)

if __name__ == '__main__':
    unittest_main()