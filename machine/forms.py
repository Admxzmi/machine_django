from django import forms
from .models import Report, Standard, MeasurementPoint

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"
        
class StandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = "__all__"
        
class MeasurementPointForm(forms.ModelForm):
    class Meta:
        model = MeasurementPoint
        fields = "__all__"
        