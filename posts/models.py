from django.db import models
from commentSystem.models import CommentBoard
from stats.models import PostStat

class Category(models.Model):
	category_name = models.CharField(max_length=50)
	parent = models.ForeignKey("self",null=True, blank=True)
	def __unicode__(self):
		return '%s' % (self.category_name)

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField(max_length=1000)
	date = models.DateField()
	post_stat = models.ForeignKey(PostStat)
	comment_board = models.ForeignKey(CommentBoard)
	categories = models.ManyToManyField(Category)
	def __unicode__(self):
		return '%s' % (self.title)
		
#class SnackPost(Post):
	#some = models.CharField(recommendation)
	#some1 = models.CharField(direction)



