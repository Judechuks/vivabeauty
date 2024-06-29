# paystack.py - logic for verifying payments and pull up base url from paystack
from django.conf import settings
import requests

class Paystack:
  PAYSTACK_SK = settings.PAYSTACK_SECRET_KEY
  base_url = 'https://api.paystack.co/'
  def verify_payment(self, ref, *args, **kwargs):
    path = f'transaction/verify/{ref}'
    headers = {
      'Authorization': f'Bearer {self.PAYSTACK_SK}',
      'Content_Type': 'application/json',
    }
    url = self.base_url + path
    response = requests.get(url, headers=headers)
    # if request was successful
    if response.status_code == 200:
      response_data = response.json()
      return response_data['status'], response_data['data']
    
    # else return data, status code and response message
    response_data = response.json()
    return response_data['status'], response_data['message']