import pandas as pd

from sqlalchemy import create_engine, types

from tkinter import filedialog

import config as cf

connstr = "mysql+pymysql://" + cf.db_user + ":" + cf.db_password + "@" + cf.db_host + ":" + cf.db_port + "/" + cf.db_database

engine = create_engine(connstr)

def nomarq (xyz):
    for filename in xyz:
        return(filename)

oriarq = filedialog.askopenfilenames(filetypes=[("Excel files",".ods")])
arq1 = nomarq(oriarq)
arq2 = arq1.split("/", -1)[-1]
arq2 = arq2.removesuffix('.ods')
arq2 = arq2.lower()

xl = pd.ExcelFile(arq1)

for s in xl.sheet_names:
    df = pd.read_excel(arq1, s, engine = 'odf')
    tab = arq2 + "_" + s.strip()
    tab = tab.lower()
    df.to_sql(tab,con=engine,index=False,if_exists='replace')
