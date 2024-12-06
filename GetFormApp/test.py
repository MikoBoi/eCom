import requests

BASE_URL = "http://127.0.0.1:8000"

# Тестовые запросы
datas = [
    # Успешные запросы
    {
        "user_email": "test@test.test",
        "order_date": "2024-12-06"
    },
    {
        "user_email": "test@test.test",
        "user_phone": "+71234567890",
    },
    {
        "user_email": "test@example.com",
        "comment_text": "Текст"
    },

    # Неуспешные запросы
    {
        "user_email": "test@example.com",
        "text": "Кул",
        "orderData": "01.01.1999"
    },
    {
        "user_email": 0,
        "phone": "+71234567890",
        "orderData": 9
    },

]

for data in datas:
    response = requests.post(f"{BASE_URL}/get_form", json=data)
    print(response.json())