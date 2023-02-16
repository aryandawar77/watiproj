from django.test import TestCase
import requests
from API.models import sumLogs

class AddSumAPITest(TestCase):
    def setUp(self):
        self.num1 = 10
        self.num2 = 20

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        data={
          'num1':self.num1,
          'num2':self.num2
        }
        response = requests.post('http://127.0.0.1:8000/api/add/', data)
        data = response.json()
        
        # persistantObj = sumLogs.objects.filter(pk=data['storageKey']).first()
        # print(persistantObj)
        # if not persistantObj:
        #   raise Exception('Value not stored in DB')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['sum'],self.num1+self.num2)
        # self.assertEqual(data['sum'],self.num1+self.num2)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')