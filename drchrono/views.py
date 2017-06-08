from django.http import HttpResponse

def dummy(request):
    html = '<html><body>This is a little dummy page.</body></html>'
    return HttpResponse(html)