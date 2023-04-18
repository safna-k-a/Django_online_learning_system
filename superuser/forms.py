from django import forms
from Myapp.models import Course_details,Offer

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course_details
        fields = ['course_name', 'language', 'category', 'price', 'course_image', 'description']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'course_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        
class OfferForm(forms.ModelForm):
    class Meta:
        model =Offer
        fields = ['course_id','offerprice', 'start_date', 'end_date']
        widgets = {
            
            'offerprice': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'start_date': forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'})),
            # 'end_date': forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
            
        }
        