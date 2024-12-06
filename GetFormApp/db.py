from tinydb import TinyDB
from validations import validate_field_type

def get_templates():
    db = TinyDB("form_templates.json")
    return db.all()

def find_matching_template(form_data):
    templates = get_templates() # Выводим все шаблоны

    for template in templates:
        # Генератор словаря, исключаем из результатов у которых ключ равен "name"
        template_fields = {key: value for key, value in template.items() if key != "name"}

        is_matching = True

        for key, field_type in template_fields.items():
            # Проверка ключа, типа значения и самого значения ключа параметра запроса на соответствие
            if key not in form_data or type(form_data[key]) is not str or not validate_field_type(form_data[key], field_type):
                is_matching = False
                break

        # Если все ок
        if is_matching:
            return template

    # Если нет, то переходим к типизаций
    return None
