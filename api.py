from fastapi import FastAPI
import pandas as pd
import json


file=open('data.json')
data=json.load(file)
file.close()

msg_format="University Roll No/EXAMINATION ROLL NO: {1}\nCourse: {2}\nStream: {3}\nCollege: {4}\nUniversity: {4}\nFirst Name: {5}\nMiddle Name: {6}\nLast Name: {7}\nFull Name: {8}\nGender: {9}\nDAY (D.O.B): {10}\nMONTH (D.O.B): {11}\nYEAR (D.O.B): {12}\nD.O.B: {13}\nMobile No: {14}\nAlternative Mobile No: {15}\nWhatsApp No: {16}\nEmail ID: {17}\nAlternative Email ID: {18}\nFather / Mother 's Name: {19}\nFather / Mother 's Mobile No: {20}\nFather / Mother 's Email ID: {21}\nClass 10th School Name: {22}\nB.Tech 1st Sem CGPA: {23}\nB.Tech 2nd Sem CGPA: {24}\nB.Tech 3rd Sem CGPA: {25}\nB.Tech 4th Sem CGPA: {26}\nB.Tech 5th Sem CGPA: {27}\nAVG CGPA: {28}\nPresent Address: {29}\nCity: {30}\nState: {31}\nPin No: {32}\nCountry: {33}\nPermanent Address: {34}\nCity: {34}\nState: {35}\nPin No: {36}\nCountry: {37}\nPAN No: {39}\nAADHAR No: {40}\nVOTER ID: {41}\nPASSPORT No: {42}\nEmail Address: {43}\n"

app=FastAPI()
#================================================= (F U N C T I O N S) ====================================================




#================================================== (R O U T E S) ========================================================
@app.get("/")
def home():
    return "Greetings! Welcome to the database"

@app.get("/student/id/{enrollment_id}")
def get_stud(enrollment_id:int):
    flag=False
    for stud in data:
        if stud['id']==enrollment_id:
            flag=True
            student=stud
            break

    if flag==False:
        return "data for refered uni id does not exist"  
    return student

@app.get("/student/email/{email}")
def searchByEmailId(email):
    flag=False
    for stud in data:
        if stud['emailid']==email.lower() or stud['emailid']==email.upper():
            flag=True
            student=stud
            break

    if flag==False:
        return "data for refered email id does not exist"  
    return student

@app.get("/student/name/{name}")
def searchByName(name):
    students=[]
    flag=False
    for stud in data:
        tempName=stud['fullname']
        tempName=tempName.lower()
        if tempName.find(name.lower())>=0 or tempName.find(name.upper())>=0:
            students.append(stud)
            flag=True
    if flag==False:
        return "data for refered email id does not exist"
    return students











