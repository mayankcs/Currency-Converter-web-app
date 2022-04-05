from flask import Flask, request, render_template
import exchange_rate

app=Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    result=''
    before=''
    if request.method == "POST":
        Source=request.form.get('Source').upper()
        Target=request.form.get('Target').upper()
        Amount=float(request.form.get('Amount'))
        #rate,date=exchange_rate.get_exchange_rate(Source,Target)
        rate,date=75.398089 ,'2022-04-05'
        result=rate*Amount
        
        before="%s %s =%s "%(Source,str(Amount),Target)
        print(before)
    return render_template("index.html",before=before,result=result)

if __name__=='__main__':
    app.run(debug=True)


