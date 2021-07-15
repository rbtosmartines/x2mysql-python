from tkinter.constants import X
import pandas as pd

from sqlalchemy import create_engine, types

from tkinter import filedialog

import config as cf

connstr = "mysql+pymysql://" + cf.db_user + ":" + cf.db_password + "@" + cf.db_host + ":" + cf.db_port + "/" + cf.db_database

engine = create_engine(connstr)

def nomarq (xyz):
    for filename in xyz:
        return(filename)

oriarq = filedialog.askopenfilenames(filetypes=[("Excel files",".csv")])
arq1 = nomarq(oriarq)
arq2 = arq1.split("/", -1)[-1]
arq2 = arq2.removesuffix('.csv')
arq2 = arq2.lower()

df = pd.read_csv(arq1,sep=';',quotechar='\'',encoding='utf8')
df.to_sql(arq2,con=engine,index=False,if_exists='replace')