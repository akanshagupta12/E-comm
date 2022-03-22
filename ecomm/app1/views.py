from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import conf
from .models import Products
from .models import Cart
from django.contrib import messages
from django.db.models import  F
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from decouple import config

# Create your views here.
def home(request):
    return render(request , 'index.html')

def product_view(request):
    result= Products.objects.all()
    count= Cart.objects.all().count()
    # print(obj.data)
    print(type(result))
    print(result)
    return render(request , 'products.html' , {'data': result , 'count':count})

def add_item_to_cart(request ,  *args , **kwargs):
    print("in add item to cart function")
    item = list(Products.objects.filter(id=kwargs.get('pk')).values())
    cart_item = Cart.objects.filter(name=item[0]['name'])
    print(len(cart_item))
    if len(cart_item)>0:
        print("in if--------------------")
        Products.objects.filter(name=item[0]['name']).update(in_cart = True)
        messages.success(request, 'Item Already in Cart. Kindly , proceed for checkout 😊')
        return redirect('/home/products/')
    else:
        print("in else +++++++++++++++++")
        Products.objects.filter(name=item[0]['name']).update(in_cart = True)
        Cart.objects.create(id= kwargs.get('pk'), name=item[0]['name'] , mrp = item[0]['mrp'] , csp = item[0]['csp'] , image = item[0]['image'])
        messages.success(request, 'Item added to cart successfully.')
        return redirect('/home/products/')

def add_quantity_in_cart(request ,  *args , **kwargs):
    # print(request.kwargs.get('pk'))
    item = list(Products.objects.filter(id=kwargs.get('pk')).values())
    cart_item = list(Cart.objects.filter(name=item[0]['name']).values())
    print("cart items" , cart_item )
    print(len(cart_item))
    if len(cart_item)>0:
            Cart.objects.filter(name=item[0]['name']).update(quantity=F('quantity')+1)
            Products.objects.filter(name=item[0]['name']).update(in_cart = True)
            print(list(Products.objects.filter(name=item[0]['name'])))
            messages.success(request, 'Item quantity added.')
            return redirect('/home/order/')

def remove_quantity_in_cart(request ,  *args , **kwargs):
    # print(request.kwargs.get('pk'))
    item = list(Products.objects.filter(id=kwargs.get('pk')).values())
    cart_item = list(Cart.objects.filter(name=item[0]['name']).values())
    print("cart items" , cart_item )
    print(len(cart_item))
    if len(cart_item)>0:
        if cart_item[0]['quantity']==1:
            Cart.objects.filter(id=kwargs.get('pk')).delete()
            Products.objects.filter(id=kwargs.get('pk')).update(in_cart = False)
            return redirect('/home/order/')
        else:
            print("in if----------------------------")
            Cart.objects.filter(name=item[0]['name']).update(quantity=F('quantity')-1)
            messages.success(request, 'Item quantity decreased.')
            return redirect('/home/order/')

def delete_item_from_cart(request ,  *args , **kwargs):
            Cart.objects.filter(id=kwargs.get('pk')).delete()
            Products.objects.filter(id=kwargs.get('pk')).update(in_cart = False)
            return redirect('/home/order/')
    
# def cart_view(request):
#     item = request.GET.get('item_name')
#     item_details = Products.objects.filter(name=item)
#     items = cartSerializer(item_details , many=True)
#     item = json.loads(json.dumps(items.data))   
#     item_in_cart = Cart.objects.filter(name=item[0]['name'])
#     if len(item_in_cart)>0:
#         Cart.objects.filter(name=item[0]['name']).update(quantity=F('quantity')+1)
#     else:
#         Cart.objects.create(name=item[0]['name'] , mrp = item[0]['mrp'] , csp = item[0]['csp'] , image = item[0]['image'])
#     # print(item)
#     return HttpResponse("success")


print("uiqyqi")
def cart_page(request):
    result= Cart.objects.all()
    count_item= Cart.objects.all().count()
    cart_subtotal = [item.subtotal for item in Cart.objects.all()] 
    cart_subtotal = sum(cart_subtotal)
    print(cart_subtotal)
    return render(request , 'cart.html' , {'data': result , 'cart_subtotal':cart_subtotal , 'count_item':count_item})

def count_item(request):
    result= Cart.objects.all().count()
    print(result)
    return render(request , 'cart.html' , {'data': result})

def payment(request , *args , **kwargs):
    result= Cart.objects.all()
    cart_subtotal = [item.subtotal for item in Cart.objects.all()] 
    cart_subtotal = sum(cart_subtotal)
    total = cart_subtotal*100
    razor_id = settings.RAZOR_KEY_ID    
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        # import razorpay
        # DATA = {
        #     "amount":cart_subtotal , 
        #     "currency": "INR" , 
        # }
        # print("payment")
        # client = razorpay.Client(auth=("key" , "secret"))
        # payment = client.order.create(data=DATA)
        # print(payment)
        # print("----------" , cart_subtotal)
    return render(request , 'payment.html' , {'total':total , "name":name , "email":email , 'data':result , 'cart_total':cart_subtotal , 'razor_id':razor_id})

@csrf_exempt
def success(request):
    return render(request , 'payment_successful.html')
        
def payment_failed(request):
    return render(request , 'paymentfailure.html')

def customer_form(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        print("in post")
    cart_subtotal = [item.subtotal for item in Cart.objects.all()] 
    cart_subtotal = sum(cart_subtotal)
    return render(request , 'form.html' , {'total':cart_subtotal})

def item_details(request , *args , **kwargs):
    item = Products.objects.filter(id=kwargs.get('pk'))
    print(item)
    return render(request , 'item.html' , {'item':item})

def sending_mail(request):
    print("in")
    subject = 'welcome to wizilla store'
    message = f'Hello , thank you for subscribing to wizilla store.Now , you are a part of our wizilla Family.'
    # email_from = config('EMAIL_HOST_USER')
    email_from  = settings.EMAIL_HOST_USER
    print("-----",email_from)
    if request.method == 'POST':
        print("in post")
        email = request.POST['email']
    recipient_list = [email ]
    send_mail(subject, message, email_from, recipient_list )
    return redirect('/home/')

def search(request):
    result= Cart.objects.all().count()
    if request.method == "POST":
        title = request.POST['item']
    items = Products.objects.filter(Q(name__icontains=title) | Q(category__icontains = title) |Q(sub_category__icontains = title))
    print(len(items))
    if len(items)!=0:
        return render(request , 'products.html', {'data':items , 'count':result})
    else:
        return render(request , 'no_products_found.html' ,{'title':title})

def add_in_cart(request ,  *args , **kwargs):
    print("in add item to cart function")
    id=kwargs.get('pk')
    item = list(Products.objects.filter(id=kwargs.get('pk')).values())
    Products.objects.filter(name=item[0]['name']).update(in_cart = True)
    Cart.objects.create(id= kwargs.get('pk'), name=item[0]['name'] , mrp = item[0]['mrp'] , csp = item[0]['csp'] , image = item[0]['image'])
    path = '/home/item/{}/'.format(id)
    print(path)
    return redirect(path)