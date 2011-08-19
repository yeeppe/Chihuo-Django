from django import template
from rsvp.models import ChihuoActivity


register = template.Library()


# 1.1
class GetAllActivities(template.Node):
	def __init__(self, var_name):
		self.var_name = var_name
	
	def render(self, context):
		context[self.var_name] = ChihuoActivity.objecs.all()
		return ''

#  1.2
# USAGE: {% get_all_chihuo_activities as activity_list %}
def get_all_chihuo_activities(parser,token):
	try:	
		tag_name, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetAllActivities(var_name)
	
	
register.tag('get_all_chihuo_activities', get_all_chihuo_activities)

