from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Task


# membuat class TaskForm untuk membuat task
class TaskForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Task
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('nama', 'keluarga', 'status')
        # mengatur teks label untuk setiap field
        labels = {
            'nama': _('Nama'),
            'keluarga': _('Keluarga'),
            'status': _('Status')
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'nama': {
                'required': _("Nama harus diisi."),
            },
            'keluarga': {
                'required': _("Keluarga harus diisi."),
            },
        }