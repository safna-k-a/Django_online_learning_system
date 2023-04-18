from django.http import HttpResponseBadRequest
from django.shortcuts import render
import razorpay
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from flask import Flask,request

from Myapp.models import Cart, Course_details
# Create your views here.
# def Home(request):
#     return render(request,"app.html")

app = Flask(__name__,static_folder = "static", static_url_path='')
razorpay_client = razorpay.Client(auth=("rzp_test_acgCaQhDp1w1uK", "8egrozmgdp1GGzZ2DYvNNRcl"))

def app_create(request):
    
    return render(request,"app.html")

@csrf_exempt
def app_charge(request,id,pk):
    if request.method == 'POST':
      
        #amount = 5100
        user=User.objects.get(id=pk)
        course=Course_details.objects.get(id=id)
        amount=course.price
        course_name=course.course_name
        Cart.objects.create(status=1,course_id=id,user_id=pk)
        # payment_id = request.POST.get('razorpay_payment_id')
        # razorpay_client.payment.capture(course_name,amount)
        return render(request,"charge.html",{'course_name':course_name,'amount':amount,'user':user})
    else:
        return HttpResponseBadRequest()

if __name__ == '__main__':
    app.run()
