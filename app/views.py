from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect


def index(request):
    comments = Comment.objects.all().order_by('-time')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return render(request, 'app/index.html', {'form': form, 'comments': comments})