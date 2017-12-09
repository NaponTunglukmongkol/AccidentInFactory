

import pandas as pd





df = pd.read_csv('ProjectPsit1.csv')







years = df.ปี #df.คือการนำปีทั้งหมดมาเป็น list
year_all = []
for year in years: #เก็บปีทั้งหมดว่ามีกี่ปี
    if year not in year_all:
        year_all.append(year)



def kindofaccident(): #ฟังก์ชันหาประเภทอุบัติเหตุว่ามีอะไรบ้าง
    accidents = df.accident
    accident_all = []
    for accident in accidents:
        if accident not in accident_all:
            accident_all.append(accident)
    return accident_all




def injured_dicc(): #ฟังก์ชันเก็บจำนวนคนบาดเจ็บในแต่ละปี
    injured_dic = {}
    injured = df.injured
    year_b = year_all[0]
    people_injured = 0
    for i in year_all:
        injured_dic[year_b] = people_injured #ถ้าปีเปลี่ยนก็เพิ่มจำนวนคนบาดเจ็บเข้าไปใน dict
        people_injured = 0
        for people, year in zip(injured,years): #เช็คคนกับจำนวนปีว่าตรงกันไหมถ้าตรงก็บวกคนบาดเจ็บ
            if year == i:
                people_injured += people
        year_b = i
    injured_dic[year_b] = people_injured
    list_injured = [injured_dic[year] for year in year_all]
    return list_injured
            





def death_year(): #ฟังก์ชันเก็บจำนวนคนเสียชีวิตในแต่ละปี
    death = df.death
    death_dic = {} 
    people_death = 0
    year_b = year_all[0]
    for i in year_all:
        death_dic[year_b] = people_death
        people_death = 0
        for people, year in zip(death, years):
            if year == i:
                people_death += people
        year_b = i
    death_dic[year_b] = people_death
    list_death = [death_dic[year] for year in year_all]
    return list_death
