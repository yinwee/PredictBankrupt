#!/usr/bin/env python
# coding: utf-8

# In[19]:


from flask import Flask


# In[20]:


app = Flask(__name__)


# In[21]:


from flask import request, render_template
from keras.models import load_model

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        NP_TA = request.form.get("NP_TA") 
        TL_TA = request.form.get("TL_TA")    
        WC_TA = request.form.get("WC_TA") 
        print(NP_TA, TL_TA, WC_TA) 
        model = load_model("BKRNN") 
        pred = model.predict([[float(NP_TA), float(TL_TA), float(WC_TA)]]) 
        print(pred) 
        pred = pred[0][0] 
        s = "Predicted Bankruptcy Score is " + str(pred) 
        return(render_template("index.html", result = s)) 
    else: 
        return(render_template("index.html", result = '2'))


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:




