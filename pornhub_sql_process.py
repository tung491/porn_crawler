import sqlite3
import json


def main():
    with open('pornhub.json') as f:
        items = json.loads(f.read())
    
    conn = sqlite3.connect('porn.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE pornhub (
    id INTEGER primary key,
    name VARCHAR,
    img_src VARCHAR,
    gender VARCHAR,
    born_date VARCHAR,
    birth_place VARCHAR,
    height int
    );''')
    for item in items:
        c.execute('''INSERT INTO pornhub(name, img_src, gender, born_date, birth_place, height)
        VALUES (?, ?, ?, ?, ?, ?)''', (item['name'], item['img_src'], item['gender'], item['born_date'], item['birth_place'], item['height'])
                  )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()