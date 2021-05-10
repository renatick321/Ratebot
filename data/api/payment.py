from coinbase_commerce.client import Client
import sys
sys.path.append("../../")
from config import API_KEY

coinbase = Client(api_key=API_KEY)


def charge_create(amount):
	charge = coinbase.charge.create(name='The Sovereign Individual',
	                              description='Mastering the Transition to the Information Age',
	                              pricing_type='fixed_price',
	                              local_price={
	                                  "amount": str(amount),
	                                  "currency": "USD"
	                              })
	return charge


def get_charge(id):
	charge = coinbase.charge.retrieve(id)
	return charge