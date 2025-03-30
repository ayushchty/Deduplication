import mysql.connector as mc
import pandas as pd
from fuzzywuzzy import fuzz
def word_match(df):
    for i in df.select_dtypes(include=['object']).columns:
        a=df[i].str.lower().unique()
        d={}
        for j in range(len(a)+1):
            for k in range(j+1,len(a)):
                score=fuzz.ratio(a[j],a[k])
                if score>=80:
                    d[a[k]]=a[j]
            df[i]=df[i].str.lower().replace(d)
    return df
class sql_2:
    def __init__(self):
        try:
            self.con=mc.connect(host="localhost",user="root",password="root",database="check1")
        except Exception as e:
            print(e)
    def file3(self):
        if self.con:
            df=pd.read_sql("select * from data1",self.con)
            self.con.close()
            return df
        else:
            return None

def file2():
    user_ip=input("Which file type do u wanna scan??(csv/json/sql/xlsx) ").lower()
    file=input("Enter the file name: ")
    # df = pd.DataFrame(data)
    if user_ip=="csv" and file.endswith(".csv"):
        df = pd.read_csv(file)
    elif user_ip=="xlsx" and file.endswith(".xlsx"):
        df = pd.read_excel(file)
    elif user_ip=="txt" and file.endswith(".txt"):
        df = pd.read_csv(file)
    elif user_ip=="json" and file.endswith(".json"):
        df=pd.read_json(file)
    elif user_ip=="sql":
        df=sql_2()
        df=df.file3()
    
    else:
        print("invalid file type")
    # df=pd.read_csv(file)
    df = word_match(df)
    if df.empty:
        print("file is empty")
    else:
        print ("file uploaded successfully")
        print("analyzing file")
        nulsum=df.isnull().sum()
        dupsum=df.duplicated().sum()
        print(f"file processed \n null:{nulsum} \n duplicate:{dupsum}")

        if dupsum>0:
            n=input("do you want to remove duplicates? (y/n)")
            if n=="y":
                df=df.drop_duplicates()
                print("file processed successfully")
        a=input("do u want to download it? (y/n)")
        if a=="y":
            df.to_csv("cleaned.csv",index=False)
            print("file downloaded successfully")
        else:
            print("file not downloaded")

# file2(input("Which file type do u wanna scan??(csv/json/sql/xlsx) ").lower(),"a.csv")
# file2()
# file2("mysql")
file2()