from flask import Flask, request, render_template
import exchange_rate

app=Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    result=''
    before=''
    if request.method == "POST":
        #Accept data from html form
        Source=request.form.get('Source').upper()
        Target=request.form.get('Target').upper()
        Amount=float(request.form.get('Amount'))
        
        #fetching current exchange rate
        rate,date=exchange_rate.get_exchange_rate(Source,Target)
        result=rate*Amount
        
        before="%s %s =%s "%(Source,str(Amount),Target)
        print(before)
    return render_template("index.html",before=before,result=result)

if __name__=='__main__':
    app.run(debug=True)


