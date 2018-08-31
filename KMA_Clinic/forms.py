from django import forms
from .models import KMA
from .models import Visits


class PostForm(forms.ModelForm):
	#age = forms.CharField(widget=forms.TextInput(), initial="KMA.age_")
	class Meta:
		model  = KMA
		fields = [
			'name',
			'address',
			'birthdate',
			'age',
			'phone',
			'husband',
		]


class PostVisit(forms.ModelForm):
	class Meta:
		model  = Visits
		fields = [
			'patient_id',
			'present_hist1',
			'present_hist2',
			'present_hist3',
			'past_hist1',
			'past_hist2',
			'past_hist3',
		]




