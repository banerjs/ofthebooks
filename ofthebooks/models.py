from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

# Create your models here.

class BookReview(models.Model):
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=500)
	rating = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(5), MinValueValidator(1)])
	amazon_url = models.URLField(null=True, blank=True, max_length=1000)
	amazon_image_url = models.URLField(null=True, blank=True, max_length=1000)
	review = models.TextField(null=True, blank=True)
	slug = models.SlugField(max_length=1000, blank=True, editable=False, unique=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title + ' by ' + self.author

	def save(self, *args, **kwargs):
		self.slug = slugify(self.author + ' ' + self.title)
		super(BookReview, self).save(*args, **kwargs)
