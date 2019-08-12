from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Posts, Comment
from .forms import contactForm, commentForm
from django.http import HttpResponseRedirect



def Home(request):
    return render(request, 'subProject/index.html')

class PostListView(ListView):
    model = Posts
    template_name = "subProject/post.html"

def Details(request, post_id):
    post = Posts.objects.get(id=post_id)
    comment = Comment.objects.filter(post=post, reply=None).order_by('-date')
    if request.method == "POST":
        content_form = commentForm(request.POST or None)
        if content_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return redirect('post')
        else:
            print("the form is not valid")
    else:
        form = commentForm()
    context = {"post":post, "form":form, "comment":comment}
    return render(request, 'subProject/detail.html', context)

def Contact(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = contactForm()
    return render(request, 'subProject/contact.html', {'form':form})


