# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Post

def list_posts(request):
	posts = Post.objects.all()
	return render_to_response('list_posts.html',{
		'posts': posts,
	}, context_instance=RequestContext(request)
	)