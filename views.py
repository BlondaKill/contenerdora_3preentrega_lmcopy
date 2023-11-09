from django.shortcuts import render
from django.shortcuts import redirect

from .models import *
from .forms import *

# views:


def listar_main_agency(request):
    contexto = {
        'main_Model_girl': Model_girl.objects.all(),
        'main_Brand': Brand.objects.all(),
        'main_Client': Client.objects.all(),

    }

    http_response = render(
        request=request,
        template_name='agency/main_agency.html',
        context=contexto,
    )
    return http_response


def create_static(request):
    object1 = Model_girl(name="Lisa", last_name="Taylor",
                         height=1.80, age=21, birthdate="2002-05-10")
    object2 = Brand(name="Speed", city=" Boston ", address="235 Jefferson Ave")
    object3 = Client(name="Jack", last_name="Fox", email="jack_fox@gmail.com")
    object1.save()
    object2.save()
    object3.save()

    return render(request=request,
                  template_name='agency/main_agency.html',
                  )


def create_model_girl(request):
    if request.method == 'POST':
        form = ModelGirlForm(request.POST)
        if form.is_valid():
            model_girl = Model_girl(
                name=form.cleaned_data['name'],
                last_name=form.cleaned_data['last_name'],
                height=form.cleaned_data['height'],
                age=form.cleaned_data['age'],
                birthdate=form.cleaned_data['birthdate']
            )
            model_girl.save()
            return redirect('list_model_girl')
    else:
        form = ModelGirlForm()
    return render(request, 'agency/modelgirl_form.html', {'form': form})


def list_model_girl(request):
    girls = Model_girl.objects.all()
    return render(request, 'agency/modelgirl_list.html', {'girls': girls})


def search_model_girl(request):
    form = SearchModelGirlForm(request.GET)
    results = Model_girl.objects.all()

    if form.is_valid():
        height = form.cleaned_data.get('height')

        if height is not None:
            results = results.filter(height=height)

    return render(request, 'agency/modelgirl_search.html', {'form': form, 'results': results})


def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = Brand(
                name=form.cleaned_data['name'],
                city=form.cleaned_data['city'],
                address=form.cleaned_data['address'],
            )
            brand.save()
            return redirect('list_brand')
    else:
        form = BrandForm()
    return render(request, 'agency/brand_form.html', {'form': form})


def list_brand(request):
    brand = Brand.objects.all()
    return render(request, 'agency/brand_list.html', {'brand': brand})


def search_brand(request):
    form = SearchBrandForm(request.GET)
    results = Brand.objects.all()

    if form.is_valid():
        city = form.cleaned_data.get('city')

        if city is not None:
            results = results.filter(city=city)

    return render(request, 'agency/brand_search.html', {'form': form, 'results': results})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = Client(
                name=form.cleaned_data['name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],

            )
            client.save()
            return redirect('list_client')
    else:
        form = ClientForm()
    return render(request, 'agency/client_form.html', {'form': form})


def list_client(request):
    client = Client.objects.all()
    return render(request, 'agency/client_list.html', {'client': client})


def search_client(request):
    form = SearchClientForm(request.GET)
    results = Client.objects.all()

    if form.is_valid():
        email = form.cleaned_data.get('email')

        if email is not None:
            results = results.filter(email=email)

    return render(request, 'agency/client_search.html', {'form': form, 'results': results})
