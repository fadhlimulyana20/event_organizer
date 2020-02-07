from django import forms

from .models import Event, Location, EventParticipant, EventPayment

class UpdateTranferReceipt(forms.ModelForm):
    image_receipt = forms.ImageField(widget=forms.FileInput)

    image_receipt.widget.attrs['class'] = 'form-control-file'
    image_receipt.widget.attrs['id'] = 'image_receipt'

    class Meta:
        model = EventPayment
        fields = ['image_receipt',]
