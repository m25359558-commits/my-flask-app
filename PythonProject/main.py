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
        "photo_url": "https://i.pinimg.com/originals/33/53/e8/3353e89fa1f7f773aa830563aca0f90c.jpg",
        "floor":"Мужской",
        "age":"45 лет"
    },
    "academic_info": {
        "responsible_for_contingent":"Центр профессиональной подготовки",
        "faculty":"Центр профессиональной подготовки",
        "department":"Центр профессиональной подготовки",
        "status":"обучается",
        "year":"2025-2026",
        "programType":"Магистратура",
        "educationalProgram":"7M04107-Дело административное",
        "trainingFormat":"очная",
        "Departments":"Русское",
        "educationalLevel":"высшего образования",
        "durationTraining":"1 год",
        "yearStudy":"1-й год обучения",
        "TypeAcademicPeriod":"семестровая система",
        "financing":"договор 2-х сторонний",
        "typeCurriculum":"центр профессиональной подготовки"
    },  
    # мед страховка
    "insurance_info": {
        "title": "Обязательное социальное медицинское страхование (ОСМС)",
        "service": "msqory.kz",
        "status": "Застрахован",
        "last_update": "01.05.2026 01:36:01",
        "description": "Данные загружаются с Фонда Социального Медицинского Страхования"
    },
    # пенья
    "penalty":{
        "titles":"Задолжность по оплате за обучение / Пеня" ,
        "note":"Внимание!",
        "arrears":"имеется не большая задолжность по оплате за обучение!Она пока не БЛОКИРУЕТ доступ к сесси ",
        "main_debt":"основной долг:0.00тг",
        "fine":"пеня:30 241.00 тг",
        "reminder":"Напрминаем что основной долг и пения должныоплачиваться отдельными платежами, с указанием соответствующего основания платежа"
    },
    # итоговый гпа
    "resultGPA":{
        "title":"Итоговый GPA",
        "note":"Внимание",
        "info_GPA":"Итоговый GPA подсчитывается только по дисциплинам трвнскрипта, которые имеют итогувую оценку!",
        "counting_formula":"Формула подсчета:Для каждой дисциплины имеющую оценку подсчитывается произведение кредитов на балы.Все произведения суммируются и затемм делятся на ссуму всех кредитов",
        "summaryGPA":"итоговый GPA:2.84",
        "loans":"Итого кредитов 139/170"
    },
    # предупреждение
    "warning":{
        "note":"Внимание!",
        "scores_statement":"Баллы Ведомость(РК,РК2 и Экзамен/Итоговый контроль) доступны только выставленные в систему АСУ преподавателем и утвержденые офис - регистратором начиная с апреля 2023 года.",
        "socores_transcript":"Баллы Транскрипт(Итого в процентах,Итого в балах) должны содержать все выставленные и перезачтенные дисциплины с момента начала обучения на текущей образовательной программе.",
    },
    # Таблица, разделенная по учебным периодам
    "academic_periods": [
        {
            "period_title": "2025 - 2026 учебный год, 2 семестр (2026 год, весна)",
            "subjects": [
                {
                    "name": "Академическое письмо",
                    "code": "AP B01",
                    "credits": 4,
                    "rk1": {"score": "30", "teacher": "Алдабергенқызы Л."},
                    "rk2": {"score": "72", "teacher": "Алдабергенқызы Л."},
                    "exam": "-",
                    "total_percent": "-",
                    "total_score": "-",
                    "gpa": "-"  # Добавлен столбик GPA
                },
                {
                    "name": "Введение в предпринимательство",
                    "code": "VP B01",
                    "credits": 5,
                    "rk1": {"score": "60", "teacher": "Муратов У. М."},
                    "rk2": {"score": "50", "teacher": "Сисенова А. Т."},
                    "exam": "-",
                    "total_percent": "-",
                    "total_score": "-",
                    "gpa": "-" # Добавлен столбик GPA
                },
                {
                    "name": "Второй иностранный язык - IV",
                    "code": "VIYa(IV) B01",
                    "credits": 5,
                    "rk1": {"score": "79", "teacher": "Комекова М. О."},
                    "rk2": {"score": "76", "teacher": "Комекова М. О."},
                    "exam": "-",
                    "total_percent": "-",
                    "total_score": "-",
                    "gpa": "-" # Добавлен столбик GPA
                },
                {
                    "name": "Креативное мышление",
                    "code": "KM B01",
                    "credits": 3,
                    "rk1": {"score": "50", "teacher": "Тулекова Г. Х."},
                    "rk2": {"score": "75", "teacher": "Елекенова М. М."},
                    "exam": "-",
                    "total_percent": "-",
                    "total_score": "-",
                    "gpa": "-" # Добавлен столбик GPA
                },
                {
                    "name": "Производственная практика - II",
                    "code": "PP(II) B01",
                    "credits": 4,
                    "rk1": {"score": "-", "teacher": ""},
                    "rk2": {"score": "-", "teacher": ""},
                    "exam": "-",
                    "total_percent": "-",
                    "total_score": "-",
                    "gpa": "-" # Добавлен столбик GPA
                },
                {
                    "name": "Услуги по переводу",
                    "code": "UP B01",
                    "credits": 5,
                    "rk1": {"score": "90", "teacher": "Головчун А. А."},
                    "rk2": {"score": "90", "teacher": "Головчун А. А."},
                    "exam": "-",
                    "total_percent": "-",
                    "total_score": "-",
                    "gpa": "-" # Добавлен столбик GPA
                },
                {
                    "name": "Финансовое сопровождение бизнеса",
                    "code": "FSB B01",
                    "credits": 5,
                    "rk1": {"score": "68", "teacher": "Мухамедьярова-Левина Т. Т."},
                    "rk2": {"score": "65", "teacher": "Мухамедьярова-Левина Т. Т."},
                    "exam": "-",
                    "total_percent": "-",
                    "total_score": "-",
                    "gpa": "-" # Добавлен столбик GPA
                },
                # Твой итоговый блок
                {
                    "result": "итого освоено за период",
                    "score": "0/31",
                    "gpa": "-"
                }
            ]
        }
    ],
   # НОВЫЙ БЛОК: ПЕРЕЗАЧЕТ (на основе скриншота)
    "overdrawing": [
        {
            "name": "Базовый иностранный язык",
            "code": "BI B01",
            "credits": 4,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "74",
            "gpa": "2.33"
        },
        {
            "name": "Базовый иностранный язык в контексте межкультурной коммуникации",
            "code": "BIYaKMK B01",
            "credits": 4,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "69",
            "gpa": "2.00"
        },
        {
            "name": "Введение в языкознание",
            "code": "VYa B01",
            "credits": 5,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "87",
            "gpa": "3.33"
        },
        {
            "name": "Второй иностранный язык",
            "code": "VIYa B01",
            "credits": 5,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "94",
            "gpa": "3.67"
        },
        {
            "name": "Второй иностранный язык - I",
            "code": "VIYa(I) B01",
            "credits": 4,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "89",
            "gpa": "3.33"
        },
        {
            "name": "Второй иностранный язык - III",
            "code": "VIYa(III) B01",
            "credits": 5,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "94",
            "gpa": "3.67"
        },
        {
            "name": "Иностранный язык - I",
            "code": "IYa(I) B01",
            "credits": 5,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "71",
            "gpa": "2.33"
        },
        {
            "name": "Иностранный язык - II",
            "code": "IYa(II) B01",
            "credits": 5,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "75",
            "gpa": "2.67"
        },
        {
            "name": "Иностранный язык по социально-гуманитарному и естественно-научному направлению",
            "code": "IYaSGENN B01",
            "credits": 5,
            "rk1": "-", "rk2": "-", "exam": "-",
            "total_score": "82",
            "gpa": "3.00"
        }
    ]
}

