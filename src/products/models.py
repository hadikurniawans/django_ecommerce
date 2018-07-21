import random
import os
from django.db import models

# Create your models here.

def get_filename_ext(filepath):
	base_name  	 = os.path.base_name(filepath)
	name, ext 	 = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1,123212)
	name, ext    = get_filename_ext(filename)
	final_name	 = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_name}".format(
		new_filename=new_filename, 
		final_name=final_name)

class Product(models.Model):
	title 		 = models.CharField(max_length=120)
	description  = models.TextField()
	price 		 = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	image		 = models.FileField(upload_to='products/', null=True, blank=False)

	def __str__(self):
		return self.title
