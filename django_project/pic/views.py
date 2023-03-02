from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from pic.models import Pic
from pic.forms import CreateForm

def index(request):
    return HttpResponse("Hello, world. this is the pictures index")

class PicListView(OwnerListView):
    model = Pic
    template_name = "pic/list.html"

class PicDetailView(OwnerDetailView):
    model = Pic
    template_name = "pic/detail.html"

class PicCreateView(LoginRequiredMixin, View):
    template_name = 'pic/form.html'
    success_url = reverse_lazy('pic:all')

    def get(self, request, pk=None):
        form = CreateForm()

        ctx = {'form': form}
        return render(request, self.template_name, ctx)
    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

class PicUpdateView(LoginRequiredMixin, View):
	template_name = 'pic/form.html'
	success_url = reverse_lazy('pic:all')

	def get(self, request, pk):
		pic = get_object_or_404(Pic, id=pk, owner=self.request.user)
		form = CreateForm(instance=pic)
		ctx = {'form': form}
		return render(request, self.template_name, ctx)

	def post(self, request, pk=None):
		pic = get_object_or_404(Pic, id=pk, owner=self.request.user)
		print(pic)
		form = CreateForm(request.POST, request.FILES or None, instance=pic)
		if not form.is_valid():
			ctx = {'form': form}
			return render(request, self.template_name, ctx)

		pic = form.save(commit=False)
		pic.owner = self.request.user
		pic.save()
		return redirect(self.success_url)

class PicDeleteView(OwnerDeleteView):
	model = Pic
	template_name = "pic/delete.html"

def stream_file(request, pk):
    pic = get_object_or_404(Pic, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
