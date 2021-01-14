from django.shortcuts import render, redirect
from .models import stock
from .forms import StockForm
from django.contrib import messages


def home(request):
	import requests
	import json

	if request.method == "POST":
		ticker = request.POST['ticker']

		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?&token=pk_0d91d44050cc4ca2973b9d485e05aae7")

		try: 
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'Error'
		return render(request, 'home.html', {'api': api})


	else:
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above"})

	
def about(request):
	return render(request, 'about.html', {})


def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added!"))
			return redirect('add_stock')

	else:

		ticker = stock.objects.all()

		output = []
		for i in ticker:

			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(i) + "/quote?&token=pk_0d91d44050cc4ca2973b9d485e05aae7")

			try: 
				api = json.loads(api_request.content)
				output.append(api)

			except Exception as e:
				api = 'Error'
				


		return  render(request, 'add_stock.html', {'ticker' : ticker, 'output': output})

		
def delete(request, stock_id):

	item = stock.objects.get(pk= stock_id)
	item.delete()
	messages.success(request, ('You have deleted a stock!'))
	return redirect('delete_stock')

def delete_stock(request):
	ticker = stock.objects.all()

	return render(request, 'delete_stock.html', {'ticker': ticker})


	
