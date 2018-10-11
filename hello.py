from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# funcName在路由中定义了，是路由下面试图函数中的变量
@app.route('/user/<funcName>')
def user(funcName):
    # pagename 是在user.html中使用的变量
    return render_template('user.html', pagename=funcName)

