from django import forms
from pico_column.models import PicoRow, WIDTH_CHOICES
from django.utils.translation import ugettext_lazy as _

class PicoRowForm(forms.ModelForm):
    NUM_COLUMNS = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "11"),
        (12, "12"),
    )


    create = forms.ChoiceField(choices=NUM_COLUMNS, label=_("Create Columns"), help_text=_("Create this number of columns"))
    create_width = forms.ChoiceField(choices=WIDTH_CHOICES, label=_("Column width"), help_text=("Width of created columns. You can still change the width of the column afterwards."))


    class Meta:
        model = PicoRow
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')