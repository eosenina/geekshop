from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from authapp.models import User
from mainapp.models import ProductCategory, Product
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoriesAdminForm, ProductAdminForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    selected_user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    content = {'form': form, 'selected_user': selected_user}
    return render(request, 'adminapp/admin-users-update-delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_read(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoriesAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories_read'))
    else:
        form = CategoriesAdminForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, category_id):
    selected_category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoriesAdminForm(data=request.POST, instance=selected_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories_read'))
    else:
        form = CategoriesAdminForm(instance=selected_category)
    content = {'form': form, 'selected_category': selected_category}
    return render(request, 'adminapp/admin-categories-update-delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_remove(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_categories_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products_read(request):
    context = {'products': Product.objects.all()}
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products_read'))
    else:
        form = ProductAdminForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, product_id):
    selected_product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST, files=request.FILES, instance=selected_product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products_read'))
    else:
        form = ProductAdminForm(instance=selected_product)
    content = {'form': form, 'selected_product': selected_product}
    return render(request, 'adminapp/admin-products-update-delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_remove(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_products_read'))