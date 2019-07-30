from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    print('here')
    return render_template('home.html')
    
    
@app.route('/student/<int:student_id>')
def display_student(student_id):
    print('wtf is this bs')
    return render_template('student.html', student_id = student_id) 

if __name__ == '__main__':
    app.run(debug=True)
