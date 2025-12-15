import unittest
import json
from app import app

class FlaskCalculatorTest(unittest.TestCase):
    def setUp(self):
        # создаём тестовый клиент
        self.app = app.test_client()
        self.app.testing = True
    
    def test_add_valid(self):
        response = self.app.get('/add?a=5&b=10')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 15.0)
        
    def test_add_invaid(self): 
        response = self.app.get('/add?a=5&b=test')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], "Invalid input")
    

if __name__ == "__main__":
    unittest.main()