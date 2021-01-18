"""
	Steps to push new code to github

	git add . 

	git commit -am "The reason for the commit"

	git push
 """


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

		
	return render(request, 'home.html', {'ticker': ticker, 'stuff': stuff, 'api': api, 'ticker2': ticker2})

	
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

		stuff = ''

		for i in range(0, len(ticker)):
			if i < len(ticker) -1:
				stuff = stuff + str(ticker[i]) + ','
			else:
				stuff = stuff + str(ticker[i])


		api_request = requests.get("https://cloud.iexapis.com/stable/stock/market/batch?symbols=" + stuff + "&types=quote&token=pk_0d91d44050cc4ca2973b9d485e05aae7")


		try:

			api = json.loads(api_request.content)

		except Exception as e:

			api = 'Error'


		return  render(request, 'add_stock.html', {'api': api})

		
def delete(request, stock_id):

	item = stock.objects.get(pk= stock_id)
	item.delete()
	messages.success(request, ('You have deleted a stock!'))
	return redirect('delete_stock')

def delete_stock(request):
	ticker = stock.objects.all()

	return render(request, 'delete_stock.html', {'ticker': ticker})


	
