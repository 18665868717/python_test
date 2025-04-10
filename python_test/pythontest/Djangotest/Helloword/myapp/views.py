from django.shortcuts import render,HttpResponse,get_object_or_404

# Create your views here.


# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")

def shei(request):
    return HttpResponse('你谁啊')


def test_html(request):
    from django.shortcuts import render
    return render(request,'test_html.html')