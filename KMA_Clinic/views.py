from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import KMA, Visits 
from .forms import PostForm, PostVisit
from django import forms
from django.forms.widgets import HiddenInput
from django.utils import timezone

# Create your views here.
def patients(request): #Home Page
	query = KMA.objects.all().order_by('-id') 	
	#instance = KMA.objects.get(id=id)
	context = {
		'page_title': 'Patient\'s Data',
		'page_body': 'Hi it\'s my real APP.',
		'age_': age_,
		'query': query,
		#'instance':instance,
		'btn_save':'Save',
	}

	return render(request, 'list.html', context)

def patient_age(request,age): #Home Page
	query = KMA.objects.all().order_by('-id') 	
	instance = KMA.objects.get(age=age)
	context = {
		'page_title': 'Patient\'s Data',
		'page_body': 'Hi it\'s my real APP.',
		'age_': age_,
		'query': query,
		'instance':instance,
		'btn_save':'Save',
	}

	return render(request, 'detail.html', context)

# For Patient Screen
def detail(request,id):

    instance = KMA.objects.get(id=id) #get_object_or_404(post, id=id) #post.objects.get(id=3)

    context = { 
        'views_title':'Page Detail', 
        'age_': age_,
        'btn':'Update',
        'instance': instance,
        }

    return render(request,"detail.html", context)

# For visits screen
def detail_visits(request,id):

    instance = Visits.objects.get(id=id)#get_object_or_404(post, id=id) #post.objects.get(id=3)

    context = { 
        'views_title':'Visits Details', 
        'btn':'Update',
        'instance': instance,
        }

    return render(request,"visits.html", context)

def save_form(request):
	form = PostForm(request.POST or None)
	# cal_age = form.fields['age'].initial
	# cal_age = age_()
	#if request.method == 'POST':
		#age= request.POST.get('age')
	try:
		#cal_age = form.cleaned_data['age']
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, 'Save Process Done for Patient ID : ' + str(instance.id))
			cal_age = form.cleaned_data('age')
			return HttpResponseRedirect(instance.get_url())
	except Exception as e:
		messages.success(request, 'We Can\'t Save, Name Already Exists')

	context = {
		'views_title':'Insert Data',
		'page_title': 'New Patient',
		'age_': age_,
        'btn':'Insert',
        'form': form,
	}	

	return render(request, 'form.html', context)

def update_form(request,id):
	instance = KMA.objects.get(id=id)  #get_object_or_404(post, id=id)
	form = PostForm(request.POST or None , instance=instance)
	# cal_age = form.fields['age'].initial
	# cal_age = age_()
	try:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, 'Update Process Done for Patient ID : '  + str(instance.id))
			return HttpResponseRedirect(instance.pass_age())#, render()
	except Exception as e:
		messages.success(request, 'We Can\'t Update, Name Already Exists')
	
	var = 'Patient ID'	
	context = {
		'views_title':'Update Form',
		'page_title': 'Update Patient',
		'var': var,
        'btn':'Update',
        'form': form,
        'age_':age_,
        'instance': instance,
	}	

	return render(request, 'form.html', context)

def save_visits(request):

	form = PostVisit(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Save Process Done for ID No: ' + str(instance.id))
		return HttpResponseRedirect(instance.url_visit())

	#form.fields[''].widget = forms.HiddenInput()
	context = {
		'page_title': 'New Visit',
		'btn': 'Save',
		'form': form,
	}	

	return render(request, 'form.html', context)

def update_visits(request,id):
	instance = Visits.objects.get(id=id)  #get_object_or_404(post, id=id)
	form = PostVisit(request.POST or None , instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Update Process Done for Visit No = '  + str(instance.id))
		return HttpResponseRedirect(instance.url_visit())

	var = 'Visit No'
	context = {
		'views_title':'Update Form',
		'page_title': 'Update Visit',
		'var': var,
        'btn':'Update',
        'form': form,
        'instance': instance,
	}	

	return render(request, 'form.html', context)

###################################################
def age_(self):
	import datetime
	
	#query = KMA.objects.get()
	dob = self.birthdate
	tod = datetime.date.today()
	my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
	return my_age

	#django.utils.timezone.now()
	#return int((datetime.date.today() - KMA.birthdate).days / 365.25)


def get_age(date_birth, date_today):


	years_diff = date_today.year - date_birth.year
	months_diff = date_today.month - date_birth.month
	days_diff = date_today.day - date_birth.day
	age_in_days = (date_today - date_birth).days

	age = years_diff
	age_string = str(age) + " years"

	# age can be in months or days.
	if years_diff == 0:
	    if months_diff == 0:
	        age = age_in_days
	        age_string = str(age) + " days"
	    elif months_diff == 1:
	        if days_diff < 0:
	            age = age_in_days
	            age_string = str(age) + " days"
	        else:
	            age = months_diff
	            age_string = str(age) + " months"
	    else:
	        if days_diff < 0:
	            age = months_diff - 1
	        else:
	            age = months_diff
	        age_string = str(age) + " months"
	# age can be in years, months or days.
	elif years_diff == 1:
	    if months_diff < 0:
	        age = months_diff + 12
	        age_string = str(age) + " months" 
	        if age == 1:
	            if days_diff < 0:
	                age = age_in_days
	                age_string = str(age) + " days" 
	        elif days_diff < 0:
	            age = age-1
	            age_string = str(age) + " months"
	    elif months_diff == 0:
	        if days_diff < 0:
	            age = 11
	            age_string = str(age) + " months"
	        else:
	            age = 1
	            age_string = str(age) + " years"
	    else:
	        age = 1
	        age_string = str(age) + " years"
	# The age is guaranteed to be in years.
	else:
	    if months_diff < 0:
	        age = years_diff - 1
	    elif months_diff == 0:
	        if days_diff < 0:
	            age = years_diff - 1
	        else:
	            age = years_diff
	    else:
	        age = years_diff
	    age_string = str(age) + " years"

	if age == 1:
	    age_string = age_string.replace("years", "year").replace("months", "month").replace("days", "day")

	return age_string
