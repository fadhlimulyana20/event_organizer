from django import forms

from .models import Invoice

class UpdateTranferReceipt(forms.ModelForm):
    image_receipt = forms.ImageField(widget=forms.FileInput)

    image_receipt.widget.attrs['class'] = 'form-control-file'
    image_receipt.widget.attrs['id'] = 'image_receipt'

    class Meta:
        model = Invoice
        fields = ['image_receipt',]
