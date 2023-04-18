from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class userImage(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images') 
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50)
class Languages(models.Model):
    language=models.CharField(max_length=50)
class Course_details(models.Model):
    course_name=models.CharField(max_length=50)
    language=models.ForeignKey(Languages,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.IntegerField()
    course_image=models.ImageField(upload_to='images/')
    description=models.TextField(default="why we learn ?")
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course_details,on_delete=models.CASCADE)
    status=models.IntegerField()
class Offer(models.Model):
    course_id=models.ForeignKey(Course_details,on_delete=models.CASCADE)
    offerprice=models.IntegerField()
    start_date=models.DateField() 
    end_date=models.DateField() 
    def __str__(self):
        return self.course_id
# class join_table(models.Model):
#     tableId = models.AutoField(primary_key=True)
#     course = models.ForeignKey("Course_details", null=False, db_column="course_name")
#     offer = models.ForeignKey("Offer", null=False, db_column="sessionId")
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course_details,on_delete=models.CASCADE)
    status=models.IntegerField()



class CartItem(models.Model):
    item = models.ForeignKey(Course_details, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.item}"
   


