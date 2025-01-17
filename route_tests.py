from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

class cartTests(TestCase):
    """Flask tests."""

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_index(self):
        '''Tests to see if the main store page works and displays shirts'''
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_shirt(self):
        '''Checks to see if one shirt can be displayed'''
        result = self.app.get('/shirt/0')
        self.assertEqual(result.status_code, 200)
    
    def test_create_cart_item(self):
        '''This checks if you can successfully be able to add to cart'''
        result = self.app.get('cart/add/0')
        self.assertEqual(result.status_code, 200)

    def test_edit_cart(self):
        '''This checks if you can successfully be able to edit the item in your cart'''
        result = self.app.get('/cart/edit/5d9fb0c57f1dda07a9e374c2')
        self.assertEqual(result.status_code, 200)

    def test_cart_item_update(self):
        '''This completes the update to the cart'''
        result = self.app.get('/cart?cart_item=%7B%27_id%27%3A+ObjectId%28%275d9fb0c57f1dda07a9e374c2%27%29%2C+%27quantity%27%3A+%271%27%2C+%27size%27%3A+%27m%27%2C+%27title%27%3A+%27Blue+and+White+Shirt%27%2C+%27price%27%3A+10.0%7D&cart_item_id=5d9fb0c57f1dda07a9e374c2')
        self.assertEqual(result.status_code, 200)

    def test_cart_delete(self):
        '''This deletes the item and display the new cart with the removed item'''
        result = self.app.get('/cart')
        self.assertEqual(result.status_code, 200)

    def test_cart_submit(self):
        '''This displays '''
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)




    

if __name__ == '__main__':
    unittest_main()