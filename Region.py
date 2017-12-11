import pandas as pd
df = pd.read_csv("ProjectPsit1.csv")
import pygal

north = ['เชียงราย', 'เชียงใหม่', 'น่าน', 'พะเยา', 'แพร่', 'แม่ฮ่องสอน', 'ลำปาง', 'ลำพูน', 'อุตรดิตถ์']
northeast = ['กาฬสินธุ์', 'ขอนแก่น', 'ชัยภูมิ', 'นครพนม', 'นครราชสีมา', 'บึงกาฬ', 'บุรีรัมย์', 'มหาสารคาม', 'มุกดาหาร', 'ยโสธร', 'ร้อยเอ็ด', 'เลย', 'สกลนคร', 'สุรินทร์', 'ศรีสะเกษ', 'หนองคาย', 'หนองบัวลำภู', 'อุดรธานี', 'อุบลราชธานี', 'อำนาจเจริญ']
middle = ['กำแพงเพชร', 'ชัยนาท', 'นครนายก', 'นครปฐม', 'นครสวรรค์', 'นนทบุรี', 'ปทุมธานี', 'พระนครศรีอยุธยา', 'พิจิตร', 'พิษณุโลก', 'เพชรบูรณ์', 'ลพบุรี', 'สมุทรปราการ', 'สมุทรสงคราม', 'สมุทรสาคร', 'สิงห์บุรี', 'สุโขทัย', 'สุพรรณบุรี', 'สระบุรี', 'อ่างทอง', 'อุทัยธานี']
east = ['จันทบุรี', 'ฉะเชิงเทรา', 'ชลบุรี', 'ตราด', 'ปราจีนบุรี', 'ระยอง', 'สระแก้ว']
west = ['กาญจนบุรี', 'ตาก', 'ประจวบคีรีขันธ์', 'เพชรบุรี', 'ราชบุรี']
south = ['กระบี่', 'ชุมพร', 'ตรัง', 'นครศรีธรรมราช', 'นราธิวาส', 'ปัตตานี', 'พังงา', 'พัทลุง', 'ภูเก็ต', 'ระนอง', 'สตูล', 'สงขลา', 'สุราษฎร์ธานี', 'ยะลา']

cities = df.จังหวัด
city_north = 0
city_northeast = 0
city_middle = 0
city_east = 0
city_west = 0
city_south = 0
for city in cities:
    if city in north:
        city_north += 1
    elif city in northeast:
        city_northeast += 1
    elif city in middle:
        city_middle += 1
    elif city in east:
        city_east += 1
    elif city in west:
        city_west += 1
    elif city in south:
        city_south += 1
line = pygal.Bar()
line.title = "จำนวนครั้งของอุบัติเหตุในแต่ละภาค"
line.x_labels = ("ภาคเหนือ", "ภาคอีสาน", "ภาคกลาง", "ภาคตะวันออก", "ภาคตะวันตก", "ภาคใต้")
line.add("accident", [city_north, city_northeast, city_middle, city_east, city_west, city_south])
line.render_to_file("test.svg")
