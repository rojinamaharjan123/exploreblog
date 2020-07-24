from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class TimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	is_active = models.BooleanField(default=True)

	class Meta:
		abstract = True


class Admin(TimeStamp):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	address = models.CharField(max_length=100, null=True, blank=True)

	def save(self, *args, **kwargs):
		grp, created = Group.objects.get_or_create(name="Admin")
		self.user.groups.add(grp)

		super().save(*args, **kwargs)

	def __str__(self):
		return self.name


class Customer(TimeStamp):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	address = models.CharField(max_length=100)

	def save(self, *args, **kwargs):
		grp, created = Group.objects.get_or_create(name="Customer")
		self.user.groups.add(grp)

		super().save(*args, **kwargs)

	def __str__(self):
		return self.name


class Category(TimeStamp):
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to="category")
	description = models.TextField()
	# root = models.ForeignKey(
	# 	"self", on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.title


class Article(TimeStamp):
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to="article")
	category = models.ForeignKey(
		Category, on_delete=models.SET_NULL, null=True, blank=True)
	description = models.TextField()
	author = models.OneToOneField(Customer, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Website(TimeStamp):
	name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to="logo")
	email = models.EmailField()
	phone_no = models.CharField(max_length=50)
	address = models.CharField(max_length=100, null=True, blank=True)
	facebook = models.CharField(max_length=100, null=True, blank=True)
	twitter = models.CharField(max_length=100, null=True, blank=True)
	instagram = models.CharField(max_length=100, null=True, blank=True)
	about = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name


