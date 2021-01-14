from django import forms
from .models import stock

class StockForm(forms.ModelForm):
	"""docstring for StockForm"""
	class Meta(object):
		"""docstring for Meta"""
		model = stock
		fields = ["ticker"]