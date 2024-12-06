import re
from datetime import datetime

def validate_email(value):
    return re.match(r"[^@]+@[^@]+\.[^@]+", value) is not None # Регулярное выражение на валидность формата почты

def validate_phone(value):
    return re.match(r"^\+7\d{3}\d{3}\d{2}\d{2}$", value) is not None # Регулярное выражение на валидность номера

def validate_date(value):
    try:
        # Проверяем дату на формат "%d.%m.%Y"
        datetime.strptime(value, "%d.%m.%Y")
        return True
    except ValueError:
        try:
            # Проверяем дату на формат "%Y-%m-%d"
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            return False

def validate_field_type(value, field_type):
    if field_type == "email":
        return validate_email(value)
    if field_type == "phone":
        return validate_phone(value)
    if field_type == "date":
        return validate_date(value)
    return True

def validate_and_type_fields(form_data):
    field_types = {}

    for key, value in form_data.items():
        # Проверка если попалось число, возвращаем "number"
        if type(value) in [int, float]:
            field_types[key] = "number"
            continue

        # Остальная проверка
        if validate_date(value):
            field_types[key] = "date"
        elif validate_phone(value):
            field_types[key] = "phone"
        elif validate_email(value):
            field_types[key] = "email"
        else:
            field_types[key] = "text"
    return field_types
