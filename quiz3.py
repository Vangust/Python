import requests
import json
import sqlite3

key = 'b0382a9da8d31051dd5eecdc220673dc'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format('Tbilisi', key)
r = requests.get(url)
print('Status Code:',r.status_code)
print(r.headers)
print(r.text)

res = r.json()

f = open('file.json','w')
json.dump(res, f, indent=4)
f.close()

a = res['weather'][0]['main']
b = res['weather'][0]['description']
print(a)
print(b)

conn = sqlite3.connect('data.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather
(id INTEGER PRIMARY KEY AUTOINCREMENT,
weather VARCHAR(20),
description VARCHAR(50))
''')
c.execute('INSERT INTO weather(weather, description) VALUES (?, ?)', (a, b))
conn.commit()
conn.close()
# პროგრამის გაშვებისას, პროგრამა ახლანდელ თბილისის ამინდს(და ამინდის აღწერილობას) ამატებს data.sqlite დატაბაიზში. მეტი ვერ მოვიფიქრე, ან დამეზარა, არ ვიცი.
# (ალბათ უფრო დამეზარა). ა ხო კიდე json ფაილის ინფორმაციასაც ინახავს, და რაგაცებს პრინტავს(ამინდს, მის აღწერას, სტატუსის კოდს...)
