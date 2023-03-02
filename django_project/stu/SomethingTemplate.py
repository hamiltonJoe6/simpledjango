class SomethingTemplate(TemplateView):
        template_name = "stu/stuview.html"

        def get(self, request):
                form = StuForm()
                post = Post.objects.all()
                print(post)
                context = {'form': form, 'post': post}
                return render(request, self.template_name, context)

        def post(self, request):
                form = StuForm(request.POST)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.save()
                        text = form.cleaned_data['post']
                        form = StuForm()
                        return redirect(reverse('Stu:templateView'))

                context = {'form': form, 'text': text}
                return render(request, self.template_name, context)
