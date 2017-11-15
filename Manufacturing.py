import pandas as pd
df = pd.read_csv("ProjectPsit1.csv")
import pygal
manufacturing = df.ประกอบกิจการ
manu_lst = {}
for i in manufacturing:
    if i not in manu_lst:
        manu_lst[i] = 1
    else:
        manu_lst[i] += 1
prev = 100
textlst = []
numlst = []
for _ in range(4):
    maxed = 0
    for i in (manu_lst.keys()):
        if manu_lst[i] > maxed and manu_lst[i] < prev:
            maxed = manu_lst[i]
            text = i
        else:
            continue
    textlst.append(text)
    numlst.append(maxed)
    prev = maxed

line = pygal.Bar()
line.title = "จำนวนอุบัติเหตุในแต่ละประเภทของโรงงาน."
line.x_labels = (textlst)
line.add("อุบัติเหตุ", numlst)
line.render_to_file("test2.svg")
