from django import forms


class SearchForm(forms.Form):
    CHOICES_COLOMN = (
        ('title', 'Название'),
        ('count', 'Количество'),
        ('distance', 'Расстояние'),
    )
    CHOICES_CONDITION =(
        ('exact', 'Равно'),
        ('contains', 'Содержит'),
        ('gt', 'Больше'),
        ('lt', 'Меньше'),
    )
    colomn = forms.ChoiceField(choices=CHOICES_COLOMN, label='Выбор колонки для поиска')
    condition = forms.ChoiceField(choices=CHOICES_CONDITION, label='Выбор условия для поиска')
    q = forms.CharField(min_length=1, max_length=25, required=True, label='Поиск')

