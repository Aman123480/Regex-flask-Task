#step -1 import
from flask import Flask,render_template,request
import re

app=Flask(__name__)

#step-2 routing the code

@app.route('/',methods=['POST','GET'])
def search():
    if request.method == 'POST':
        name=request.form["int_1"]
        regex=request.form["int_2"]
        x=re.findall(regex,name)
        y=len(x)
            
        return render_template('search.html',n=name,r=regex,x=x,y=y,)
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)