from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.core import serializers

from .forms import MakeForm, CommentForm
from .models import Stu, Post

from django.views.generic import TemplateView

def display(request):
        return render(request, 'stu/base.html')

def extends(request):
        return render(request, 'stu/extends.html')

def jsonlist(request):
	querySet = Stu.objects.all()
	querySet = serializers.serialize('json', querySet)
	return HttpResponse(querySet, content_type="application/json")

def index(request):
	if request.user.is_authenticated:
		context = {
			"title": request.user
		}
	else:
		context = {
			"title": "Not Logged"
		}
	return render(request, 'stu/index.html', context)

def stu_list(request):
	querySet = Stu.stusobjects.all()

	query = request.GET.get('qry')
	if query:
		querySet = querySet.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name__icontains=query) |
			Q(user__last_name__icontains=query)
			).distinct()

	context = {
		"stu_list": querySet,
		"title": "stuList"
	}

	return render(request, "stu/list_view.html", context)


def stu_detail(request, slug=None):
	instance = get_object_or_404(Stu, slug=slug)
	context = {
		"instance": instance,
	}
	return render(request, 'stu/detail_view.html', context)

def stu_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	if not request.user.is_authenticated:
		raise Http404

	form = MakeForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()

		messages.success(request, "Successfully created")
		return redirect('Stu:list')
	else:
		messages.error(request, "Not Successfully created")
	context = {
		"form": form,
	}
	return render(request, "stu/form.html", context)

def stu_update(request, id=None):
	instance = get_object_or_404(Stu, id=id)
	form = MakeForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('http://127.0.0.1:8000/stus/list/')

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form
	}
	return render(request, 'stu/form.html', context)

def stu_delete(request, id=None):
	instance = get_object_or_404(Stu, id=id)
	messages.success(request, "Successfully deleted")
	return redirect('Stu:list')

def add_comment(request, article_id):
	a = Stu.stusobjects.get(id=article_id)
	s = a.slug

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			c=form.save(commit=False)
			c.article = a
			c.save()
			messages.success(request, 'added comment')
			return redirect('Stu:detailpost', slug=s)
	else:
		form = CommentForm()
		messages.error(request, "comment not added")
	context = {
		"form": form,
	}
	return render(request, "stu/comment.html", context)

def like(request, id=None):
	if id:
		a = Stu.stusobjects.get(id=id)
		count = a.likes
		count += 1
		a.likes = count
		a.save()

	return redirect('Stu:list')

