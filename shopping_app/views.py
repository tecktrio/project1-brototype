from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from shopping_app.forms import add_banner, company_info, add_product_form
from shopping_app.models import banner, Company_Info, All_products_in_bag, all_products, Customer


def root(request):
    return redirect(home)


def home(request):
    banner1 = banner.objects.get(id=1)
    banner2 = banner.objects.get(id=2)
    banner3 = banner.objects.get(id=3)
    banner4 = banner.objects.get(id=4)
    company_details = Company_Info.objects.get(id=1)
    products = all_products.objects.all()
    if request.method == 'POST':
        login_status = 'guest'
        signin_email = request.POST['signin_email']
        signin_password = request.POST['signin_password']
        customer = Customer.objects.all()
        for each in customer:
            if signin_email in each.customer_email:
                if each.customer_password == signin_password:
                    login_status = each.customer_email
        return render(request, 'index.html',
                      {'banner1': banner1, 'banner2': banner2, 'banner3': banner3, 'banner4': banner4,
                       'company_info': company_details, 'products': products, 'login_status':login_status})

    return render(request, 'index.html',
                  {'banner1': banner1, 'banner2': banner2, 'banner3': banner3, 'banner4': banner4,
                   'company_info': company_details, 'products': products, 'login_status': 'guest'})


def add_company_info(request):
    if request.method == 'POST':
        form = company_info(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = company_info()
    return render(request, 'addCompanyInfo.html', {'form': form})


def add_banners(request):
    if request.method == 'POST':
        form = add_banner(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = add_banner()
    return render(request, 'addBanner.html', {'form': form})


def add_products(request):
    # if request.method == 'POST':
    #     form = add_product_form(request.POST, request.FILES)
    #     # product_name = request.POST['product_name']
    #     # product_description = request.POST['product_description']
    #     # product_mrp = request.POST['product_mrp']
    #     # product_category = request.POST['product_category']
    #     # product_sub_category = request.POST['product_sub_category']
    #     # product_specification_1 = request.POST['product_specification_1']
    #     # product_specification_2 = request.POST['product_specification_2']
    #     # product_gender = request.POST['product_gender']
    #     # product_rating = request.POST['product_rating']
    #     # product_is_trusted = request.POST['product_is_trusted']
    #     # product_review_id = request.POST['product_review_id']
    #     # product_status = request.POST['product_status']
    #     # product = all_products.objects.create(product_name=product_name, product_description=product_description,
    #     #                                       product_mrp=product_mrp,
    #     #                                       product_category=product_category,
    #     #                                       product_sub_category=product_sub_category,
    #     #                                       product_specification_1=product_specification_1,
    #     #                                       product_specification_2=product_specification_2,
    #     #                                       product_gender=product_gender, product_rating=product_rating,
    #     #                                       product_is_trusted=product_is_trusted,
    #     #                                       product_review_id=product_review_id, product_status=product_status)
    #
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('successfully uploaded')
    #     return HttpResponse('added new product successful')
    # form = add_product_form
    # return render(request, 'add_product1.html', {'form': form})

    if request.method == 'POST':
        form = add_product_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')

    form = add_product_form()
    return render(request, 'add_product1.html', {'form': form})


def success():
    return HttpResponse('successfully uploaded')


def user_sign_in(request):
    signin_email = request.POST['signin_email']
    signin_password = request.POST['signin_password']

    coustomer = Customer.objects.all()
    for each in coustomer:
        if signin_email in each.customer_email:
            if each.customer_password == signin_password:
                return redirect(home, 1)
    return HttpResponse('you are a bad ass')


def user_signup(request):
    signup_email = request.POST['signup_email']
    signup_password = request.POST['signup_password']
    signup_phone_number = request.POST['signup_phone_number']
    customer = Customer.objects.create(customer_email=signup_email, customer_password=signup_password,
                                       customer_phone_number=signup_phone_number)
    customer.save()

    return redirect(home)


def category(request):
    return render(request, 'category.html')
