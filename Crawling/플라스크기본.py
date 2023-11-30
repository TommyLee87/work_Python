from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, request
import requests
import json

app = Flask(__name__)

data = {
    'stations': ['강남역', '역삼역', '서울역'],
    'ridership': [1000, 800, 1200]
}

# GET 요청을 처리하는 라우터
@app.route('/api/data', methods=['GET'])
def get_data():
    resp = Response(json.dumps(data, ensure_ascii=False), mimetype='application/json; charset=utf-8')
    return resp
@app.route('/api/weather', methods=['GET'])
def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
    #HTTP GET 요청
    resp = requests.get(url)
    #HTTP 파싱
    soup = BeautifulSoup(resp.text, "html.parser")
    output = ''
    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"

    return output

@app.route('/api/query', methods=['GET'])
def get_query():
    output = ""
    item_type = request.args.get('type', default=None, type=None)
    item_color = request.args.get('color', default=None, type=None)
    output += f"<h1>{item_type}</h1>"
    output += f"<h1>{item_color}</h1>"
    return output

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)