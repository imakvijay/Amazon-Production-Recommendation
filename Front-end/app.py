from flask import Flask


app = Flask(__name__)



@app.route('/index',  methods=['POST', 'GET'])
def home_page():
    return 'Hi'


if __name__ == "__main__":
    app.run()
