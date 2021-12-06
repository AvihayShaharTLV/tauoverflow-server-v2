# -*- encoding: utf-8 -*-

import glob
import os
import pandas as pd

schema = 'sababa'


def define_courses_insert_query(course_id: str, name: str, department_english_name: str) -> str:
    query = f"INSERT INTO {schema}.courses (course_id, name, department_id)" \
            f" VALUES ('{course_id}', '{name}'," \
            f" (SELECT id from sababa.departments WHERE departments.english_name='{department_english_name}'));\n "
    return query


def process_course(department_path: str) -> str:
    department_english_name = department_path.split('\\')[-1].split('.')[0]
    df = pd.read_csv(department_path, index_col=False)
    queries = []
    for i, row in df.iterrows():
        query = define_courses_insert_query(row['course_id'], row['course_name'].replace('\'', ''),
                                            department_english_name)
        queries.append(query)
    return queries


path = r''

counter = 0
with open('', 'w', encoding='utf-8') as file:
    for z, faculties, files in os.walk(path):
        for faculty in faculties:
            faculty_folder = os.path.join(path, faculty)
            departments = [file_path for file_path in glob.iglob(faculty_folder + '**\*.csv')]
            for department in departments:
                department_courses_queries = process_course(department)
                counter += len(department_courses_queries)
                print(counter)
            #     file.writelines(department_courses_queries)
            # file.write('\n')

print(counter)