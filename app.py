from flask import Response, Flask
from flask_cors import CORS
import schedule
import time
from routes.movie_api_handler import api_extract_info

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/movie_api', methods=['GET'])
def route_api_extract_info():
    result = api_extract_info()
    return Response(result, content_type='application/json; charset=utf-8')

def api_data_sending():
    print("API 정보 전송")
    api_extract_info()

#매일 정해진 시간에 동작 하도록 구현
schedule.every().day.at("12:30").do(api_data_sending)

if __name__ == '__main__':
    app.run(debug=True)

while True:
    schedule.run_pending()
    time.sleep(1)
