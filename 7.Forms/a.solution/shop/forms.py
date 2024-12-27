from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    
    gender = forms.ChoiceField(choices = GENDERS)
    full_name = forms.CharField(max_length = 60, min_length = 5)
    height = forms.IntegerField(max_value = 250, min_value = 70)
    age = forms.IntegerField(max_value = 99, min_value = 14)

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if full_name.istitle() == False:
            raise forms.ValidationError('Error')
        return full_name
