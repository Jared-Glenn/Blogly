from app import app
from unittest import TestCase

class BloglyTestCase(TestCase):
    def test_user_list(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)
            
    def test_new_user(self):
        with app.test_client() as client:
            res = client.get('/users/new')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Create a user</h1>', html)
    
    def test_user(self):
        with app.test_client() as client:
            res = client.get('/users/1')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<input id="edit-button" type="button"', html)
    
    def test_edit_user(self):
        with app.test_client() as client:
            res = client.get('/users/1/edit')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Edit a user</h1>', html)
    
    def test_post_form_page(self):
        with app.test_client() as client:
            res = client.get('/users/1/posts/new')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Add Post for', html)
    
    def test_edit_post(self):
        with app.test_client() as client:
            res = client.get('/posts/1/edit')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Edit a post</h1>', html)