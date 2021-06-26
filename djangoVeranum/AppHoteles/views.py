from djangoVeranum.AppHoteles.models import ReservaHabitacion
from django.shortcuts import redirect, render
from AppHoteles.models import *
from AppHoteles.forms import HabitacionForm

# Create your views here.
def home (request):
    return render(request,'principal.html')

def reservaHabitacion(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/reservas')
            except:
                pass
    else:
        form = HabitacionForm()
        reservaHabitacion = ReservaHabitacion.objects.all()
        return render(request,'mantenedorReservas.html',{'form': form, 'reservaHabitacion': reservaHabitacion})