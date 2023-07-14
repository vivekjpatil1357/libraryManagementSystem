from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('home/',home,name='home'),
    path('register/',register,name='register'),
    path('addbook/',AddBook.as_view(),name='AddBook'),
    path('bookinstance/',AddBookInstance.as_view(),name='AddBookInstance'),
    path('listbooks/',ListBooks.as_view(),name='ListBooks'),
    path('issuebookinstance/',issueBookInstance,name='IssueBookInstance'),
    path('borrowerInfo/<int:id>',listBorrowerInfo,name='listBorrowerInfo'),
    
]

