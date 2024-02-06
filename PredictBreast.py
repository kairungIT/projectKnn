import streamlit as st

st.image('./pic/Breast.jpg') # ข้อมูลรูปภาพตัวเอง
col1, col2 = st.columns(2)

with col1:
  st.header('การทำนายการเกิดโรคมะเร็งเต้านม') # ชื่อตัวเอง
  st.subheader('ชื่อ นศ.')
with col2:
  st.subheader('สาขาวิชาวิทยาการข้อมูล')
  st.subheader('คณะวิทยาศาสตร์และเทคโนโลยี')

  html_1 = """
<div style="background-color:#76D7C4;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>การทำนายข้อมูลโรคมะเร็งเต้านม</h4></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd
dt=pd.read_csv('./data/breastcancer.csv')
st.write(dt.head(10))
dt1 = dt['ClumpThickness'].mean()
dt2 = dt['UniformityofCellSize'].mean()
dt3 = dt['UniformityofCellShape'].mean()
dt4 = dt['MarginalAdhesion'].mean()
dt5 = dt['SingleEpithelialCellSize'].mean()
dt6 = dt['BareNuclei'].mean()
dt7 = dt['BlandChromatin'].mean()
dt8 = dt['NormalNucleoli'].mean()
dt9 = dt['Mitoses'].mean()

dx = [dt1, dt2, dt3, dt4,dt5,dt6,dt7,dt8,dt9]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4","d5","d6","d7","d8","d9"])
if st.button("show bar chart"):
    st.bar_chart(dx2)
    st.button("Not show bar chart")
else :
    st.button("Not show bar chart") 

html_2 = """
<div style="background-color:#FFBF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายการเป็นโรคมะเร็ง</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")   

inpt1 = st.number_input("กรุณาเลือกข้อมูล input1")
inpt2 = st.number_input("กรุณาเลือกข้อมูล input2")
inpt3 = st.number_input("กรุณาเลือกข้อมูล input3")
inpt4 = st.number_input("กรุณาเลือกข้อมูล input4")
inpt5 = st.number_input("กรุณาเลือกข้อมูล input5")
inpt6 = st.number_input("กรุณาเลือกข้อมูล input6")
inpt7 = st.number_input("กรุณาเลือกข้อมูล input7")
inpt8 = st.number_input("กรุณาเลือกข้อมูล input8")
inpt9 = st.number_input("กรุณาเลือกข้อมูล input9")

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

if st.button("ทำนายผล"):
   # ทำนาย
   #dt = pd.read_csv("./data/breastcancer.csv") 

   X = dt.iloc[:,1:11]
   y = dt.Class   

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)

    #ข้อมูล input สำหรับทดลองจำแนกข้อมูล
   x_input = np.array([[inpt1,inpt2,inpt3,inpt4,inpt5,inpt6,inpt7,inpt8,inpt9]])
    # เอา input ไปทดสอบ
   st.write(Knn_model.predict(x_input))
   out=Knn_model.predict(x_input)

   if out[0]=="2":
 #     st.image("./pic/iris1.jpg")
      st.header("ไม่เป็นมะเร็ง")
   else:
 #     st.image("./pic/iris3.jpg")  
      st.header("เป็นมะเร็ง")
   st.button("ไม่ทำนายผล")
else :
    st.button("ไม่ทำนายผล")

