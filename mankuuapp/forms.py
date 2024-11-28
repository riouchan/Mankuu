from django import forms
from .models import ManqooRelations

FLAG_CHOICHES = [
    ('', '---------'),  # Empty option as the default choice (null)
    (1, '有効'),  # '1' means 'Active' (有効)
    (0, '無効'),  # '0' means 'Inactive' (無効)
]


class ManqooRelationsForm(forms.ModelForm):

    class Meta:
        model = ManqooRelations
        # Use '__all__' to include all fields; you can also specify fields individually
        fields = '__all__'
        widgets = {
            'customer_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer code',
                'maxlength': '10'
            }),
            'parking_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter parking name'
            }),
            'database': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter database name'
            }),
            'start_rack': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter start rack'
            }),
            'end_rack': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter end rack'
            }),
            'machine_id': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter machine ID'
            }),
            'area_code': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter area code'
            }),
            'available_flag': forms.Select(choices=FLAG_CHOICHES, attrs={
                'class': 'form-control'
            }),
            'empty_threshold': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter empty threshold'
            }),
            'busy_threshold': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter busy threshold'
            }),
            'vehicle_type': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter vehicle type'
            }),
            'full_car_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full car count'
            }),
            'created': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select created date',
                'type': 'datetime-local'
            }),
            'modified': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select modified date',
                'type': 'datetime-local'
            }),
            'machine_type': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter machine type'
            }),
        }
