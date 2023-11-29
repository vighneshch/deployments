
import streamlit as st
import pickle
import pandas as pd
X_test = pd.DataFrame(columns = ['carat','depth','table','x','y','z'])

with open('diamonds_lr.pkl','rb') as file:
    model = pickle.load(file)

st.header('Diamond Price Prediction')

st.sidebar.header('Features')

carat = st.sidebar.slider('Select Carat for the diamond',min_value = 0.1,max_value = 6.0,step = 0.01)
depth = st.sidebar.slider('Select depth of the diamond',min_value = 43,max_value =80,step = 1 )
table = st.sidebar.slider('Select table of the diamond',min_value = 43,max_value =100,step = 1 )
x = st.sidebar.slider('Select x of the diamond',min_value = 0.0,max_value =11.0,step = 0.01 )
y = st.sidebar.slider('Select y of the diamond',min_value = 0.0,max_value =60.0,step = 0.1 )
z = st.sidebar.slider('Select z of the diamond',min_value = 0.0,max_value =32.0,step = 0.1 )

X_test.loc[len(X_test)] = pd.Series({'carat':carat,'depth':depth,'table':table,'x':x,'y':y,'z':z})

st.write(X_test)

y_hat = model.predict(X_test)

st.write("The predicted price of diamond is :",y_hat)
