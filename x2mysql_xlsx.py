import pandas as pd

from sqlalchemy import create_engine, types

from tkinter import filedialog

engine = create_engine('mysql+pymysql://root:beta2020@localhost:3308/x2mysql') # enter your password and database names here

def nomarq (xyz):
    for filename in xyz:
        return(filename)

oriarq = filedialog.askopenfilenames(filetypes=[("Excel files",".xlsx")])
arq1 = nomarq(oriarq)
arq2 = arq1.split("/", -1)[-1]
arq2 = arq2.removesuffix('.xlsx')
arq2 = arq2.lower()

xl = pd.ExcelFile(arq1)

for s in xl.sheet_names:
    df = pd.read_excel(arq1, s)
    tab = arq2 + "_" + s.strip()
    tab = tab.lower()
    df.to_sql(tab,con=engine,index=False,if_exists='replace')
