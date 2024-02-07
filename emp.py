import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.title("Employee Management System")
choice=st.sidebar.selectbox("My Menu",("Home","Employee","Admin","new job"))
if(choice=="Home"):
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp9uv6wV-Iz9zviYxSCA9QFGNlTH1kM3aAkw&usqp=CAU")
    st.header("WELCOME")
    st.write("Hello This is an Application developed by Gouri Soni as a part of training of Project")
elif(choice=="Employee"):
    st.write("Employee login")
    if "login" not in st.session_state:
        st.session_state["login"]=False
    id=st.text_input("Enter Employee ID")
    password=st.text_input("Enter Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
        c=mydb.cursor()
        c.execute("select * from users")
        for row in c:
            if(row[0]==id and row[1]==password):
                st.session_state["login"]=True
                break
        if(st.session_state["login"]==False):
            st.subheader("Incorrect ID or Password")
    if(st.session_state["login"]==True):
        st.subheader("Login Successful")
        choice2=st.selectbox("Features",("None","Personal details","office details","salary"))
        if(choice2=="Personal details"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
            c=mydb.cursor()
            c.execute("select * from personal")
            l=[]
            for r in c:
                l.append(r)
            df=pd.DataFrame(data=l,columns=["Employee ID","Employee Name","City","birthdate","phone"])
            st.dataframe(df)
        elif(choice2=="office details"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
            c=mydb.cursor()
            c.execute("select * from office")
            l=[]
            for r in c:
                l.append(r)
            df=pd.DataFrame(data=l,columns=["Employee code","Name","Post","Joining","basicpay"])
            st.dataframe(df) 
        elif(choice2=="salary"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
            c=mydb.cursor()
            c.execute("select * from salary")
            l=[]
            for r in c:
                l.append(r)
            df=pd.DataFrame(data=l,columns=["Employee code","Name","Year","Month","Working day","final pay"])
            st.dataframe(df)
elif(choice=="Admin"):
    st.write("Admin login")
    if "alogin" not in st.session_state:
        st.session_state["alogin"]=False
    id=st.text_input("Enter Admin ID")
    password=st.text_input("Enter Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
        c=mydb.cursor()
        c.execute("select * from admin")
        for row in c:
            if(row[0]==id and row[1]==password):
                st.session_state["alogin"]=True
                break
        if(st.session_state["alogin"]==False):
            st.subheader("Incorrect ID or Password")
    if(st.session_state["alogin"]==True):
        st.subheader("Login Successful")
        choice2=st.selectbox("Features",("None","Employee personal detail","Add new employee","new Employee office detail","new employee salary"))
        if(choice2=="Employee personal detail"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
            c=mydb.cursor()
            c.execute(("select * from personal where Empid = ?"),(Empid))
            l=[]
            for r in c:
                l.append(r)
            df=pd.DataFrame(data=l,columns=["Employee Code","Employee Name","City","birthdate","phone"])
            st.dataframe(df)
        elif(choice2=="Add new employee"):
            Empid=st.text_input("Enter employee ID") 
            Name=st.text_input("Enter new emp name")
            City=st.text_input("Enter city")
            birthdate=st.text_input("Enter birth date")
            phone=st.text_input("Enter phone number")
           #empid=st.text_input("Enter employee ID")
            btn2=st.button("new emp Details added")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
                c=mydb.cursor()
                c.execute("Insert into personal values(%s,%s,%s,%s,%s)",(Empid,Name,City,birthdate,phone))
                mydb.commit()  
                st.header("New Employee details added successfully")
        elif(choice2=="new Employee office detail"):
            Ecode=st.text_input("Enter new emp code")
            name=st.text_input("Enter name")
            post=st.text_input("Enter post")
            joining=st.text_input("Enter joining date")
            basicpay=st.text_input("Enter basic pay")
           #empid=st.text_input("Enter employee ID")
            btn2=st.button("new emp office Details added")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
                c=mydb.cursor()
                c.execute("Insert into office values(%s,%s,%s,%s,%s)",(Ecode,name,post,joining,basicpay))
                mydb.commit()  
                st.header("New Employee details added successfully")
        elif(choice2=="new employee salary"):
            Ecode=st.text_input("Enter new emp code")
            name=st.text_input("Enter name")
            Year=st.text_input("Enter Year")
            Month=st.text_input("Enter Month")
            WorkingD=st.text_input("Enter Working day")
            Finalpay=st.text_input("Enter Final pay")
           #empid=st.text_input("Enter employee ID")
            btn2=st.button("new emp office Details added")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="Sonam$oni9",database="employee1")
                c=mydb.cursor()
                c.execute("Insert into salary values(%s,%s,%s,%s,%s,%s)",(Ecode,name,Year,Month,WorkingD,Finalpay))
                mydb.commit()  
                st.header("New Employee  added successfully")        
elif(choice=="new job"):
    st.title("Python")
    st.markdown('<iframe src="https://www.gyandata.com/jobdesc/Python-Lead-Dev.pdf" width="100%" height="500"></iframe>',unsafe_allow_html=True)
    st.markdown('<iframe src="https://cdn.nationalarchives.gov.uk/documents/senior-back-end-developer-python.pdf" width="100%" height="500"></iframe>',unsafe_allow_html=True)
    st.title("Java")
    st.markdown('<iframe src="https://www.payasia.asia/job/Java-Developer(Chennai,India).pdf" width="100%" height="500"></iframe>',unsafe_allow_html=True)
    st.markdown('<iframe src="https://gusec.edu.in/wp-content/uploads/2022/10/Job-Description_-Zyapaar.pdf" width="100%" height="500"></iframe>',unsafe_allow_html=True)
     