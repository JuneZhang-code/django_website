from django.shortcuts import render

# Create your views here.
def community(request):
    return render(request,'Community/community.html')

def initiate(request):
    return render(request,'Community/initiate.html')

def invest(request):
    return render(request,'Community/invest.html')
