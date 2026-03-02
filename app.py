from flask import Flask, render_template

# สร้าง Instance ของ Flask
app = Flask(__name__)

# กำหนด Route (เส้นทาง) ของหน้าแรก
@app.route('/')
def home():
    return render_template('index.html')

# ส่วนสำหรับรัน Server
if __name__ == '__main__':
    # debug=True จะช่วยให้เวลาเราแก้โค้ด หน้าเว็บจะอัปเดตให้อัตโนมัติ
    app.run(debug=True, port=5000)