from django.contrib import admin
from hello.models import C, Book, Author, Authored, Person, Course, Membership

admin.site.register(C)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Authored)
admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Membership)
