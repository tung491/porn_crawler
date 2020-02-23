import json
import sqlite3


def parse_items():
    with open('jav.json') as f:
        data = json.loads(f.read())
    return data


def main():
    conn = sqlite3.connect('porn.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE jav(
    id INTEGER primary key,
    model_name VARCHAR,
    img_src VARCHAR,
    born_date VARCHAR,
    blood VARCHAR,
    breast INTEGER,
    hips INTEGER,
    waist INTEGER,
    height INTEGER,
    model_style VARCHAR,
    video_classes VARCHAR,
    video_count INTEGER
            );''')
    items = parse_items()
    for item in items:
        item['model_style'] = ', '.join(item['model_style'])
        item['video_classes'] = ', '.join(item['video_classes'])
        c.execute('''
        INSERT INTO jav(model_name, img_src, born_date, blood, breast, hips, waist, height, model_style, video_classes, video_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', tuple(item.values()))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()