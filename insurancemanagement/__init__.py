from django.http import HttpResponse

def coursedetail (request) :
    with open('static/c.html') as f:
        contents = f.read()
    return HttpResponse(contents)

def cp (request) :
    with open('static/cp.html') as f:
        contents = f.read()
    return HttpResponse(contents)

def gr (request) :
    with open('static/gr.html') as f:
         contents = f.read()
    return HttpResponse(contents)
