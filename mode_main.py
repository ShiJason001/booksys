import mode_users
import mode_books
from flask import Flask, redirect, request, render_template, url_for
import mode_cookies

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/user_login')

@app.route('/user_login', methods=['POST', 'GET'])
def user_login():
    if request.method == "GET":
        return "方法错误"
        # return render_template('user_login')
    elif request.method == "POST":
        data = request.json
        username = data['username']
        password = data['password']
        check_msg = mode_users.check(username, password)
        print(check_msg)
        if check_msg is None:
            return render_template('/user_login')
        else:
            retcode = 200
            mode_cookies.set_cookies(username, "success")
            c1 = mode_cookies.get_cookies(username)
            print(c1)
            return "登录成功", retcode, {"cookies": c1}

            # return render_template(url_for(user_index))

@app.route('/user_index')
def user_index():
    return "Welcome"


if __name__ == "__main__":
    app.run()
