# Create your views here.





#def post_comment(request, new_comment):
#	if request.session.get('has_commented', False):
#		return HttpResponse("You have already commented.")
#	c = comments.Comment(comment=new_comment)
#	c.save()
#	request.session['has_commented'] = True
#	return HttpResponse('Thanks for your comment!')