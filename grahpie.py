




import pandas as pd





df = pd.read_csv('ProjectPsit1.csv')










years = df.ปี
year_all = []
for year in years:
    if year not in year_all:
        year_all.append(year)
year_all





def kindofaccident():
    accidents = df.accident
    accident_all = []
    for accident in accidents:
        if accident not in accident_all:
            accident_all.append(accident)
    return accident_all





def injured_dicc():
    injured_dic = {}
    injured = df.injured
    year_b = year_all[0]
    people_injured = 0
    for i in year_all:
        injured_dic[year_b] = people_injured
        people_injured = 0
        for people, year in zip(injured,years):
            if year == i:
                people_injured += people
        year_b = i
    injured_dic[year_b] = people_injured
    list_injured = [injured_dic[year] for year in year_all]
    return list_injured
            





def death_year():
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








def accident_year():
    accident_all = df.accident
    count_accident = 0
    dic_acc = {}
    accident_b = 0
    for accident in kindofaccident():
        dic_acc[accident_b] = count_accident
        count_accident = 0
        for accidents in accident_all:
            if accident == accidents:
                count_accident += 1
        accident_b = accident
        dic_acc[accident_b] = count_accident
    return dic_acc
                
                
            
         
    


summary_all = df.summary
summary_list = []
for summary in summary_all:
    if summary not in summary_list:
        summary_list.append(summary)
accident_all = df.accident


# In[14]:


def accident_count(accident_choice):
    summary_fire = {}
    summary_b = "0"
    count = 0
    for summary in summary_list:
        if count > 0:
                summary_fire[summary_b] = count
        count = 0
        for accident, summary_s in zip(accident_all, summary_all):
            if accident == accident_choice and summary_s == summary:
                count += 1
        summary_b = summary
    summary_fire[summary_b] = count






    a = sorted(summary_fire.values())
    a.sort(reverse=True)    
    list_top_4 = []





    for i in range(4):
        list_top_4.append(list(summary_fire.keys())[list(summary_fire.values()).index(a[i])])





    count = 0
    dic_summary_top_4 = {}
    for summary in list_top_4:
        dic_summary_top_4[summary] = summary_fire[summary]
        count += summary_fire[summary]
    if accident_year()[accident_choice] - count != 0:
            dic_summary_top_4["อื่นๆ"] = accident_year()[accident_choice] - count 

    import pygal
    pie_chart = pygal.Pie()
    pie_chart.title ='สาเหตหลักของการเกิด'+accident_choice+' %'
    for summary in dic_summary_top_4:
        percent = round((dic_summary_top_4[summary])/(accident_year()[accident_choice])*100, 2)
        pie_chart.add(summary, percent)
    pie_chart.render_to_file('pie_chart.svg')
accident_count(input())
