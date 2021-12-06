# -*- encoding: utf-8 -*-

import glob
import os
import pandas as pd

schema = 'sababa'

english_to_hebrew_dict = {
    'Abroad Students': 'סטודנטים מחול',

    'Kelim Shluvim': 'כלים שלובים',

    'Architecture': 'ביה"ס לאדריכלות',
    'Art Elective Courses': 'חטיבה לשיעורי בחירה',
    'Art History': 'החוג לתולדות האמנות',
    'Film School': 'ביה"ס לקולנוע וטלוויזיה',
    'Training Studies In Cinema': 'לימודי הכשרה בקולנוע',
    'Multidisciplinary Art Program': 'התוכנית הרב תחומית באמנויות',
    'Music School': 'ביה"ס למוזיקה',
    'Theater': 'החוג לאמנות התאטרון',
    'Cyber': 'סייבר',

    'Biomedical Engineering': 'הנדסה ביו-רפואית',
    'Electricity And Eectronics': 'חשמל ואלקטרוניקה',
    'Hightech Science': 'מדעים להייטק',
    'Industrial Engineering': 'הנדסת תעשייה',
    'Masters Biomedical Engineering': 'תואר שני - הנדסה ביו-רפואית',
    'Masters Environment Engineering': 'תואר שני - הנדסת סביבה',
    'Masters Industrial Engineering': 'תואר שני - הנדסת תעשייה',
    'Masters Mechanical Engineering': 'תואר שני - הנדסה מכנית',
    'Masters Systems Engineering': 'תואר שני - הנדסת מערכות',
    'Material Sciences Engineering': 'מדע והנדסה של חומרים',
    'Mechanical Engineering': 'הנדסה מכנית',
    'School Of Electrical Engineering': 'ביה"ס להנדסת חשמל',
    'Service Courses': 'קורסי שירות',

    'Communication': 'תקשורת',
    'Diplomacy': 'התכנית לדיפלומטיה',
    'Economy': 'כלכלה',
    'Immigration Studies': 'לימודי הגירה',
    'Political Science': 'מדע המדינה',
    'Psychology': 'פסיכולוגיה',
    'Public Policy': 'מדיניות ציבורית',
    'Security Studies': 'לימודי בטחון',
    'Social Sciences General': 'מדכי החברה - כללי',
    'Sociology And Antropology': 'סוציולוגיה ואנתרופולוגיה',
    'Work Studies': 'לימודי עבודה',

    'Biochemistry': 'ביוכימיה',
    'Biology': 'ביולוגיה',
    'Cell Studies Immunology': 'חקר התא ולאימונולוגיה',
    'Microbiology Moleculary Biotechnology': 'מיקרוביולוגיה מולקולרית וביוטכנולוגיה',
    'Neurobiochemistry': 'ניורוביוכימיה',
    'Plant Sciences': 'מדעי הצמח',
    'Zoology': 'זואולוגיה',

    'Chemistry': 'כימיה',
    'Computer Science': 'מדעי המחשב',
    'Environment Studies': 'לימודי הסביבה',
    'Geography And Human Environment': 'גאוגרפיה וסביבת האדם',
    'Geophysics': 'גיאופיזיקה',
    'Mathematics': 'מתמטיקה',
    'Physics And Astronomy': 'פיזיקה ואסטרונומיה',
    'Statistics And Performance Studies': 'סטטיסטיקה וחקר ביצועים',

    'Laws': 'משפטים',

    'Accountancy': 'חשבונאות',
    'Business Administration For Managers ': 'מנהל עסקים למנהלים',
    'Business Administration': 'התוכנית למנהל עסקים',
    'Health Systems': 'התוכנית למנהל מערכות בריאות',
    'Managment Science Performance Studies ': 'מדעי הניהול - חקר ביצועים והחלטות',
    'Managment Science Technology Systems': 'מדעי הניהול - טכנולוגיה ומערכות מידע',
    'Managment': 'ניהול',

    'Dentistry': 'ביה"ס לרפואת שיניים',
    'Emergency And Disaster Management': 'ניהול מצבי חירום ואסון',
    'Epidemiology': 'אםידמיולוגיה',
    'Graduate School': 'המדרשה לתארים מתקדמים',
    'Integrated Program In Life Science And Medicine': 'התוכנית המשולבת במדעי החיים והרפואה',
    'Masters Physiotherapy And Occupational Therapy': 'פיזיותרפיה וריפוי בעיסוק - תואר שני',
    'Medical School': 'ביה"ס לרפואה',
    'Nursing': 'סיעוד',
    'Occupational Health': 'בריאות תעסוקתית',
    'Occupational Therapy': 'ריפוי בעיסוק',
    'Physiotherapy': 'פיזיותרפיה',
    'Public Health': 'בריאות הציבור',
    'Studies Of Communication Disorders': 'לימודי הפרעות בתקשורת',

    'Curriculum Planning And Teaching': 'תכנון לימודים והוראה',
    'Mathematical Scientific And Technological Education': 'חינוך מתמטי, מדעי וטכנולוגי',
    'Policy And Administration In Education': 'מדיניות ומנהל בחינוך',
    'School Of Education': 'ביה"ס לחינוך',
    'School Of Neuroscience': 'ביה"ס למדעי המוח',
    'School Of Social Work': 'ביה"ס לעבודה סוציאלית',
    'Special Education': 'ביה"ס לחינוך מיוחד',

    'English As Foreign Language': 'אנגלית כשפה זרה',
    'Foreign Languages': 'שפות זרות',

    'Connected Plus': 'מתחברים פלוס',

    'Africa Studies Intra Uni': 'לימודי אפריקה בתוכנית הבין-אוניברסיטאית',
    'Arabic Islam Studies': 'לימודי הערבית והאיסלאם',
    'Archeology': 'ארכיאולוגיה ותרבויות המזרח הקדום',
    'Certificate Studies In Translation And Translation Editing': 'לימודי תעודה בתרגום ועריכת תרגום',
    'Child And Youth Culture Research': 'מחקר תרבות הילד והנוער',
    'Classical Studies': 'לימודים קלאסיים',
    'Cognitive Studies Language And Uses': 'לימודים קוגניטיביים של השפה ושימושיה',
    'Cultural Sciences': 'מדעי התרבות',
    'East Asia Studies': 'לימודי מזרח אסיה',
    'English': 'אנגלית',
    'French': 'צרפתית',
    'General History': 'היסטוריה כללית',
    'General Linguistics': 'בלשנות כללית',
    'Hebrew Language And Semitic Linguistics': 'הלשון העברית ובלשנות שמית',
    'History And Philosophy Of Science And Ideas': 'היסטוריה ופילוסופיה של המדעים והרעיונות',
    'History School': 'ביה"ס להיסטוריה',
    'Israel People History': 'היסטוריה של עם ישראל',
    'Jewish Philosopy And Talmud': 'פילוסופיה יהודית ותלמוד',
    'Language Teaching Unit': 'היחידה להוראת שפות',
    'Legend': 'מקרא',
    'Linuistic Editing Certificate': 'לימודי תעודה - עריכה לשונית',
    'Literature': 'ספרות',
    'Masters Gender Studies': 'תוכנית ללימודי מגדר - תואר שני',
    'Middle East Africa History': 'היסטוריה של המזה"ת ואפריקה',
    'Middle East Studies Of Our Time': 'לימודי המזה"ת בן זמננו',
    'Multidisciplinary Program In The Humanities': 'התוכנית הרב-תחומית במדעי הרוח',
    'Philosopy': 'פילוסופיה',
    'Pkm': 'פכ"מ',
    'Religious Sciences': 'מדעי הדתות',
    'Women And Gender Studies': 'התוכנית ללימודי נשים ומגדר'
}


def define_department_insert_query(english_name: str, hebrew_name: str, faculty_english_name: str) -> str:
    query = rf"INSERT INTO {schema}.departments (english_name, hebrew_name, faculty_id)" \
           f" VALUES ('{english_name}', '{hebrew_name}'," \
           f" (SELECT id from sababa.faculties WHERE faculties.english_name='{faculty_english_name}'));\n"
    return query


def process_department(department_path: str, faculty_english_name: str) -> str:
    department_english_name = department_path.split('\\')[-1].split('.')[0]
    query = define_department_insert_query(department_english_name, english_to_hebrew_dict[department_english_name],
                                           faculty_english_name)
    return query


path = r''

with open('insert_script_2.txt', 'w', encoding='utf-8') as file:
    for z, faculties, files in os.walk(path):
        for faculty in faculties:
            faculty_folder = os.path.join(path, faculty)
            departments = [file_path for file_path in glob.iglob(faculty_folder + '**\*.csv')]
            for department in departments:
                department_query = process_department(department, faculty)
                file.write(department_query)
            file.write('\n')
