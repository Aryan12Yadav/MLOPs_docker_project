from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
 
<head>
    <h2>Enter Your Name:</h2>
    <form action="/greet" method="post">
        <input type="text" name="username" placeholder="Your name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

'''





@app.route('/greet',methods = ['POST'])
def greet():
    user_input = request.form['username']
    return f"Hello {user_input}, Welcome to th is app for Docker demonstration"

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000)


