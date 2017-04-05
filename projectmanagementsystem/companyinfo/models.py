from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
	AUTO = 'AU'
	CE = 'CE'
	IOT = 'IOT'
	TECHNOLOGY_TYPE = (
		(AUTO, 'AUTOMOTIVE'),
		(CE, 'CONSUMER'),
		(IOT, 'IOT'),
	)
	technology_select = models.CharField(
		max_length = 3,
		choices = TECHNOLOGY_TYPE,
	)
	url = models.URLField()
	business = models.CharField(max_length=200, default = '')
	name = models.CharField(max_length=20)
	contact = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	email = models.EmailField()
	position = models.CharField(max_length=20)
	reference = models.CharField(max_length=2000)
	cdate = models.DateTimeField(auto_now_add=True)

'''
class TechnologyType(models.Model):
	TECHNOLOGY_TYPE = (
		(AUTO, 'AUTOMOTIVE'),
		(CE, 'CONSUMER'),
		(IOT, 'IOT'),
	)
	technology_select = models.CharField(
		max_length = 3,
		choice = TECHNOLOGY_TYPE,
	)

class URLField(CharField):
	default_validators = [validators.URLValidator()]
	description =
'''
