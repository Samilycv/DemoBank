from django.shortcuts import render, redirect
# from .forms import home, ApplicationForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login as auth_login,logout

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print (username)
        print (password)
        check = authenticate(request, username=username, password=password)
        print (check)
        if check:
            auth_login(request,check)
            return redirect(dashboard)
    return render(request, 'login.html')
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return render(request, 'login.html')

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def branches(request):
    return render(request, 'branches.html')

def application(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data['district'])
            account = Account.objects.create(name=form_data['name'],dob=form_data['dob'],age=form_data['age'],
                                             gender=form_data['gender'],phone_number=form_data['phone_number'],
                                             email=form_data['email'],address=form_data['address'],
                                             account_type=form_data['account_type'])
            account.materials_provide.set(form_data['materials_provide'])
            account.district = District.objects.get(name=form_data['district'])
            account.branch = City.objects.get(name=form_data['branch'])
            account.save()
            message = "Application accepted"
            context = {'message': message}
            return render(request, 'success.html', context)
    context = {'form': form}
    return render(request, 'application.html',context)

def get_branches(request):
    district = request.GET.get('district')
    cities = City.objects.filter(district=district).order_by('name')
    # if district == "Ernakulam":
    #     branches = ['Aluva', 'Edapally']
    # elif district == "Kottayam":
    #     branches = ['Pala', 'Changanacherry']
    # elif district == "Thrissur":
    #     branches = ['Chalakudy', 'Guruvayoor']
    # elif district == "Kollam":
    #     branches = ['Kottarakkara', 'Karunagappally']
    # elif district == "Trivandrum":
    #     branches = ['Neyyattinkara', 'Attingal']
    # else:
    #     branches = []
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
