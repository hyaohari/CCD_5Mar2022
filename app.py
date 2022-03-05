#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask
app = Flask(__name__)


# In[8]:


from flask import render_template, request
import joblib
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        income = float(income)
        age = float(age)
        loan = float(loan)
        print(income, age, loan)
        
        model1 = joblib.load("CCD_DT")
        pred1 = model1.predict([[income, age, loan]])
        if pred1 == 0:
            decision = "No"
        else:
            decision = "Yes"
        s1 = "The predicted credit card default based on Decision Tree is " + decision
        
        model2 = joblib.load("CCD_Reg")
        pred2 = model2.predict([[income, age, loan]])
        if pred2 == 0:
            decision = "No"
        else:
            decision = "Yes"
        s2 = "The predicted credit card default based on Linear Regression is " + decision
        
        model3 = joblib.load("CCD_NN")
        pred3 = model3.predict([[income, age, loan]])
        if pred3 == 0:
            decision = "No"
        else:
            decision = "Yes"
        s3 = "The predicted credit card default based on Neural Network is " + decision
        
        model4 = joblib.load("CCD_RF")
        pred4 = model4.predict([[income, age, loan]])
        if pred4 == 0:
            decision = "No"
        else:
            decision = "Yes"
        s4 = "The predicted credit card default based on Random Forest is " + decision
        
        model5 = joblib.load("CCD_GB")
        pred5 = model5.predict([[income, age, loan]])
        if pred5 == 0:
            decision = "No"
        else:
            decision = "Yes"
        s5 = "The predicted credit card default based on Gradient Boosting is " + decision
        
        return(render_template("index.html", result1=s1, result2=s2, result3=s3, result4=s4, result5=s5))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2", result4="2", result5="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




