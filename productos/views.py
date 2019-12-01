from django.shortcuts import render

def post_list(request):
    return render(request, 'productos/post_list.html', {})
