from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure DB
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_pwd']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])   # route decorator
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        date = userDetails['date']
        print(date)
        print(type(date))
        return 'success'
    
    return render_template('index.html')

@app.route('/executeQuery', methods=['GET', 'POST'])
def execute():
    if request.method == 'POST':
        req = request.form
        query = req['query']
        cur = mysql.connection.cursor()

        resultValue = cur.execute(query)
        if resultValue > 0:
            table = cur.fetchall()
            data = [query, table]
            return render_template('executeQuery.html', data = data)
    # else:
        # return render_template('executeQuery.html')
        # mysql.connection.commit()
        # cur.close()
    data = []
    return render_template('executeQuery.html', data = data)
    
@app.route('/attendanceOnDate', methods=['GET', 'POST'])
def dateQuery():
    if request.method == 'POST':
        req = request.form
        date = req['date']
        cur = mysql.connection.cursor()

        resultValue = cur.execute("SELECT * FROM attendance where adate = %s;", [date])
        if resultValue > 0:
            table = cur.fetchall()
            data = [date, table]
            return render_template('dataForDate.html', data = data)
    
    data = []
    return render_template('dataForDate.html', data = data)

@app.route('/addStudent', methods=['GET', 'POST'])
def addStd():
    if request.method == 'POST':
        studDetails = request.form
        sid = studDetails['sid']
        tid = studDetails['tid']
        sname = studDetails['sname']
        clas = studDetails['class']
        section = studDetails['section']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student(sid, tid, sname, class, section) VALUES(%s, %s, %s, %s, %s)", (sid, tid, sname, clas, section))
        mysql.connection.commit()
        cur.close()
        # return redirect('/display')
    
    return render_template('addStudent.html')

@app.route('/addAttendance', methods=['GET', 'POST'])
def addAttend():
    if request.method == 'POST':
        attendDetails = request.form
        sid = attendDetails['sid']
        tid = attendDetails['tid']
        date = attendDetails['date']
        status = attendDetails['status']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO attendance(sid, tid, adate, apresent) VALUES(%s, %s, %s, %s)", (sid, tid, date, status))
        mysql.connection.commit()
        cur.close()
    
    return render_template('addAttendance.html')

@app.route('/addTeacher', methods=['GET', 'POST'])
def addTeach():
    if request.method == 'POST':
        teachDetails = request.form
        tid = teachDetails['tid']
        name = teachDetails['name']
        course = teachDetails['course']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO teacher(tid, tname, course) VALUES(%s, %s, %s)", (tid, name, course))
        mysql.connection.commit()
        cur.close()
        # return redirect('/display')
    
    return render_template('addTeacher.html')

# @app.route('/display')
# def disp():
#     cur = mysql.connection.cursor()
#     sid = '200'
#     resultValue = cur.execute("SELECT * FROM student NATURAL JOIN attendance WHERE sid LIKE %s", [sid])
#     if resultValue > 0:
#         data = cur.fetchall()
#         return render_template('stdData.html', data=data)
    
#     data = []
#     return render_template('stdData.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)