from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student/<int:student_id>/<name>/<year>/<labstatus>')
def display_student(student_id, name,year,labstatus):
    return render_template('student.html', student_id=student_id, name = student.name ,year=student.year, labstatus= student.finished_lab)

app.run(debug=True)
