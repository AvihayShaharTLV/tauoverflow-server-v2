import pandas as pd
import os
import glob


def process_courses_in_maslul(maslul_path, folder, maslul_name):
    maslul_courses = pd.read_csv(maslul_path, index_col=0)
    maslul_courses.drop_duplicates(subset=['course_id'], inplace=True)
    maslul_name_alone = maslul_name.replace('.csv', '')
    final_maslul_path = folder + '\\' + maslul_name_alone + '_test.csv'
    maslul_courses.to_csv(final_maslul_path, index=False)


path = r''

for z, faculties, files in os.walk(path):
    for faculty in faculties:
        if faculty != 'dsfdsf':
            continue
        faculty_folder = os.path.join(path, faculty)
        maslulim = [file_path for file_path in glob.iglob(faculty_folder + '**\*.csv')]
        print(f'All courses for {faculty} faculty:')
        for maslul in maslulim:
            print(maslul)
            process_courses_in_maslul(maslul, faculty_folder, maslul.split('\\')[-1])
        print('\n')
