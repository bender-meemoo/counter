from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'visitcount' in request.session:
        request.session['visitcount'] += 1
    else:
        request.session['visitcount'] = 1
    return render(request, "index.html")

def resetinfo(request):
    del request.session['visitcount']
    return redirect('/')