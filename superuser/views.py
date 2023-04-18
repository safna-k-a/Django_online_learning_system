from django.shortcuts import redirect, render
from .forms import CourseForm, OfferForm
from Myapp.models import Category,Course_details, Languages, Offer
from django.shortcuts import render, get_object_or_404
from datetime import datetime


def course(request):
    data = Languages.objects.all()
    category = Category.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('course')
        language_id = request.POST.get('language') # assuming the value of language is the id of the related Language object
        category_id = request.POST.get('category') # assuming the value of category is the id of the related Category object
        price = request.POST.get('price')
        image = request.FILES.get('image')
        description = request.POST.get('des')
        
        language = get_object_or_404(Languages, id=language_id)
        selected_category = get_object_or_404(Category, id=category_id)
        
        course = Course_details(course_name=name, language=language, category= selected_category, price=price, course_image=image, description=description)
        course.save()
        
    return render(request, "course.html", {'data': data, 'category': category})


# def offer(request):
#      data=Course_details.objects.all()
#      if request.method=='POST':
#          courseid=request.POST.get('courseid')
#          offerprice=request.POST.get('offerprice')
#          startdate=request.POST.get('startdate')
#          enddate=request.POST.get('enddate')
         
#          course = get_object_or_404(Course_details, id=courseid)
#          offer=Offer(course_id=course,offerprice=offerprice,start_date=startdate,end_date=enddate)
#          offer.save()
#      return render(request,"offer.html",{'data':data})


def offer(request):
    data = Course_details.objects.all()
    if request.method == 'POST':
        courseid = request.POST.get('course')
        offerprice = float(request.POST.get('offerprice'))
        startdate = datetime.strptime(request.POST.get('startdate'), '%Y-%m-%d').date()
        enddate = datetime.strptime(request.POST.get('enddate'), '%Y-%m-%d').date()
        course = get_object_or_404(Course_details, id=courseid)
        Offer.objects.create(course_id=course, offerprice=offerprice, start_date=startdate, end_date=enddate)
    return render(request, "offer.html", {'data': data})

 
def admin(request):
     return render(request,'admin.html')
 
def viewcourse(request):
    data = Course_details.objects.all().select_related('language', 'category')
    
    return render(request,"viewcourse.html",{'data':data})
def viewoffer(request):
    data = Offer.objects.all().select_related('course_id')
    
    return render(request,"viewoffer.html",{'data':data})



def deletecourse(request, id):
    course = Course_details.objects.get(id=id)
    course.delete()
    return redirect('viewcourse')


def updatecourse(request, id):
    course = get_object_or_404(Course_details, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('viewcourse')
    else:
        form = CourseForm(instance=course)

    return render(request, 'updatecourse.html', {'form': form})
 
def updateoffer(request, id):
    offer = get_object_or_404(Offer, id=id)
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('viewoffer')
    else:
        form = OfferForm(instance=offer)

    return render(request, 'updateoffer.html', {'form': form})
     
     
     
def deleteoffer(request, id):
    offer = Offer.objects.get(id=id)
    offer.delete()
    return redirect('viewoffer')
