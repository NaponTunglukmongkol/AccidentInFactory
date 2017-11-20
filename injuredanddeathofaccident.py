import pandas as pd
import pygal
df = pd.read_csv('ProjectPsit1.csv')
years = df.ปี
accident = df.accident
injured = df.injured
death = df.death
injuredfire_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
injuredexplode_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
injuredgas_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
injuredmachine_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
deathfire_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
deathexplode_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
deathgas_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
deathmachine_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(years)):
    if years[i] == 2544:
        plus = 0
    elif years[i] == 2545:
        plus = 1
    elif years[i] == 2546:
        plus = 2
    elif years[i] == 2547:
        plus = 3
    elif years[i] == 2548:
        plus = 4
    elif years[i] == 2549:
        plus = 5
    elif years[i] == 2550:
        plus = 6
    elif years[i] == 2551:
        plus = 7
    elif years[i] == 2552:
        plus = 8
    elif years[i] == 2553:
        plus = 9
    elif years[i] == 2554:
        plus = 10
    elif years[i] == 2555:
        plus = 11
    elif years[i] == 2556:
        plus = 12
    if accident[i] == "อัคคีภัย":
        injuredfire_lst[0+plus] = injuredfire_lst[0+plus] + injured[i]
        deathfire_lst[0+plus] = deathfire_lst[0+plus] + death[i]
    elif accident[i] == "ระเบิด":
        injuredexplode_lst[0+plus] = injuredexplode_lst[0+plus] + injured[i]
        deathexplode_lst[0+plus] = deathexplode_lst[0+plus] + death[i]
    elif accident[i] == "ก๊าซแอมโมเนียรั่ว":
        injuredgas_lst[0+plus] = injuredgas_lst[0+plus] + injured[i]
        deathgas_lst[0+plus] = deathgas_lst[0+plus] + death[i]
    elif accident[i] == "เครื่องจักร":
        injuredmachine_lst[0+plus] = injuredmachine_lst[0+plus] + injured[i]
        deathmachine_lst[0+plus] = deathmachine_lst[0+plus] + death[i]


line = pygal.Bar()
line.title = "จำนวนผู้คนเจ็บตายในอุบัติเหตุtop 4"
line.x_labels = (2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556)
line.add("อัคคีภัย-เจ็บ", injuredfire_lst)
line.add("อัคคีภัย-ตาย", deathfire_lst)
line.add("ระเบิด-เจ็บ", injuredexplode_lst)
line.add("ระเบิด-ตาย", deathexplode_lst)
line.add("แก๊ซแอมโมเนียรั่ว-เจ็บ", injuredgas_lst)
line.add("แก๊ซแอมโมเนียรั่ว-ตาย", deathgas_lst)
line.add("เครื่องจักร-เจ็บ", injuredmachine_lst)
line.add("เครื่องจักร-ตาย", deathmachine_lst)
line.render_to_file("test3.svg")\

