from django.shortcuts import render
from myapp.models import Product
from django.http import HttpResponse

# Create your views here.

def webpage(request, *args):
    result = []
    if request.method == "POST":
	result = []
        data = request.POST.get('data', '')
        for objects in Product.objects.all():
            if data.lower() in Product.get_text(objects).lower():
                help=Product.get_helpfulness(objects)
                good_rating=int(help.split("/")[0])
                bad_rating=int(help.split("/")[1])-good_rating
                result.append([Product.get_score(objects), good_rating, bad_rating, Product.get_text(objects)])
        if not result == []:
            result.sort(key=lambda x: (-x[0], -x[1], x[2]))
            output = result[0][3]
        else:
            output = ""
        message = {
            'review_text': output,
        }
        return render(request, "webpage.html", message)

    return render(request, "webpage.html")
