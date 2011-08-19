from django.db import models
from stats.models import UserStat
from posts.models import Post
from commentSystem.models import Comment

GENDER_CHOICES = (
		(u'M', u'Male'),
		(u'F', u'Female'),
		(u'O', u'Other'),
)

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
	email = models.EmailField()
	register_date = models.DateField()
	user_stat = models.ForeignKey(UserStat)
	comments = models.ManyToManyField(Comment)
	#headshot = models.ImageField(upload_to="static/users/headshot")
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)
#
#class SuperAdmin(User):
#	some_attribute = models.CharField(max_length=50)
	
#class Admin(User):
#	some_attribute = models.IntegerField()

class Editer(User):
	posts = models.ManyToManyField(Post)
	
class Contributor(User):
	posts = models.ManyToManyField(Post)

#class Vistor(User):
#	some = models.IntegerField()
	