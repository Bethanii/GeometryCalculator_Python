from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route("/sayHello", methods=['POST'])
def move_forward():
    #Moving forward code
    message = "Moving Forward..."
    return render_template('sayHello.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)