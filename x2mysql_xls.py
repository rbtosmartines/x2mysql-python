import pandas as pd

from sqlalchemy import create_engine

from tkinter import filedialog

import config as cf
import sqlalchemy as sa

connstr = "mysql+pymysql://" + cf.db_user + ":" + cf.db_password + "@" + cf.db_host + ":" + cf.db_port + "/" + cf.db_database

engine = create_engine(connstr)

def nomarq (xyz):
    for filename in xyz:
        return(filename)

oriarq = filedialog.askopenfilenames(filetypes=[("Excel files",".xls")])
arq1 = nomarq(oriarq)
arq2 = arq1.split("/", -1)[-1]
arq2 = arq2.removesuffix('.xls')
arq2 = arq2.lower().replace('-','_')

xl = pd.ExcelFile(arq1)

rsl = open('result.txt', 'a')

for s in xl.sheet_names:
    df = pd.read_excel(arq1, s)
    tab = arq2 + "_" + s.strip()
    tab = tab.lower()
    df.to_sql(tab,con=engine,index=False,if_exists='replace')

    qtd = pd.read_sql(sa.text('SELECT count(*) FROM ' + tab),engine)
    xyz=qtd.values
    rows = str(xyz[0][0])
    rsl.write(arq1 + ' => ' + tab + ' ===> ' + rows + ' linhas.\n')

rsl.close()