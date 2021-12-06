import time

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path="",
                          options=chrome_options)
driver.get("https://www.ims.tau.ac.il/tal/kr/search_p.aspx")
select = Select(driver.find_element_by_id('lstYear1'))
select.select_by_value('2020')
semesters = (driver.find_elements_by_name('ckSem'))

# semesters[2].click()

csv_name = 'security_studies' + '.csv'

# facultyselect1 = Select(driver.find_element_by_id('lstDep1'))
# facultyselect1.select_by_value('0897')
# facultyselect2 = Select(driver.find_element_by_id('lstDep2'))
# facultyselect2.select_by_value('0560')
facultyselect3 = Select(driver.find_element_by_id('lstDep3'))
facultyselect3.select_by_value('1052')
# facultyselect4 = Select(driver.find_element_by_id('lstDep4'))
# facultyselect4.select_by_value('0491')
# facultyselect5 = Select(driver.find_element_by_id('lstDep5'))
# facultyselect5.select_by_value('2171-2172')
# facultyselect6 = Select(driver.find_element_by_id('lstDep6'))
# facultyselect6.select_by_value('0368')
# facultyselect7 = Select(driver.find_element_by_id('lstDep7'))
# facultyselect7.select_by_value('14')
# facultyselect8 = Select(driver.find_element_by_id('lstDep8'))
# facultyselect8.select_by_value('1242')
# facultyselect9 = Select(driver.find_element_by_id('lstDep9'))
# facultyselect9.select_by_value('0191')
# facultyselect10 = Select(driver.find_element_by_id('lstDep10'))
# facultyselect10.select_by_value('15')
# facultyselect10 = Select(driver.find_element_by_id('lstDep11'))
# facultyselect10.select_by_value('2172')
# facultyselect12 = Select(driver.find_element_by_id('lstDep12'))
# facultyselect12.select_by_value('1883')
# facultyselect13 = Select(driver.find_element_by_id('lstDep13'))
# facultyselect13.select_by_value('1843')
# facultyselect14 = Select(driver.find_element_by_id('lstDep14'))
# facultyselect14.select_by_value('2120')
time.sleep(1)

(driver.find_element_by_id('search1')).click()

elements = driver.find_elements_by_class_name('listtdbld')
lines = []

for i in range(len(elements)):
    line = str(elements[i].text)
    line = line.split("  ")
    l = len(line[1])
    line1 = line[1][9:]
    line2 = line[1][6:8]
    lines.append((line[0], line1, line2))

result_df = pandas.DataFrame(columns=['course_name', 'course_id'])

i = 0
while True:
    try:
        for i in range(len(elements)):
            line = str(elements[i].text)
            line = line.split("  ")
            l = len(line[1])
            line1 = line[1][9:]
            line2 = line[1][6:8]
            lines.append([line[0], line1, line2])
            result_df = result_df.append({'course_name': line1, 'course_id': line[0]}, ignore_index=True)
        (driver.find_element_by_id('next')).click()
        elements = driver.find_elements_by_class_name('listtdbld')
        time.sleep(2)
        i += 1
    except Exception as e:
        # driver.quit()
        print('Something failed! i = ', i)
        print(e)
        break
print(len(lines))

result_df.to_csv(csv_name, encoding='utf-8')