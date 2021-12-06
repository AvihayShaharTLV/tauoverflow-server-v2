# -*- encoding: utf-8 -*-

import glob
import os
import pandas as pd

schema = 'sababa'


def define_courses_insert_query(course_id: str, name: str) -> str:
    return f"INSERT INTO {schema}.courses (id, name) VALUES ('{course_id}', '{name}');\n "


def define_courses_in_departments_query(course_id: str, department_name: str) -> str:
    return f"INSERT INTO {schema}.courses_in_departments (course_id, department_id)" \
           f" VALUES ('{course_id}'," \
           f" (SELECT id from {schema}.departments WHERE departments.english_name='{department_name}'));\n "


def generate_courses_in_departments_queries(dep_df: pd.DataFrame, department_name: str) -> list:
    result = []
    department_name = department_name.split('\\')[-1].split('.')[0]
    for j, roww in dep_df.iterrows():
        query = define_courses_in_departments_query((roww['id']), department_name)
        result.append(query)

    return result


path = r'C:\\Users\\avikef\\Desktop\\sql_shit\\faculties'


df = pd.DataFrame(columns=['id', 'name'])
courses_in_departments_queries = []
for z, faculties, files in os.walk(path):
    for faculty in faculties:
        faculty_folder = os.path.join(path, faculty)
        departments = [file_path for file_path in glob.iglob(faculty_folder + '**\*.csv')]
        for department in departments:
            department_df = pd.read_csv(department)
            department_df.rename(columns={'course_id': 'id', 'course_name': 'name'}, inplace=True)
            courses_in_departments_queries.extend(generate_courses_in_departments_queries(department_df, department))
            df = df.append(department_df)
            print(len(courses_in_departments_queries))

with open('course_in_deparments_v1.txt', 'w', encoding='utf-8') as file1:
    for item in courses_in_departments_queries:
        file1.write(item)


df.drop_duplicates(inplace=True)
with open('courses_insert_new.txt', 'w', encoding='utf-8') as file:
    for i, row in df.iterrows():
        file.write(define_courses_insert_query(row['id'], row['name'].replace("'", '')))
