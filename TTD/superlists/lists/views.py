from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    #直接模拟http结果，并返回
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request,'home.html')