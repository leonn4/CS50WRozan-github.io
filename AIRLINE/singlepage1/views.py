from django.http import Http404, HttpResponse
from django.shortcuts import render

# View untuk halaman index
def index(request):
    return render(request, "singlepage/index.html")

# Text untuk setiap section
texts = [
    "SINGLE PAGE 1 IS BEING CREATED",
    "SINGLE PAGE 2 IS BEING CREATED",
    "SINGLE PAGE 3 IS BEING CREATED"
]

# View untuk section berdasarkan nomor
def section(request, num):
    if 1 <= num <= len(texts):
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such page is created")
