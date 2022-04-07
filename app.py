from flask import Flask, request, render_template
import exchange_rate

app=Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    result=''
    before=''
    msg=''
    if request.method == "POST":
        try:
            #Accept data from html form
            Source=request.form.get('Source').upper().rstrip()
            Target=request.form.get('Target').upper().rstrip()
            Amount=float(request.form.get('Amount'))
            if len(Source)!=3 or len(Target)!=3:
                msg="Please provide correct currency code "
                print(msg)
                return render_template("index.html",msg=msg)
            #fetching current exchange rate
            rate,date=exchange_rate.get_exchange_rate(Source,Target)
            result=rate*Amount

            before="%s %s =%s "%(Source,str(Amount),Target)
        except:
            msg="Please check the input data again"
        
    return render_template("index.html",msg=msg,before=before,result=result)

if __name__=='__main__':
    app.run(debug=False)


