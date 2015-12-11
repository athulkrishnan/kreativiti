from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class SignUp(models.Model):
	name = models.CharField(max_length=100, verbose_name='')
	email = models.EmailField(verbose_name='')
	phone = models.CharField(max_length=14, verbose_name='')
	location = models.CharField(max_length=20, verbose_name='')
	details = models.CharField(max_length=1000, blank=True, verbose_name='')
	# verbose_name='' inside fields to hide name
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.email)