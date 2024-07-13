from django.shortcuts import render
# the next line (3) can be deleted once post_list.html has been created *
# from django.http import HttpResponse
# * add the following instead:
from django.views import generic
from .models import Post

# Create your views here.
# the next lines (6 and 7) can be deleted once post_list.html has been created
# def my_blog(request):
# 	return HttpResponse("Hello, Blog!")
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3
