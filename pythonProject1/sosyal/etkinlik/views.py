from django.shortcuts import render,  redirect
from .models import Activate
from .forms import EtkinlikForm

def merhaba(request):
    liste =  Activate.objects.all()
    return render(request,'etkinlik/giris.html', {'etkinlikler': liste})

def ekle(request):
    form = EtkinlikForm
    if request.method == 'POST':
        form = EtkinlikForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = EtkinlikForm()

    return render(request,'etkinlik/ekle.html', {'form': form })
def sil(request,id):
    kayit = Activate.objects.get(id=id)
    kayit.delete()
    return redirect('/')


