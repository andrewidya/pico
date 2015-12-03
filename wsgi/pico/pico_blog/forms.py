from django import forms

class SearchForm(forms.Form):
	search_input = forms.CharField(required=False,
		widget=forms.TextInput(
			attrs={'class': 'form-control'}
			)
		)