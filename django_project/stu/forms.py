from django.forms import ModelForm
from django import forms
from stu.models import Stu, Comment, Post

class MakeForm(ModelForm):
	class Meta:
		model = Stu
		fields = ['title', 'content', 'image', 'likes']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'body']

class PostForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control',
		}
	))

	class Meta:
		model = Post
		fields = ['post']
