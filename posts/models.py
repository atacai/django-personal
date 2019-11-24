from django.db import models

class Post(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

	username		= models.CharField(max_length=20, blank=False, null=False)
	gender 			= models.CharField(max_length=6, choices=GENDER_CHOICES, default='M')
	post_text		= models.TextField(blank=False, null=False)
	time				= models.DateTimeField(auto_now_add=True)