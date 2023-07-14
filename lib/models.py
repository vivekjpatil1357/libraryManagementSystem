from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime,timedelta
# Create your models here.
class ExtraUserInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=10)
    choices=[('male','Male'),('female','Female')]
    gender=models.CharField(default='',max_length=10,choices=choices)

class Book(models.Model):
        title=models.CharField(default='',max_length=50)
        author=models.CharField(default='',max_length=50)
        choice=[('education','Education'),('entertainment','Entertainment'),('science','Science')]
        # category=models.CharField(default='',choices=choice)
        category=models.CharField(choices=choice,max_length=30)

        def __str__(self) :
              return self.title
        
class BookInstance(models.Model):
      isbn=models.UUIDField(primary_key=True,default=uuid.uuid4)
      
      is_borrowed=models.CharField(max_length=10,default='false')
      book=models.ForeignKey(Book,on_delete=models.CASCADE)
      def __str__(self) -> str:
            return f'{self.book.title} :{self.isbn}'
      
def returnDate():
      return datetime.today()+ timedelta(days=8)


class IssueBook(models.Model):
      borrower=models.ForeignKey(User,on_delete=models.CASCADE)
      book=models.ForeignKey(BookInstance,on_delete=models.CASCADE)
      issue_date=models.DateField(auto_now=True)
      return_date=models.DateField(default=returnDate())
      def __str__(self) -> str:
            return f' {self.book.isbn} : {self.book.book.title}'
    