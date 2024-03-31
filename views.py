from django.http import HttpResponse

def helloworldfunc(request):
    responseobject = HttpResponse('helloworld')
    return responseobject