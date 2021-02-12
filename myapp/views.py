from django.shortcuts import render
from myapp.models import Product
from django.http import HttpResponse

# Create your views here.

def webpage(request, *args):
    result = []
    if request.method == "POST":
        data = request.POST.get('data', '')
        for objects in Product.objects.all():
            if data.lower() in Product.get_text(objects).lower():
                result.append([Product.get_score(objects), Product.get_helpfulness(objects), Product.get_text(objects)])
        if not result == []:
            result.sort(key=lambda x: x[0],reverse=True)
            output = result[0][2]
        else:
            output = ""
        message = {
            'review_text': output,
        }
        return render(request, "webpage.html", message)

    return render(request, "webpage.html")
