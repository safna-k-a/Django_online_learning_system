from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from Myapp.models import Cart, CartItem, Course_details, Offer, userImage
from .forms import CreateUserForm, ImageForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def Index(request):
    expired_events = Offer.objects.filter(end_date__lt=timezone.now())
    expired_events.delete()
    object=Course_details.objects.all()
    offer=Offer.objects.all()
    obj1=object.filter(language=1)
    php=object.filter(language=2)
    obj2=object.filter(language=3)
    if request.method=="POST":
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None: # Check if user object is not None
            if user.is_superuser:  # Check if user is admin
                login(request,user)
                return redirect('/adminurl')
            else:  # If not admin, login as normal user
                login(request,user)
                return redirect('/dashboard')
    return render(request,'index.html',{'python':obj1,'js':obj2,'php':php,'offer':offer})

def signup(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if user_form.is_valid() and image_form.is_valid():
            # Create the User object
            user = user_form.save()
            Image = image_form.save(commit=False)
            Image.user = user
            Image.save()
            return redirect('/')
    else:
        user_form = CreateUserForm()
        image_form=ImageForm()
    return render(request, 'signup.html', {'user_form': user_form,'image_form': image_form})


def loginpage(request):
    
    if request.method=="POST":
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None: # Check if user object is not None
            if user.is_superuser:  # Check if user is admin
                login(request,user)
                return redirect('/adminurl')
            else:  # If not admin, login as normal user
                login(request,user)
                return redirect('/dashboard')
    return render(request,'index.html')

# @login_required(login_url="/")
def dashboard(request):
    try:
        quantity1 = CartItem.objects.filter(user=request.user)
        c=quantity1.count()
    except CartItem.DoesNotExist:
        quantity = 0
    object=Course_details.objects.all()
    offer=Offer.objects.all()
    obj1=object.filter(language=1)
    php=object.filter(language=2)
    obj2=object.filter(language=3)
    obj = userImage.objects.get(user=request.user)
    return render(request,"dashboard.html",{'data':obj,'python':obj1,'js':obj2,'php':php,'offer':offer,'count':c})
def logout1(request):
    logout(request)
    return redirect("/")
@login_required(login_url="/")
def admin_dash(request):
    obj = userImage.objects.get(user=request.user)
    return render(request,"../../superuser/templates/admin.html",{'data':obj})
def buy(request,id):
    course = Course_details.objects.get(id=id)
    return render(request,"details.html",{'course':course})
def buy1(request,id):
    course = Offer.objects.get(course_id=id)
    return render(request,"detailsoffer.html",{'course':course})
@login_required(login_url="/")
def app(request,id,pk):
    print(id)
    course = Course_details.objects.get(id=id)
    cart=CartItem.objects.get(id=pk)
    amount=cart.amount*100
    return render(request,"../../payment/templates/app.html",{'course':course,'amount':amount,'cart':cart})
@login_required(login_url="/")
def app1(request,id):
    course = Course_details.objects.get(id=id)
    amount=course.price*100
    return render(request,"../../payment/templates/app1.html",{'course':course,'amount':amount})
def log(request,id):
    course = Course_details.objects.get(id=id)
    
    if request.method=="POST":
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('app',id)
    return render(request,'details.html',{'course':course})
def log1(request,id):
    course = Course_details.objects.get(id=id)
    
    if request.method=="POST":
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('app1',id)
    return render(request,'details.html',{'course':course})
def search(request):
    return render(request,'search.html')

def search_course(request):
        query = request.GET.get('q')
        course_obj = Course_details.objects.filter(course_name__icontains=query)
        return render(request, 'search.html', {'course': course_obj})
def my_course(request,id):
        course=Cart.objects.filter(user_id=id)
        image=userImage.objects.get(user_id=id)
        return render(request, 'my_course.html', {'course':course,'data':image})
def loginsearch(request):
        query = request.GET.get('q')
        course_obj = Course_details.objects.filter(course_name__icontains=query)
        return render(request, 'loginsearch.html', {'course': course_obj})
    

def add_to_cart(request, id):
    item = get_object_or_404(Course_details, pk=id)
    try:
        quantity1 = CartItem.objects.filter(user=request.user)
        c=quantity1.count()
    except CartItem.DoesNotExist:
        quantity1 = 0
  
    # Get the user's cart
    

    # Add the item to the cart or update its quantity
    if request.user.is_authenticated:
        for item1 in quantity1:
            if item1.item.id == id:
                messages.error(request, "Already added to cart")
                break
        else:
            cart_item= CartItem(user=request.user,item=item,amount=item.price)
            cart_item.quantity = 1
            cart_item.amount=item.price*cart_item.quantity
            cart_item.save()

        return redirect('/dashboard',{'quantity':quantity1,'count':c })  
    else:
        # If the user is not authenticated, redirect to the login page
        return redirect('login')
def cartitem(request):
    course=CartItem.objects.filter(user=request.user)
    return render(request,'cartitems.html',{'course':course})


def add_to_cart1(request, id):
    item = get_object_or_404(Course_details, pk=id)
    try:
        quantity1 = CartItem.objects.filter(user=request.user)
    except CartItem.DoesNotExist:
        quantity1 = 0
    # Get the user's cart
    

    # Add the item to the cart or update its quantity
    if request.user.is_authenticated:
        
        cart_item, created = CartItem.objects.get_or_create(user=request.user,item=item)
        if not created:
            cart_item.quantity += 1
            cart_item.amount=item.price*cart_item.quantity
            cart_item.save()

        return redirect('/cartitem',{'quantity':quantity1})  
    else:
        # If the user is not authenticated, redirect to the login page
        return redirect('login')
def delete_cart(request, id):
    item = get_object_or_404(CartItem, pk=id)
    try:
        quantity1 = CartItem.objects.filter(user=request.user)
    except CartItem.DoesNotExist:
        quantity1 = 0
    item.delete()
    return redirect('/cartitem',{'quantity':quantity1})
    
    