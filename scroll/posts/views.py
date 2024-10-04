import time

from django.http import JsonResponse
from django.shortcuts import render

# create your views here/
def index(request):
    return render(request, "posts/index.html")

def posts(request):

    #Get start and end poinst
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    #generate list of post
    data = []
    for i in range(start, end +1):
        data.append(f"Post #{i}")

    #Artificially delay speed of response
    time.sleep(1)

    return JsonResponse({"posts": data})