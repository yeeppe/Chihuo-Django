from django.db import models


class Comment(models.Model):
	content = models.CharField(max_length=200)
	date = models.DateField()
	def __unicode__(self):
		return '%s' % (self.content)
	
class CommentBoard(models.Model):
	comment_count = models.IntegerField()
	comments = models.ManyToManyField(Comment)
	last_updated = models.DateField()


	
	

