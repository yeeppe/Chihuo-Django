from django.db import models
from users.models import User
from restaurants.models import Shop

class Participant(models.Model):
	user = models.ForeignKey(User)

class Initiator(models.Model):
	user = models.ForeignKey(User)

class ChihuoEvent(models.Model):
	initiator = models.ForeignKey(Initiator)
	date = models.DateField()
	opacity = models.IntegerField()
	participants = models.ManyToManyField(Participant)
	place = models.ForeignKey(Shop)
	description = models.TextField(max_length=200)


