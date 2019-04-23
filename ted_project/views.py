from django.shortcuts import render


def home_view(request):

    context = {
        'message': 'hello'
    }
    return render(request, 'generic/home.html', context)
