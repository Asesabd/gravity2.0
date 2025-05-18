from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Működik a webhook!'

@app.route('/gravity-webhook', methods=['POST'])
def gravity_webhook():
    adat = request.json
    print("Kapott adat:", adat)
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(debug=True)