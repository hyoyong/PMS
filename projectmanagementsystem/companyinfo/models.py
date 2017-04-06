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

		verbose_name = "기술종류",
	)

	url = models.URLField()
	url.verbose_name = "홈페이지"

	business = models.CharField(max_length=200)
	business.verbose_name = "진행사업"

	name = models.CharField(max_length=20)
	name.verbose_name = "회사명"

	contact = models.CharField(max_length=20)
	contact.verbose_name = "업체담당자"

	phone = models.CharField(max_length=20)
	phone.verbose_name = "전화번호"

	email = models.EmailField()
	email.verbose_name = "이메일"

	position = models.CharField(max_length=20)
	position.verbose_name = "직급"

	reference = models.CharField(max_length=2000)
	reference.verbose_name = "양산경험"

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
