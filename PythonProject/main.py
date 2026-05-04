import functions_framework
from flask import Flask, jsonify, request

# 1. Данные СТУДЕНТА (взяты из твоих документов)
STUDENT_DATA = {
    "role": "student",
    "personal_info": {
        "full_name": "Шавдинов Асан Нурахметович",
        "id_contingent": "25263111",
        "iin": "801210300993",
        "email": "25263111@turan-edu.kz",
        "phone": "+7(701)734-83-67",
        "birth_date": "10.12.1980",
        "citizenship": "Гражданин Республики Казахстан"
    },
    "academic_info": {
        "faculty": "Центр профессиональной подготовки",
        "status": "Обучается",
        "program_type": "Магистратура",
        "specialty": "7M04107 - Деловое администратирование (EMBA)",
        "study_form": "Очная",
        "current_year": "1-й год обучения"
    }
}

# 2. Данные ПРЕПОДАВАТЕЛЯ (пример структуры)
TEACHER_DATA = {
    "role": "teacher",
    "personal_info": {
        "full_name": "Иванов Иван Иванович",
        "id_employee": "10020030",
        "email": "i.ivanov@turan-edu.kz",
        "phone": "+7(777)123-45-67"
    },
    "professional_info": {
        "faculty": "Информационные технологии",
        "department": "Программная инженерия",
        "position": "Профессор"
    }
}


@functions_framework.http
def get_profile(request):
    # Настройка CORS для работы с мобильным приложением
    headers = {'Access-Control-Allow-Origin': '*'}

    # Логика: если в запросе есть параметр role=teacher, отдаем препода
    # Иначе по умолчанию отдаем студента
    role = request.args.get('role', 'student')

    if role == 'teacher':
        return jsonify(TEACHER_DATA), 200, headers
    return jsonify(STUDENT_DATA), 200, headers


# Блок для локального запуска на твоем компьютере
if __name__ == "__main__":
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # Чтобы русский текст не превращался в кракозябры


    @app.route('/')
    def index():
        return get_profile(request)


    print("\n[OK] Сервер запущен!")
    print("[СТУДЕНТ]: http://127.0.0.1:5000/")
    print("[ПРЕПОДАВАТЕЛЬ]: http://127.0.0.1:5000/?role=teacher")
    app.run(host='0.0.0.0', port=5000)