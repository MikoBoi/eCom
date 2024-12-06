import uvicorn
from fastapi import FastAPI, Request
from db import find_matching_template
from validations import validate_and_type_fields

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Отправь POST запрос на /get_form"}

@app.post("/get_form")
async def get_form(request: Request):
    form_data = await request.json()

    # Находим подходящий шаблон
    matching_template = find_matching_template(form_data)
    if matching_template:
        return {"template_name": matching_template["name"]}

    # Если шаблон не найден, выполнить типизацию полей
    typed_fields = validate_and_type_fields(form_data)
    return typed_fields

if __name__ == "__main__":
    uvicorn.run(app)
