from django.shortcuts import render

from django.shortcuts import render
# Create your views here.
from  apps.models import *
from django.http import Http404,HttpResponse
from apps.forms import CommentForm

def index(request):
    return render(request,'index.html')

def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    return render(request,'blog_list.html',{'blogs':blogs})
def get_details(request,blog_id):
    try:
        blog = Blog.objects.get(id = blog_id)
    except Blog.DoesNotExist:
        return HttpResponse('你好，你搜索的博客序号不对')
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    content = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog_details.html', content)

