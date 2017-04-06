from django.forms import ModelForm
from companyinfo.models import *

class Form(ModelForm):
	class Meta:
		model = CompanyInfo
		fields = ['name','business','reference','url','contact','position','phone','email']