# 2. Данные ПРЕПОДАВАТЕЛЯ
TEACHER_DATA = {
    "role": "teacher",
    "personal_info": {
        "full_name": "Иванов Иван Иванович",
        "work":"Депортамент по академическим вопросам/ директор",
        "iin": "10020030",
        "email": "30938888187@turan-edu.kz",
        "mob_phone": "+7(777)123-45-67",
        "work_phone":"+7(727)260-40-07",
        "work_phone2":"1030",
        "body":"павильон №1/UN 301",
        "Birthday":"Мужской/10 октября"
    },
    "professional_info": {
        "status":"работает",
        "division":"депортамент по академическим вопросам",
        "faculty": "Информационные технологии",
        "department": "Программная инженерия",
        "position": "Директор",
        "bet":"1",
        "photo_url": "https://img.freepik.com/premium-psd/portrait-attractive-calm-bearded-man-with-flawless-skin-isolated-light-transparent-background_410516-124384.jpg?w=740"
    },
    #Информация о дополнительных должностях
    "additional_positions":{
        "division":"Высшая школа информационных технологий",
         "post":"проффесор",
    "bet":"0.50"
    },
    # информация об ученой степени
    "information_about_academic_degree":{
    "academic_degree":"доктор наук",
    "academic_degree1":"кандидант наук",
    "branch_science":"технических наук",
    "branch_science2":"физо-математическх наук",
    "date_issue":"16.06.2011",
    "date_issue2":"21.12.1993"
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
