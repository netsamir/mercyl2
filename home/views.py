from django.shortcuts import render

# Create your views here.
def main(request):
    title = "Welcome %s" % request.readlines()
    context = {
        "template_title": title,
    }
    return render(request, "home.html", context)

def price(request):
    title = "Calculate the price"
    context = {
        "template_title": title,
    }
    return render(request, "home.html", context)
