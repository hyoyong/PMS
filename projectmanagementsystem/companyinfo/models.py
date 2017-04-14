# coding: utf-8
from django.db import models

# Create your models here.

class CompanyInfo(models.Model):
	id = models.IntegerField(primary_key=True)
	technology_select = models.CharField(max_length=10, null=True)
	created_date = models.DateField(null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	business = models.CharField(max_length=200, null=True, blank=True)
	name = models.CharField(max_length=20, null=True, blank=True)
	contact = models.CharField(max_length=20, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	position = models.CharField(max_length=20, null=True, blank=True)
	reference = models.CharField(max_length=2000, null=True, blank=True)
#	cdate = models.DateTimeField(auto_now_add=True)
	hits = models.IntegerField(default=0, null=True, blank=True)
