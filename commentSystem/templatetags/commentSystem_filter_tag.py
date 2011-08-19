from django import template
from posts.models import Post

register = template.Library()

class GetCommentsOf(template.Node):
	def __init__(self, post_id, var_name):
		self.post_id = post_id
		self.var_name = var_name
	
	def render(self, context):
		p = Post.objects.get(id=post_id)
		cs = p.comment_board
		context[self.var_name] = cs.comments
		return ''


def get_comments_of_postid(parser, token):
	try:
		tag_name, post_id, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetCommentsOf(post_id, var_name)
	
class GetCommentBoard(template.Node):
	def __init__(self, post_id, var_name):
		self.post_id = post.id
		self.var_name = var_name
	
	def render(self, context):
		p = Post.objects.get(id=post_id)
		context[self.var_name] = p.comment_board
		return ''

def get_comment_board_of_postid(parser, token):
	try:
		tag_name, post_id, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetCommentBoard(post_id, var_name)	


register.tag('get_comments_of_postid', get_comments_of_postid)
register.tag('get_comment_board_of_postid', get_comment_board_of_postid)

