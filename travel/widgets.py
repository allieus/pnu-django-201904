from django import forms

class TextCounterInput(forms.TextInput):
    template_name = 'travel/widgets/text_counter.html'
