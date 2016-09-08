from flask import *
from models import *
import datetime

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST', 'GET'])
def index():
    Counter.create(method=request.method, time=datetime.datetime.now())
    return render_template('index.html')

@app.route('/request-counter', methods=['GET'])
def counter():
    query = Counter.select(Counter.method, fn.COUNT(Counter.id).alias("number_of_request")).group_by(Counter.method)
    return render_template('table.html', query=query)


if __name__ == "__main__":
    app.run()
