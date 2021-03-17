from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'visitcount' in request.session:
        request.session['visitcount'] += 1
    else: 
        request.session['visitcount'] = 1
    return render(request, "index.html")

def cheat(request):
    print('Got post info^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print(request.POST)
    if 'visitcount' in request.session:
        request.session['visitcount'] += int(request.POST['number'])
    return redirect("/")

def duex(request):
    if 'visitcount' in request.session:
        request.session['visitcount'] += 1
    else:
        request.session['visitcount'] = 1
    return redirect("/")

def resetinfo(request):
    del request.session['visitcount']
    return redirect('/')