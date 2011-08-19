from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from posts.models import Category
from posts.models import Post

def main_view(request):
	return render_to_response('index/index.html',{})
	
def category_view(request,category):
	c = get_object_or_404(Category, id=category)	# get category
	post_list = Post.objects.all()
	return render_to_response('category/index.html',
		{
			'title'				:	c.category_name,
			'post_list'			:	post_list,
		}
	)


def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
					Q(title__icontains=query)
		)
		results = Post.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response('index/search.html',
			{
				"results"	:	results,
				"query"		: 	query
			})