from django.shortcuts import render
from .forms import CustomerForm

def index(request):
    return render(request, 'index.html')


def customers(request):
    form = CustomerForm()
    return render(request, 'customers.html', {'form': form})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})