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
        "floor":"Мужской/10.12.1980/45 лет",
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
},
    #Инфо об учебном звании
"Information_about_academic_title":{
    "academic_rank_1":"Доцент",
    "academic_rank_2":"Профессор",
    "specialization_1":"Информатика, вычислительная техника и автоматизация",
    "specialization_2":"Информатика",
    "date_issue_1":"06.06.1997",
    "date_issue_2":"28.04.2005"
},
    #Информация о повышении квалификации
    "Information_about_professional_development":{
        "discipline_profile1":"-",
        "discipline_profile2":"-",
        "discipline_profile3":"-",
        "discipline_profile4":"-",
        "form_name_topic1":"Курс:IT-менеджмент и управление технологическими проектами",
         "form_name_topic2":"Курс: Криптографическая защита и безопасность операционных и облачных IT - систем",
         "form_name_topic3":"Курс: IT- менеджмент и управление технологическими пректами",
         "form_name_topic4":"Курс: IT- менеджмент и управление цифровыми пректами",
         "data1":"02.02.2026",
         "data2":"02.02.2026",
         "data3":"02.02.2026",
         "data4":"02.02.2026",
    },
    #Идентификаторы автора научных трудов
    "Identifiers_author_scientific_papers":{
        "ORC_ID":"0000-0001-8280-1837",
        "Researcher_ID":"JPE-5229-2023",
        "Hirsch_Index":"-",
    },
   "scientific_statistics": {
    "pub_label": "Публикации", 
       "pub_total": "12", 
       "pub_5y": "6",
       "pub_is_sub": False,
    
    "scopus_label": "Scopus", 
       "scopus_total": "3",
       "scopus_5y": "2", 
       "scopus_is_sub": True,
    
    "wos_label": "WoS", 
       "wos_total": "0", 
       "wos_5y": "0",
       "wos_is_sub": True,
    
    "rinc_label": "РИНЦ",
       "rinc_total": "0", 
       "rinc_5y": "0", 
       "rinc_is_sub": True,
    
    "koks_label":"Комитет (КОКСНВО)", 
       "koks_total": "0",
       "koks_5y": "0",
       "koks_is_sub": True,
    
    "other_label": "Иное",
       "other_total": "9", 
       "other_5y": "4", 
       "other_is_sub": True,
    
    "docs_label": "Охранные документы",
       "docs_total": "0",
       "docs_5y": "×", 
       "docs_is_sub": False,
    
    "nir_label": "Договоры НИР", 
       "nir_total": "0",
       "nir_5y": "×",
       "nir_is_sub": False
},
    "scientific_info": {
    "sci_dir_1": "Естественные науки, математика и статистика",
    "sci_role_1": "Автор",
    "sci_title_1": "Монография: Математическое моделирование напряженно-деформированного состояния оболочечных конструкций",
    "sci_level_1": "Республиканский",

    "sci_dir_2": "Информационно-коммуникационные технологии",
    "sci_role_2": "Автор",
    "sci_title_2": "Учебное пособие: Жүйелік Бағдармалау",
    "sci_level_2": "Республиканский",

    "sci_dir_3": "Бизнес, управление и право",
    "sci_role_3": "Автор",
    "sci_title_3": "Учебное пособие: ЖОБАЛАРДЫ БАСҚАРУ: MS PROJECT БОЙЫНША",
    "sci_level_3": "Республиканский"
  },
    "discipline_info": {
  "disc_name_1": "PVSOUTU M01 - Практикум по внедрению стандартов в области управления IT услугами",
  "disc_load_1": "Лекция, Практика, СРОП",
  "disc_lang_1": "Русский",
  "disc_period_1": "1 семестр",

  "disc_name_2": "IODH M01 - ITSM: обзор и основные характеристики ITIL",
  "disc_load_2": "Лекция, Практика, СРОП",
  "disc_lang_2": "Русский, Казахский",
  "disc_period_2": "1 семестр",

  "disc_name_3": "SMI M01 - Стратегический менеджмент в ИТ сфере",
  "disc_load_3": "Лекция, Практика, СРОП",
  "disc_lang_3": "Русский, Казахский",
  "disc_period_3": "1 семестр"
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
