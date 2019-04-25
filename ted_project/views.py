from django.shortcuts import render


def home_view(request):
    """Establishes a route to the home page."""
    context = {
        'message': 'hello'
    }
    import pdb; pdb.set_trace()

    return render(request, 'generic/home.html', context)
