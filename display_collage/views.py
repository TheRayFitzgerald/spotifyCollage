from django.shortcuts import render

# Create your views here.
def index(request):
    print('getting code')
    code = request.GET.get('code')
    print(code)
    return render(request, 'display_collage/index.html')