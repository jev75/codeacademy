from django import forms

class NumberedRadioSelect(forms.RadioSelect):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        option['label'] = f"{index + 1}. {option['label']}"
        return option

class AnswerForm(forms.Form):
    answer = forms.ChoiceField(
        label='Jūsų pasirinkimas:',
        widget=NumberedRadioSelect
    )

    def __init__(self, *args, answer_choices=None, **kwargs):
        if answer_choices is None:
            answer_choices = []
        super().__init__(*args, **kwargs)
        self.fields['answer'].choices = answer_choices
