from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login(): return render_template('login.html')

@app.route('/register')
def register(): return render_template('register.html')

@app.route('/dashboard')
def dashboard(): return render_template('dashboard.html')

# 2.1.1 ข้อมูลผู้ใช้
@app.route('/profile')
def profile(): return render_template('profile.html')

# 2.1.2 ประวัติการใส่ข้อมูล
@app.route('/history')
def history(): return render_template('history.html')

# 2.3.1 รายชื่อนักเรียนในห้อง
@app.route('/students')
def student_list(): return render_template('student_list.html')

# 2.3.2 รายละเอียดนักเรียนรายบุคคล
@app.route('/student_detail')
def student_detail(): return render_template('student_detail.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)