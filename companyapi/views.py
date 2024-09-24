from django.http import JsonResponse

frinds = [
    'naaa',
    'nadeem',
    'rameez'
]

def home_page(request):

    return JsonResponse({"friends": frinds})


