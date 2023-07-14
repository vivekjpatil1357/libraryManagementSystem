from typing import Any
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
# from django.views.generic import 
# Create your views here.
def index(request):
    lst=IssueBook.objects.all()
    # borrower=lst[0]
    # name=borrower.first_name + borrower.last_name
    # lst[0]=name
    for i in lst:
        if i.borrower_id == i.borrower.id:
            count+=1
    return render(request,'lib/index.html',{'data':lst})

def listBorrowerInfo(request,id):
    # request.method =='POST':
    user=User.objects.get(id=id)
    # i=IssueBook.objects.all(borrower=user)
    lst=IssueBook.objects.filter(borrower_id=id)
    
    return render(request,'lib/listBorrowerInfo.html',{'data':lst,'user':user})

    # else:
    #     return render(request,'lib/listBorrowerInfo.html',{'data':lst})



def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request,'lib/login.html')

def home(request):
        return render(request,'lib/home.html')
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        gender=request.POST.get('gender')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        try :
            user=User.objects.get(username=username)
            return render(request,'lib/register.html',{'error':"user already exists"})
        except:
            if password1==password2:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                ExtraUserInfo.objects.create(user=user,mobile=mobile,gender=gender)
                return redirect('login')
            else:
                return render(request,'lib/register.html',{'error':"Password not matching"})
    else:
        return render(request,'lib/register.html')

class AddBook(CreateView):
    model=Book
    fields='__all__'
    success_url=reverse_lazy('home')

class AddBookInstance(CreateView):
    model=BookInstance
    fields='__all__'
    success_url=reverse_lazy('home')


def issueBookInstance(request):
    if request.method=='POST':
        username=request.POST.get('borrower')
        borrower=User.objects.get(username=username)
        temp=str(request.POST.get('book'))
        isbn=temp.split(':')[-1]
        
        book=BookInstance.objects.get(isbn=isbn)
        book.is_borrowed='true'
        book.save()
        IssueBook.objects.create(borrower=borrower,book=book)
        return render(request,'lib/home.html')
    else:
        lst2=list(BookInstance.objects.filter(is_borrowed='false').all())
        lst1=list(User.objects.all())
        return render(request,'lib/issuebook_form.html',{'d1':lst1,'d2':lst2})

class ListBooks(ListView):
    model=Book
    
# class issueBookInstance(CreateView):
#     model=IssueBook
    
#     BookInstance.is_borrowed='true'
#     fields='__all__'
#     queryset=BookInstance.objects.filter(is_borrowed=False).all()
#     success_url=reverse_lazy('home')
#     def form_valid(self, form):
#         response = super().form_valid(form)

#         # Update the value in the table
#         BookInstance.is_borrowed = 'true'  # Replace with the new value you want to assign
#         BookInstance.is_borrowed.save()

#         return response
# borrow or not
