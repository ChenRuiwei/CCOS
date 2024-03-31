import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from ccos import forms
from ccos.models import *


# Create your views here.


def logout(request):
    request.session.flush()
    return redirect("/login")


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_id = login_form.cleaned_data.get('user_id')
            password = login_form.cleaned_data.get('password')
            try:
                user = Customer.objects.get(customer_id=user_id)
            except:
                message = '用户不存在！'
                return render(request, 'login.html', locals())
            if user.password == password:
                request.session['user_id'] = user_id
                request.session['user_name'] = user.customer_name
                request.session['is_login'] = True
                return redirect('/canteen')
            else:
                message = '密码错误！'
                return render(request, 'login.html', locals())
        else:
            return render(request, 'login.html', locals())
    login_form = forms.LoginForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            user_id = register_form.cleaned_data.get('user_id')
            password = register_form.cleaned_data.get('password')
            user_name = register_form.cleaned_data.get('user_name')
            address = register_form.cleaned_data.get('address')
            contact_name = register_form.cleaned_data.get('contact_name')
            phone_number = register_form.cleaned_data.get('phone_number')
            same_id_user = Customer.objects.filter(customer_id=user_id)
            if same_id_user:
                message = '账号已经存在'
                return render(request, 'register.html', locals())
            new_customer = Customer()
            new_customer.customer_id = user_id
            new_customer.password = password
            new_customer.customer_name = user_name
            new_address = Address(customer_id=user_id, location=address)
            new_contact = Contact(customer_id=user_id, contact_name=contact_name, phone_number=phone_number)
            new_customer.save()
            new_address.save()
            new_contact.save()
            return redirect('/login/')
        else:
            return render(request, 'register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())


def business_register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            user_id = register_form.cleaned_data.get('user_id')
            password = register_form.cleaned_data.get('password')
            user_name = register_form.cleaned_data.get('user_name')
            same_id_user = Business.objects.filter(business_id=user_id)
            if same_id_user:
                message = '账号已经存在'
                return render(request, 'business/register.html', locals())
            new_customer = Customer()
            new_customer.customer_id = user_id
            new_customer.password = password
            new_customer.customer_name = user_name
            new_customer.save()
            return redirect('/business/login/')
        else:
            return render(request, 'business/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'business/register.html', locals())


def business_login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_id = login_form.cleaned_data.get('user_id')
            password = login_form.cleaned_data.get('password')
            try:
                user = Business.objects.get(business_id=user_id)
            except:
                message = '用户不存在！'
                return render(request, 'business/login.html', locals())
            if user.password == password:
                request.session['user_id'] = user_id
                request.session['user_name'] = user.business_id
                request.session['is_login'] = True
                return redirect(f'/business/{user_id}/order')
            else:
                message = '密码错误！'
                return render(request, 'business/login.html', locals())
        else:
            return render(request, 'business/login.html', locals())
    login_form = forms.LoginForm()
    return render(request, 'business/login.html', locals())


def business_change_dish(request, business_id, dish_id):
    message = ""
    if request.method == "POST":
        dish_name = request.POST.get("dish_name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        photo_url = request.POST.get("photo_url")
        dish = Dish.objects.get(dish_id=dish_id)
        new_dish = Dish(dish_id=dish_id, dish_name=dish_name, price=price, description=description, photo_url=photo_url,
                        restaurant_id=dish.restaurant_id, category=dish.category)
        new_dish.save()
        message = "已保存成功"
    context = {
        "dish": Dish.objects.get(dish_id=dish_id),
        "business_id": business_id,
        "message": message
    }
    return render(request, "business/dish_change.html", context=context)


def business_add_dish(request, business_id):
    message = ""
    if request.method == "POST":
        dish_name = request.POST.get("dish_name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        photo_url = request.POST.get("photo_url")
        restaurant_id = Restaurant.objects.get(business_id=business_id).restaurant_id
        category_id = Category.objects.first().category_id
        new_dish = Dish(dish_name=dish_name, price=price, description=description, photo_url=photo_url,
                        restaurant_id=restaurant_id, category_id=category_id)
        new_dish.save()
        message = "已保存成功"
    context = {
        "business_id": business_id,
        "message": message
    }
    return render(request, "business/dish_add.html", context=context)


def business_delete_dish(request, business_id, dish_id):
    Dish.objects.get(dish_id=dish_id).delete()
    return redirect(f"/business/{business_id}/dish")


def business_show_orders(request, business_id):
    indent_list = []
    for indent in Indent.objects.all():
        indent_dish = IndentDish.objects.get(indent_id=indent.indent_id)
        dish = Dish.objects.get(dish_id=indent_dish.dish_id)
        restaurant = Restaurant.objects.get(restaurant_id=dish.restaurant_id)
        if restaurant.business_id == business_id:
            indent_list.append(indent)
    order_list = []
    for indent in indent_list:
        dish_list = []
        for indent_dish in IndentDish.objects.filter(indent_id=indent.indent_id):
            dish = Dish.objects.get(dish_id=indent_dish.dish_id)
            dish_dict = {"dish": dish, "dish_number": indent_dish.dish_number}
            dish_list.append(dish_dict)
        order_list.append((indent, dish_list))
    context = {'order_list': order_list, "business": Business.objects.get(business_id=business_id)}
    return render(request, 'business/orders.html', context)


def business_show_dishes(request, business_id):
    dish_list = []
    for dish in Dish.objects.all():
        restaurant = Restaurant.objects.get(restaurant_id=dish.restaurant_id)
        if restaurant.business_id == business_id:
            dish_list.append(dish)
    context = {'dish_list': dish_list,
               'address_list': Address.objects.filter(customer_id=request.session.get('user_id')),
               'contact_list': Contact.objects.filter(customer_id=request.session.get('user_id'))}
    return render(request, "business/dish.html", context)


def business_list_dishes(request, business_id):
    restaurant_id = Restaurant.objects.get(business_id=business_id).restaurant_id
    context = {'dish_list': Dish.objects.filter(restaurant_id=restaurant_id),
               'address_list': Address.objects.filter(customer_id=request.session.get('user_id')),
               'contact_list': Contact.objects.filter(customer_id=request.session.get('user_id'))}
    return render(request, "business/dish_list.html", context)


def change_order_state(request, business_id, indent_id):
    indent = Indent.objects.get(indent_id=indent_id)
    indent.state = 1
    indent.save()
    return redirect(f"/business/{request.session.get('user_id')}/order")


def business(request):
    return redirect("/business/login")


def show_canteens(request):
    context = {'canteen_list': Canteen.objects.all()}
    return render(request, "canteen.html", context)


def show_restaurants(request, canteen_id):
    context = {'restaurant_list': Restaurant.objects.filter(canteen_id=canteen_id)}
    return render(request, "restaurant.html", context)


def show_dishes(request, restaurant_id):
    context = {'dish_list': Dish.objects.filter(restaurant_id=restaurant_id),
               'address_list': Address.objects.filter(customer_id=request.session.get('user_id')),
               'contact_list': Contact.objects.filter(customer_id=request.session.get('user_id'))}
    return render(request, "dish.html", context)


def order(request):
    if request.method == 'POST':
        new_indent = Indent(customer_id=request.session.get("user_id"),
                            address_id=request.POST.get("address_id"),
                            contact_id=request.POST.get("contact_id"),
                            order_time=datetime.datetime.now(),
                            state=0,
                            order_notes=request.POST.get("order_notes"))
        new_indent.save()
        restaurant_id = 0
        for dish in Dish.objects.all():
            dish_id_str = str(dish.dish_id)
            if dish_id_str in request.POST:
                if int(request.POST.get(dish_id_str)) == 0:
                    continue
                new_indent_dish = IndentDish(indent_id=new_indent.indent_id, dish_id=dish.dish_id,
                                             dish_number=request.POST.get(dish_id_str))
                new_indent_dish.save()
                restaurant_id = Dish.objects.get(dish_id=new_indent_dish.dish_id).restaurant_id
        context = {'dish_list': Dish.objects.filter(restaurant_id=restaurant_id),
                   'address_list': Address.objects.filter(customer_id=request.session.get('user_id')),
                   'contact_list': Contact.objects.filter(customer_id=request.session.get('user_id')),
                   'message': f'下单成功！单号为{new_indent.indent_id}'}
        return render(request, 'dish.html', context)
    return render(request, 'dish.html', locals())


def show_orders(request):
    indent_list = Indent.objects.filter(customer_id=request.session.get('user_id'))
    order_list = []
    for indent in indent_list:
        dish_list = []
        for indent_dish in IndentDish.objects.filter(indent_id=indent.indent_id):
            dish = Dish.objects.get(dish_id=indent_dish.dish_id)
            dish_dict = {"dish": dish, "dish_number": indent_dish.dish_number}
            dish_list.append(dish_dict)
        order_list.append((indent, dish_list))
    context = {'order_list': order_list}
    print(context)
    return render(request, "orders.html", context)


def personal(request):
    if "is_login" in request.session and request.session["is_login"]:
        return render(request, "personal.html")
    else:
        return redirect("/login")


def index(request):
    return redirect("/canteen")


def tt(request):
    return render(request, "tt.html")


def test(request):
    newAdministrator = Administrator("admin", "123456", "18271910086")
    newAdministrator.save()

    canteen1 = Canteen(administrator=newAdministrator,
                       canteen_name="一食堂",
                       location="荔园四栋楼下",
                       photo_url="https://www.google.com/url?sa=i&url=https%3A%2F%2F699pic.com%2Ftupian%2Fshitang.html"
                                 "&psig=AOvVaw1myhr6g2ionRNV1C9Atbxs&ust=1698765961904000&source=images&cd=vfe&opi"
                                 "=89978449&ved=0CBEQjRxqFwoTCOjgoL-KnoIDFQAAAAAdAAAAABAE")

    canteen2 = Canteen(administrator=newAdministrator,
                       canteen_name="二食堂",
                       location="荔园二栋对面",
                       photo_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg95.699pic.com%2Fphoto%2F50077"
                                 "%2F0213.jpg_wh300.jpg&tbnid=MZ0gpjOp6rHJIM&vet=12ahUKEwiLwP"
                                 "--ip6CAxWf6DgGHWBZBFEQMygFegQIARBU..i&imgrefurl=https%3A%2F%2F699pic.com%2Ftupian"
                                 "%2Fshitang.html&docid=4ILuij1TPnAMKM&w=450&h=300&q=%E9%A3%9F%E5%A0%82%E5%9B%BE%E7%89%87"
                                 "&ved=2ahUKEwiLwP--ip6CAxWf6DgGHWBZBFEQMygFegQIARBU")

    canteen3 = Canteen(administrator=newAdministrator,
                       canteen_name="三食堂",
                       location="荔园七栋楼下",
                       photo_url="https://www.google.com/url?sa=i&url=https%3A%2F%2F699pic.com%2Ftupian%2Fshitang.html"
                                 "&psig=AOvVaw1myhr6g2ionRNV1C9Atbxs&ust=1698765961904000&source=images&cd=vfe&opi"
                                 "=89978449&ved=0CBEQjRxqFwoTCOjgoL-KnoIDFQAAAAAdAAAAABAE")

    canteen4 = Canteen(administrator=newAdministrator,
                       canteen_name="四食堂",
                       location="荔园十栋对面",
                       photo_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg95.699pic.com%2Fphoto%2F50077"
                                 "%2F0213.jpg_wh300.jpg&tbnid=MZ0gpjOp6rHJIM&vet=12ahUKEwiLwP"
                                 "--ip6CAxWf6DgGHWBZBFEQMygFegQIARBU..i&imgrefurl=https%3A%2F%2F699pic.com%2Ftupian"
                                 "%2Fshitang.html&docid=4ILuij1TPnAMKM&w=450&h=300&q=%E9%A3%9F%E5%A0%82%E5%9B%BE%E7%89%87"
                                 "&ved=2ahUKEwiLwP--ip6CAxWf6DgGHWBZBFEQMygFegQIARBU")

    canteen1.save()
    canteen2.save()
    canteen3.save()
    canteen4.save()
    return HttpResponse("good")
