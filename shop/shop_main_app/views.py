from django.shortcuts import render

# Create your views here.
def index(requst):
    return render(requst, 'shop_main_app/index.html')

