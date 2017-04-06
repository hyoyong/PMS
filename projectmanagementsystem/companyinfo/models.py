# coding: utf-8
from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
	AUTO = 'AU'
	CE = 'CE'
	IOT = 'IOT'
	ALL = 'ALL'
	TECHNOLOGY_TYPE = (
		(AUTO, 'AUTOMOTIVE'),
		(CE, 'CONSUMER'),
		(IOT, 'IOT'),
		(ALL, 'ALL'),
	)
	technology_select = models.CharField(
		max_length = 3,
		choices = TECHNOLOGY_TYPE,
		default = ALL,
	)

	id = models.IntegerField(primary_key=True)
	created_date = models.DateField(null=True, blank=True)
	url = models.URLField()
	business = models.CharField(max_length=200)
	name = models.CharField(max_length=20)
	contact = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	email = models.EmailField()
	position = models.CharField(max_length=20)
	reference = models.CharField(max_length=2000)
#	cdate = models.DateTimeField(auto_now_add=True)
#	hits = models.IntegerField()
