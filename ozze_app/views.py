from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import UserCreationForm, HumanForm
from .models import Human, CoatModel, DressModel, ParkaModel, FaceMaskModel, CartModel
from django.core.mail import send_mail


# Create your views here.


def start(request):
    # request.session.save()
    # request.session.clear_expired()
    # request.session.set_expiry(None)
    if not request.session.session_key:
        request.session.save()
    context = {}
    return render(request, 'main.html', context)


def size_chart(request):
    context = {}
    return render(request, 'size_chart.html', context)


def coat_detail(request, pk):
    product = get_object_or_404(CoatModel, pk=pk)
    return render(request, 'product_coat.html', {'product': product})


def dress_detail(request, pk):
    product = get_object_or_404(DressModel, pk=pk)
    return render(request, 'product_dress.html', {'product': product})


def parka_detail(request, pk):
    product = get_object_or_404(ParkaModel, pk=pk)
    return render(request, 'product_parka.html', {'product': product})


def face_mask_detail(request, pk):
    product = get_object_or_404(FaceMaskModel, pk=pk)
    return render(request, 'product_face_mask.html', {'product': product})


def cart_view(request):
    #return HttpResponse(request.user.is_authenticated)
    #return HttpResponse(request.session.session_key)
    cart = CartModel.objects.filter(session_key=request.session.session_key)
    coat, dress, parka, face_mask = [], [], [], []
    for i in cart:
        if i.product_type == 'Coat':
            coat.append(CoatModel.objects.get(pk=i.product_id))
        elif i.product_type == 'Dress':
            dress.append(DressModel.objects.get(pk=i.product_id))
        elif i.product_type == 'Parka':
            parka.append(ParkaModel.objects.get(pk=i.product_id))
        elif i.product_type == 'Face_mask':
            face_mask.append(FaceMaskModel.objects.get(pk=i.product_id))
    context = {
        'coats': coat,
        'dresses': dress,
        'parkas': parka,
        'face_masks': face_mask,
    }
    return render(request, 'cart.html', context)


def add_to_cart(request):
    if request.method == 'POST':
        product = request.POST['AddToCart'].split(' ')
        product_id = product[0]
        product_type = product[1]
        if request.user.is_authenticated:
            cart, created = CartModel.objects.update_or_create(
                user=request.user, product_type=product_type, product_id=product_id,
                defaults={'session_key': request.session.session_key}
            )
        else:
            cart, created = CartModel.objects.get_or_create(
                session_key=request.session.session_key, product_type=product_type, product_id=product_id,
                defaults={'user': None}
            )
        try:
            cart.save()
        except IntegrityError:
            pass
        return redirect('/{}/{}/'.format(product_type.lower(), product_id))
    return HttpResponse('Somethings go wrong :(')


def del_from_cart(request):
    if request.method == 'POST':
        product = request.POST['del_from_cart'].split(' ')
        product_id = product[0]
        product_type = product[1]
        if request.user.is_authenticated:
            CartModel.objects.filter(user=request.user, product_type=product_type, product_id=product_id).delete()
        else:
            CartModel.objects.filter(session_key=request.session.session_key, product_type=product_type,
                                     product_id=product_id).delete()
    return redirect('/cart/')


class Account(TemplateView):
    template_name = 'personal_account.html'

    def get(self, request):
        our_user = Human.objects.filter(email=request.user.email)
        ctx = {
            'our_user': our_user
        }
        return render(request, self.template_name, ctx)

    # def post(self, request):
    #     form = HumanForm(request.POST)
    #     if form.is_valid():
    #         # chk = request.POST['hide_data']
    #         form.save()
    #         return redirect('account/')
    #     else:
    #         return HttpResponse(form.errors.as_text())


class ChangeAccData(UpdateView):

    def get(self, request):
        form = HumanForm
        model = Human.objects.filter(email=request.user.email)
        ctx = {
            'form': form,
            'model': model
        }
        return render(request, 'changePersonalData.html', ctx)

    def post(self, request):
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account/')
        else:
            return HttpResponse(form.errors.as_text())


class AllCatalog(TemplateView):
    template_name = 'all_clothes.html'
    products = CoatModel.objects.all()

    def get(self, request):
        ctx = {
            'products': self.products
        }
        return render(request, self.template_name, ctx)


class CoatCatalog(TemplateView):
    template_name = 'coat.html'
    products = CoatModel.objects.all()

    def get(self, request):
        ctx = {
            'products': self.products
        }
        return render(request, self.template_name, ctx)


class DressCatalog(TemplateView):
    template_name = 'dress.html'
    products = DressModel.objects.all()

    def get(self, request):
        ctx = {
            'products': self.products
        }
        return render(request, self.template_name, ctx)


class ParkaCatalog(TemplateView):
    template_name = 'parka.html'
    products = ParkaModel.objects.all()

    def get(self, request):
        ctx = {
            'products': self.products
        }
        return render(request, self.template_name, ctx)


class FaceMaskCatalog(TemplateView):
    template_name = 'face_mask.html'
    products = FaceMaskModel.objects.all()

    def get(self, request):
        ctx = {
            'products': self.products
        }
        return render(request, self.template_name, ctx)


class OnSaleCatalog(TemplateView):
    template_name = 'on_sale.html'
    products = CoatModel.objects.filter(sale__gt=0).order_by('add_date')

    def get(self, request):
        ctx = {
            'products': self.products
        }
        return render(request, self.template_name, ctx)


#
# def random_password_generate():
#     chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#     charsBig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     password_new = random.choice(charsBig)
#     for i in range(8):
#         password_new += random.choice(chars)
#     password_new += str(random.randrange(10))
#     return password_new
#

class RegisterForm(FormView):
    form_class = UserCreationForm
    success_url = '/auth'
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterForm, self).form_invalid(form)


class AuthForm(FormView):
    form_class = AuthenticationForm
    template_name = 'auth.html'
    success_url = '/main'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(AuthForm, self).form_valid(form)

    def form_invalid(self, form):
        msg = 'Пожалуйста, введите правильное имя пользователя и пароль. Учтите что оба поля могут быть чувствительны к регистру.'
        return HttpResponse(form.errors.as_text())


class LogoutForm(FormView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/main')
