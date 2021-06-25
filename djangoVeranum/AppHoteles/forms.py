from django import forms
from AppHoteles.models import Hotel, ReservaHabitacion, ReservaSalon

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = ReservaHabitacion
        fields = "__all__"