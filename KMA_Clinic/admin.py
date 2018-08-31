from django.contrib import admin
from .models import KMA
# Register your models here.

class KmaModelAdmin(admin.ModelAdmin):

	list_display  = ['name', 'address', 'birthdate', 'age', 'phone', 'husband']
	list_filter   = ['birthdate', 'name']
	search_fields = ['name', 'birthdate', 'phone'] 

	class Meta:
		model = KMA


admin.site.register(KMA,KmaModelAdmin)

