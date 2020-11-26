
# -*-coding:utf-8-*-
from flask import Flask, request, json
from datetime import datetime
import os

app = Flask(__name__)

commonResponse = {
    'version': '2.0',
    'resultCode': 'OK',
    'output': {}
}

def health_care_all(response, utteranceValue_year, utteranceValue_month, utteranceValue_day, utteranceValue_gender, str1, str2):

    from datetime import datetime

    now_year = datetime.today().year
    now_month = datetime.today().month
    now_day = datetime.today().day

    bornYear = int(utteranceValue_year)

    makeYear = now_year - int(utteranceValue_year)
    makeMonth = now_month - int(utteranceValue_month)
    makeDay = now_day - int(utteranceValue_day)
    if makeMonth > 0:
        makeYear += 1
    elif makeMonth == 0:
        if makeDay > 0:
            makeYear += 1
        elif makeDay == 0:
            makeYear += 1

    import sqlite3

    conn = sqlite3.connect("user.db")

    cur = conn.cursor()

    #datetime.today().hour += 9

    b = (datetime.today(), makeYear, utteranceValue_gender)

    from datetime import datetime

    now = datetime.now()

    birth = datetime(int(utteranceValue_year), int(utteranceValue_month), int(utteranceValue_day), 0, 0, 0)  # (year, month, day, 0,0,0)

    time = now - birth

    print("생후", time.days, "일")

    bornmonth = round(time.days / 30)

    print("생후", bornmonth, "개월")

    cur.executemany(
        'INSERT INTO user_data VALUES (?,?,?)', [b]
    )

    conn.commit()

    cur.execute("select * from user_data")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()

    print(now_year)
    print(now_month)
    print(now_day)

    response['output']['count_calc'] = makeYear

    a = ''
    count = 0

    if bornYear % 2 == 0 and makeYear >= 20:
        a += '일반 건강 검진, '
        count += 1
    if makeYear >= 40:
        a += '위암 검진, '
        count += 1
    if makeYear >= 50:
        a += '대장암 검진, '
        count += 1
    if makeYear >= 40:
        a += '간암 검진, '
        count += 1
    if makeYear >= 40 and utteranceValue_gender == '여자':
        a += '유방암 검진,'
        count += 1
    if makeYear >= 20 and utteranceValue_gender == '여자':
        a += '자궁경부암 검진, '
        count += 1
    if 54 <= makeYear <= 74:
        a += '폐암 검진, '
        count += 1
    if 4 <= bornmonth <= 6:
        a += '1차 영유아 건강검진  '
        count += 1
    if 9 <= bornmonth <= 12:
        a += '2차 영유아 건강검진  '
        count += 1
    if 18 <= bornmonth <= 24:
        a += '3차 영유아 건강검진  '
        count += 1
    if 30 <= bornmonth <= 36:
        a += '4차 영유아 건강검진  '
        count += 1
    if 42 <= bornmonth <= 48:
        a += '5차 영유아 건강검진  '
        count += 1
    if 54 <= bornmonth <= 60:
        a += '6차 영유아 건강검진  '
        count += 1
    if 66 <= bornmonth <= 71:
        a += '7차 영유아 건강검진  '
        count += 1
    if a == '':
        a += '없습니다.'
    if count >= 1:
        a = a[0:len(a)-2]

    print(a)

    response['output'][str1] = a
    response['output'][str2] = str(count)



    return response

def getUtteranceParameter():
    data = request.get_json()  # 제이슨을 받아서 배열 형태로 저장해준다.
    return data['action']['parameters']


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/info', methods=['POST'])
def info():
    data = request.get_json()
    print
    data['test']
    response = commonResponse
    response['output']['name'] = 'napier'
    return json.dumps(response)


@app.route('/health_care_start', methods=['POST'])
def health_care_start():
    utteranceParameter = getUtteranceParameter()
    utteranceValue_year = utteranceParameter['takeyear']['value']
    utteranceValue_month = utteranceParameter['takemonth']['value']
    utteranceValue_day = utteranceParameter['takeday']['value']
    utteranceValue_gender = utteranceParameter['takegender']['value']

    response = commonResponse

    print(utteranceValue_year)
    print(utteranceValue_gender)

    response = health_care_all(response, utteranceValue_year, utteranceValue_month, utteranceValue_day, utteranceValue_gender, 'health_care', 'count_calc')


    return json.dumps(response)

@app.route('/health_care_exp', methods=['POST'])
def health_care_multi_turn():
    utteranceParameter = getUtteranceParameter()
    utteranceValue_year = utteranceParameter['takeyear1']['value']
    utteranceValue_month = utteranceParameter['takemonth1']['value']
    utteranceValue_day = utteranceParameter['takeday1']['value']
    utteranceValue_gender = utteranceParameter['takegender1']['value']

    response = commonResponse

    print(utteranceValue_year)
    print(utteranceValue_gender)

    response = health_care_all(response, utteranceValue_year, utteranceValue_month, utteranceValue_day, utteranceValue_gender, 'health_care1', 'count1')


    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

