from django.shortcuts import render
from django.http import HttpResponse

def default_view(request):
    return HttpResponse("<h1>This is a site to calculate tax.</h1>")

def calculate_tax(request, any_number):
    tax_rate = 0.15
    total_with_tax = float(any_number) * (1 + tax_rate)
    return HttpResponse(f"<h1>Total with 15% tax: ${total_with_tax}</h1>")

def display_tax_rate(request):
    tax_rate = 0.15
    return render(request, 'tax_calculator_app/taxrate.html', {'tax_rate': tax_rate})
