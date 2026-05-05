import functions_framework
from flask import Flask, jsonify, request

# Создаем приложение Flask СНАРУЖИ всех условий, чтобы Render его видел
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 1. Данные СТУДЕНТА
STUDENT_DATA = {
    "role": "student",
    "personal_info": {
        "full_name": "Шавдинов Асан Нурахметович",
        "id_contingent": "25263111",
        "iin": "801210300993",
        "email": "215452@turan-edu.kz",
        "phone": "+7(701)734-83-67",
        "birth_date": "10.12.1980",
        "citizenship": "Гражданин Республики Казахстан", 
        "photo_url": "https://i.pinimg.com/originals/33/53/e8/3353e89fa1f7f773aa830563aca0f90c.jpg"
    },
    "academic_info": {
        "responsible_for_contingent": "Центр профессиональной подготовки",
        "faculty": "Центр профессиональной подготовки",
        "department": "Центр профессиональной подготовки",
        "status": "Обучается",
        "year_of_up": "2025 - 2026",
        "program_type": "Магистратура",
        "educational_program": "7M04107 - Деловое администрирование (EMBA)",
        "study_form": "Очная",
        "division": "Русское",
        "education_level": "высшее образование",
        "study_period": "1 год",
        "current_year": "1-й год обучения",
        "academic_period_type": "Семестровая система",
        "financing_type": "Договор 2-х сторонний",
        "curriculum_type": "Центр профессиональной подготовки" # Проверь кавычки тут!
    }
}

# 2. Данные ПРЕПОДАВАТЕЛЯ
TEACHER_DATA = {
    "role": "teacher",
    "personal_info": {
        "full_name": "Иванов Иван Иванович",
        "iin": "10020030",
        "email": "30938888187@turan-edu.kz",
        "phone": "+7(777)123-45-67"
    },
    "professional_info": {
        "faculty": "Информационные технологии",
        "department": "Программная инженерия",
        "position": "Профессор",
        "photo_url": "https://img.freepik.com/premium-psd/portrait-attractive-calm-bearded-man-with-flawless-skin-isolated-light-transparent-background_410516-124384.jpg?w=740"
    }
}

# Основная функция обработки
def get_profile_logic(req):
    headers = {'Access-Control-Allow-Origin': '*'}
    role = req.args.get('role', 'student')
    if role == 'teacher':
        return jsonify(TEACHER_DATA), 200, headers
    return jsonify(STUDENT_DATA), 200, headers

# Маршрут для Flask (для Render)
@app.route('/')
def index():
    return get_profile_logic(request)

# Обработчик для Cloud Functions (если вдруг захочешь вернуться)
@functions_framework.http
def get_profile(request):
    return get_profile_logic(request)

# Блок для запуска на твоем ПК
if __name__ == "__main__":
    print("\n[OK] Сервер запущен!")
    print("[СТУДЕНТ]: http://127.0.0.1:5000/")
    print("[ПРЕПОДАВАТЕЛЬ]: http://127.0.0.1:5000/?role=teacher")
    app.run(host='0.0.0.0', port=5000)
