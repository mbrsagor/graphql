from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .form import Contact_Forms, AddNewProduct, Slider_Form, CategoryForm, AddingColor_Form, AddingBrand_Form


# Create your views here.
def homepage(request):

    product_search = Product.objects.all()
    slider_obj = Slider.objects.all()
    latest_product = Product.objects.filter(category__id = 2).order_by('-id')[:6]
    best_seller = Product.objects.filter(category__id = 3).order_by('-id')[:5]
    featured = Product.objects.filter(category__id = 4).order_by('-id')[:9]
    best_seller_galllery = Product.objects.filter(category__id = 3).order_by('-id')[:9]
    special = Product.objects.filter(category__id = 5).order_by('-id')[:9]
    cat_menu = Category.objects.all()

    # Search  Query
    search_query = request.GET.get('search_q')
    if search_query:
        product_search = product_search.filter(name__icontains = search_query)


    context = {
        'slider_obj' : slider_obj,
        'latest_product' : latest_product,
        'best_seller' : best_seller,
        'featured' : featured,
        'best_seller_galllery' : best_seller_galllery,
        'special' : special,
        'cat_menu' : cat_menu,
    }
    return render(request, 'design/index.html', context)



# Sinlge page views
class Single_page_views(View):

    def get(self, request, id):

        single_page = get_object_or_404(Product, id = id)
        related_porduct = Product.objects.filter(category = single_page.category).exclude(id = id)[:4]
        context = {
            'single_product' : single_page,
            'related_porduct' : related_porduct
        }
        return render(request, 'design/shop-single-product-v1.html', context)



# Category Product
class Category_View(View):

    def get(self, request, name):

        category_product = Product.objects.filter(category__name = name)
        category_by_item = Category.objects.all()
        title_category = get_object_or_404(Category, name = name)
        brand_name = Brand.objects.all()

        search_query = request.GET.get('search_q')
        if search_query:
            product_obj = Product.filter(name__icontains = search_query)

        context = {
            'cat' : category_product,
            'cat_widget_item' : category_by_item,
            'brand_name' : brand_name,
            'title_category' : title_category
        }
        return render(request, 'design/shop-sidebar-left.html', context)



# Shop Products
class Shop_Project_Views(View):

    def get(self, request):
        all_products = Product.objects.all()
        search_query = request.GET.get('search_q')
        if search_query:
            all_products = all_products.filter(name__icontains = search_query)
        context = {
            'all_products' : all_products
        }
        template_name = 'design/shop.html'
        return render(request, template_name, context)




