from django.contrib import admin
from .models import ExtraUserInfo,Book,BookInstance,IssueBook
admin.site.register(ExtraUserInfo)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(IssueBook)
# Register your models here.
