from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.html import escape
from hello.models import C
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.http import urlencode
from django.urls import reverse_lazy
from hello.forms import MakeForm

from hello.forms import BasicForm
from django.contrib import messages

def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")

class AboutView(TemplateView):
	template_name = 'hello/about.html'

class Anotherindex(View):
	def get(self, request):
		try:
			hello_list = C.objects.values()
			context = {'hello_list': hello_list}
		except C.DoesNotExist:
			raise Http404("does not exist")
		return render(request, 'hello/index.html', context)

def detail(request, pk_from_url):
	detail_list = get_object_or_404(C, pk=pk_from_url)
	return render(request, 'hello/details.html', {'detail_list':detail_list})

class AnotherDetail(View):
	def get(self, request, pk_from_url):
		try:
			detail_list = C.objects.get(pk=pk_from_url)
			context = {'detail_list': detail_list}
		except C.DoesNotExist:
			raise Http404("does not exist")
		return render(request, 'hello/detail.html', context)

def guess(request):
        response = """<html></body>
                <p>Your guess is """+escape(request.GET['guess'])+"""</p>
                </body></html>"""
        return HttpResponse(response)

#reverse -- https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#reverse
#basically ued to include an url link from View
class LoginGetView(View):
        def get(self, req):
                res = "<pre>\n User Data in Python:\n\n"
                res += "Login url: " + reverse('login') + '\n'
                if req.user.is_authenticated:
                        res += "User: " + req.user.username + "\n"
                        res += "Email: " + req.user.email + "\n"
                else:
                        res += "User is not logged in\n"
                return HttpResponse(res)


class ManualProtect(View) :
    def get(self, request):
        if not request.user.is_authenticated :
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'hello/main.html')


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        c = C.objects.all()
        context = {'c_list': c}
        return render(request, 'hello/c_list.html', context)

class MakeCreate(LoginRequiredMixin, View):
    template = 'hello/make_form.html'
    success_url = reverse_lazy('helloview:main')
    def get(self, request):
        form = MakeForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)
    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        make = form.save()
        return redirect(self.success_url)

class MakeUpdate(LoginRequiredMixin, View):
    model = C
    success_url = reverse_lazy('helloview:main')
    template = 'hello/make_form.html'
    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'form': form}
        return render(request, self.template, ctx)
    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin, View):
    model = C
    success_url = reverse_lazy('helloview:main')
    template = 'hello/confirm_delete.html'
    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'make': make}
        return render(request, self.template, ctx)
    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)

class MyView(View):
    template_name = None
    def get(self, request) :
        old_data = {
            'title': 'Something',
	    'description': 'Description'
        }
        form = BasicForm(initial=old_data)
        ctx = {'form' : form}
        return render(request, self.template_name, ctx)
