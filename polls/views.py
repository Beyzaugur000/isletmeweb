from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Categories, Customers, Employees, Orders, Products, Suppliers, Territories


def index(request):
    return render(request, 'polls/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Kullanıcı adını al
        password = request.POST.get('password')  # Şifreyi al
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Kullanıcıyı giriş yap
            return redirect('index2')  # 'index2' olarak adlandırılmış bir sayfaya yönlendir
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')
            return redirect('login')  # Giriş sayfasına geri döner
    return render(request, 'polls/login.html')  # Giriş formunu göster


class BaseView(generic.TemplateView):
    template_name = 'polls/base.html'


from django.shortcuts import render

def index2(request):
    # Dinamik veriler
    orders = 150  # Yeni sipariş sayısı
    bounce_rate = 53  # Bounce oranı (%)
    monthly_sales = [5000, 6000, 7000, 8000, 7500]  # Aylık satış verileri
    months = ['January', 'February', 'March', 'April', 'May']  # Ay isimleri

    # Bu verileri template'e gönderiyoruz
    context = {
        'orders': orders,
        'bounce_rate': bounce_rate,
        'monthly_sales': monthly_sales,
        'months': months,
    }

    return render(request, 'polls/index2.html', context)



@login_required
def dashboard_view(request):
    # Veritabanından bilgileri çekiyoruz
    categories_count = Categories.objects.count()
    customers_count = Customers.objects.count()
    employees_count = Employees.objects.count()
    orders_count = Orders.objects.count()
    products_count = Products.objects.count()
    suppliers_count = Suppliers.objects.count()
    territories_count = Territories.objects.count()

    # Son 10 siparişi al
    recent_orders = Orders.objects.all().order_by('-order_date')[:10]

    context = {
        'categories_count': categories_count,
        'customers_count': customers_count,
        'employees_count': employees_count,
        'orders_count': orders_count,
        'products_count': products_count,
        'suppliers_count': suppliers_count,
        'territories_count': territories_count,
        'recent_orders': recent_orders,
    }
    return render(request, 'polls/dashboard.html', context)
