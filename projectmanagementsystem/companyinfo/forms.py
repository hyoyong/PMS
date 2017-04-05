from django.forms import ModelForm
from companyinfo.models import *

class Form(ModelForm):
	class Meta:
		model = CompanyInfo
		fields = ['url','business','name','contact','phone','email','position','reference']

