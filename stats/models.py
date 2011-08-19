from django.db import models

class UserStat(models.Model):
	profile_views = models.IntegerField()


class PostStat(models.Model):
	post_views = models.IntegerField()
	likes = models.IntegerField()


