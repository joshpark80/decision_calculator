from flask import Flask, render_template, flash, request
app = Flask(__name__)
 

@app.route("/", methods=['POST'])
def index():
    text = request.form['text']
    result = text * 5
    return render_template('index.html', result=result)

 
if __name__ == "__main__":
    app.run(debug = True)