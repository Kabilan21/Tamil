from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import urllib.request
from .scrapper import text_from_html
from .models import Literature


def html_view(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        literature = Literature.objects.filter(url=url).first()
        if literature:
            return JsonResponse({"html": literature.data})
        else:
            html = urllib.request.urlopen(url).read()
            html = text_from_html(html)
            literature = Literature(url=url, data=html)
            literature.save()
            return JsonResponse({"html": html})
    return render(request, 'home/index.html')
