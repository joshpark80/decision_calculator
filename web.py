from flask import Flask, render_template, flash, request
app = Flask(__name__)
 

@app.route('/', methods=['GET','POST'])
def index():
    saving = int(10000000)
    currentsaving = int(100000000)
    rate = float(6)
    age = int(35)
    retiringage = int(60)
    period = (retiringage)-(age)
    result = (saving)*(1+(rate)/1200)*(1-(1+(rate)/1200)**(period*12))/(1-(1+(rate)/1200))+(currentsaving)*((1+(rate)/100)**(period))
    saving=format(round(saving),',d')
    currentsaving=format(round(currentsaving),',d')
    result=format(round(result),',d')
    if request.method == 'POST':
        saving=request.form['saving']
        saving=int(saving)
        currentsaving=request.form['currentsaving']
        currentsaving=int(currentsaving)
        rate=request.form['rate']
        rate=float(rate)
        age=request.form['age']
        age=int(age.strip() or 0)
        retiringage=request.form['retiringage']
        retiringage=int(retiringage.strip() or 0)        
        print (saving, currentsaving, rate, age, retiringage)
        period=(retiringage)-(age)
        result=(saving)*(1+(rate)/1200)*(1-(1+(rate)/1200)**(period*12))/(1-(1+(rate)/1200))+(currentsaving)*((1+(rate)/100)**(period))
        saving=format(round(saving),',d')
        currentsaving=format(round(currentsaving),',d')
        result=format(round(result),',d')

    return render_template("index.html", saving=saving, currentsaving=currentsaving, rate=rate, result=result, age=age, retiringage=retiringage, period=period)

 
if __name__ == "__main__":
    app.run(debug = True)