from django.core.exceptions import ValidationError


def validate_year(year):
    if year < 1990 or year > 2050:
        raise ValidationError('Значение года может быть в пределах от 1990 до 2050')