# Contact views
def Contact_Us_Views(request):

    if request.method == 'GET':
        form = Contact_Forms()
    else:
        form = Contact_Forms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(name, message+"From: "+email, message, ['mbrsagor@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Message Send Failed')
            return redirect(Contact_Us_Views)
    context = {
        'form' : form,
    }

    template_name = 'design/contact.html'
    return render(request, template_name, context)



# About Us
class About_us_Views(View):

    def get(self, request):
        template_name = 'design/about.html'
        return render(request,template_name)



# User login views
def login_views(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username = username, password = password)
        if auth is not None:
            login(request, auth)
            return redirect(dashboard_views)
    template_name = 'admin/login.html'
    return render(request,template_name)




# User lgout views
def logout_views(request):

    logout(request)
    return redirect(login_views)



# Dashboard views
def dashboard_views(request):

    if request.user.is_authenticated:
        count_product = Product.objects.count()
        count_category = Category.objects.count()
        latest_product = Product.objects.all().order_by('-id')[:12]
        context = {
            'count_product' : count_product,
            'count_category' : count_category,
            'latest_product' : latest_product,
        }
        template_name = 'admin/dashboard.html'
        return render(request, template_name, context)
    else:
        return redirect(login_views)
    return render(request, 'app/bashboard.html', context)


# Show Product admin panel
class Products_View(View):

    def get(self, request):
        products = Product.objects.all()[:8]
        context = {
            'products' : products
        }
        template_name = 'admin/products.html'
        return render(request, template_name, context)



# Add New Product
def add_prodct_views(request):

    if request.user.is_authenticated:
        form = AddNewProduct()
        if request.method == 'POST':
            form = AddNewProduct(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect(add_prodct_views)
        context = {
            'form' : form
        }
        template_name = 'admin/add-product.html'
        return render(request, template_name, context)

    else:
        return redirect(login_views)



# Add New Slider
def slider_views(request):

    if request.user.is_authenticated:
        slider_obj = Slider.objects.all().order_by('-id')
        form = Slider_Form()
        if request.method == 'POST':
            form = Slider_Form(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect(slider_views)
        context = {
            'form' : form,
            'slider_obj' : slider_obj
        }
        template_name = 'admin/slider.html'
        return render(request, template_name, context)
    else:
        return redirect(login_views)



# Add New Category
def category_views(request):

    if request.user.is_authenticated:
        category_obj = Category.objects.all()
        form = CategoryForm()
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect(category_views)
        context = {
            'form' : form,
            'category_obj' : category_obj
        }
        template_name = 'admin/category.html'
        return render(request, template_name, context)
    return redirect(login_views)



# Edit Product
def edit_product_views(request, id):

    if request.user.is_authenticated:
        edit_obj = get_object_or_404(Product, id = id)
        form = AddNewProduct(request.POST or None, request.FILES, instance = edit_obj)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            return redirect(add_prodct_views)
        context = {
            'form' : form
        }
        template_name = 'admin/edit-product.html'
        return render(request, template_name, context)
    else:
        return redirect(login_views)




# List of Products
def listOf_product_viwes(request):

    if request.user.is_authenticated:
        product_obj = Product.objects.all().order_by('-publish_on')
        context = {
            'product_obj' : product_obj
        }
        template_name = 'admin/delete-product.html'
        return render(request, template_name, context)
    else:
        return redirect(login_views)



# Add New Color
def add_Color_Views(request):

    if request.user.is_authenticated:
        color_obj = Color.objects.all()
        form = AddingColor_Form()
        if request.method == 'POST':
            form = AddingColor_Form(request.POST)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect(add_Color_Views)
        context = {
            'form' : form,
            'color_obj' : color_obj,
        }
        template_name = 'admin/addcolor.html'
        return render(request, template_name, context)
    return redirect(login_views)




# Add New Brand
def adding_brand_views(request):

    if request.user.is_authenticated:
        brand_obj = Brand.objects.all()
        form = AddingBrand_Form()
        if request.method == 'POST':
            form = AddingBrand_Form(request.POST)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect(adding_brand_views)
        context = {
            'form' : form,
            'brand_obj' : brand_obj
        }
        template_name = 'admin/brand.html'
        return render(request, template_name, context)
    else:
        return redirect(login_views)



# Delete Products
def delete_product_viwes(request, id):

    if request.user.is_authenticated:
        delete_obj = get_object_or_404(Product, id = id)
        delete_obj.delete()
        return redirect(listOf_product_viwes)
    return redirect(login_views)




# Delete Category
def deleteCateogry_Views(request, id):

    if request.user.is_authenticated:
        delete_obj = get_object_or_404(Category, id = id)
        delete_obj.delete()
        return redirect(category_views)
    else:
        return redirect(login_views)




# Delete Slider
def deleteSlider_views(request, id):

    if request.user.is_authenticated:
        delete_slider_obj = get_object_or_404(Slider, id = id)
        delete_slider_obj.delete()
        return redirect(slider_views)
    else:
        return redirect(login_views)



# Delete Color
def deleteColor_views(request, id):

    if request.user.is_authenticated:
        delete_color_obj = get_object_or_404(Color, id = id)
        delete_color_obj.delete()
        return redirect(dashboard_views)
    else:
        return redirect(login_views)




# Delete Brand
def deleteBrand_views(request, id):
    
    if request.user.is_authenticated:
        delete_brand = get_object_or_404(Brand, id = id)
        delete_brand.delete()
        return redirect(dashboard_views)
    else:
        return redirect(login_views)



# Update Cateogry
def update_caategroy(request, name):

    if request.user.is_authenticated:
        update_cat_obj = get_object_or_404(Category, name=name)
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            return redirect(add_prodct_views)
        else:
          form = CategoryForm()  
    
        context = {
            'form' : form
        }
        template_name = 'admin/category.html'
        return render(request, template_name, context)

    else:
        return redirect(login_views)
        