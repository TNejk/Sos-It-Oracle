import oracledb
from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)
def get_credentials():
    with open('test_app/config.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            parsed = line.split('|')
            app.config['ORACLE_USER'] = parsed[1]
            app.config['ORACLE_PASSWORD'] = parsed[2]
            app.config['ORACLE_DNS'] = parsed[3]

def upload_data(data, connection, fetch=False):
    cursor = connection.cursor()
    try:
        if fetch:
            pass
        else:
            cursor.fetchall(data)
        connection.commit()
    except oracledb.Error as error:
        print(error)
        connection.rollback()

def connect_db():
    try:
        connection = oracledb.connect(app.config['ORACLE_USER'],app.config['ORACLE_PASSWORD'],app.config['ORACLE_DNS'])
        print("Connected to Oracle DB")
        return connection
    except Exception as e:
        print(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    connection = connect_db()
    print(connection)
    if request.method == 'POST':
        task_content = request.form['content']
        action = "INSERT INTO table_name (task_name, date_created) VALUES ('{}', '{}')".format(task_content, datetime.utcnow())
        upload_data(action, connection)

        return redirect('/')

    else:
        return render_template('index.html', tasks=[])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)