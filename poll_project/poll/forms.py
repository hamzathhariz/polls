from django.forms import ModelForm, fields

from .models import poll

class CreatePollForm(ModelForm):
    class Meta:
        model =poll
        fields=['question', 'option_one','option_two','option_three']
        