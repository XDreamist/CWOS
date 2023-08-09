from django import forms

from chipworld.models import Cameras

class addproductForm(forms.ModelForm):
    class Meta:
        model = Cameras
        fields = "__all__"