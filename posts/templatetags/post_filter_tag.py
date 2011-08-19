from django import template
from posts.models import Category
from posts.models import Post

register = template.Library()

class SubCategoryOf(template.Node):
	def __init__(self, parent_category_id, var_name):
		self.parent_category_id = parent_category_id
		self.var_name = var_name
	
	def render(self, context):
		context[self.var_name] = Category.objects.filter(parent__id=self.parent_category_id)
		return ''

def get_sub_category_of(parser, token):
	try:
		tag_name, parent_category_id,as_word, var_name= token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return SubCategoryOf(parent_category_id, var_name)

class GetCategoryOf(template.Node):
	def __init__(self, category_id, var_name):
		self.category_id = category_id
		self.var_name = var_name
	
	def render(self, context):
		context[self.var_name] = Category.obejcts.get(id=self.category_id)
		return ''

def get_category_of(parser, token):
	try:
		tag_name, category_id, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetCategoryOf(category_id, var_name)


class GetPosts(template.Node):
	def __init__(self, from_id, number_posts, var_name, order_by):
		self.from_id = from_id
		self.number_posts = number_posts
		self.var_name = var_name
		self.order_by = order_by

	def render(self, context):
		context[self.var_name] = Post.objects.order_by(self.order_by)[self.from_id:self.number_posts]
		return ''


def get_posts_from(parser, token):
	try:
		# get_latest_posts_from 1 count 5 orderby DATE as posts_list
		tag_name, from_id, count_word, number_posts, orderby_word, order_by, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetPosts(from_id, number_posts, var_name, order_by)

class GetSinglePost(template.Node):
	def __init__(self, post_id, var_name):
		self.post_id = post_id
		self.var_name = var_name
	
	def render(self, context):
		context[self.var_name] = Post.objects.get(id=self.post_id)
		return ''

def get_single_post(parser, token):
	try:
		tag_name, post_id, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetSinglePost(post_id, var_name)



register.tag('get_single_post', get_single_post)
register.tag('get_sub_category_of', get_sub_category_of)
register.tag('get_posts_from', get_posts_from)
register.tag('get_category_of', get_category_of)




