from django.forms import ModelForm
from companyinfo.models import *

class Form(ModelForm):
	class Meta:
		model = CompanyInfo
		fields = ['name','technology_select','business','reference','url','contact','position','phone','email']
