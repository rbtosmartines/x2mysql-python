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

oriarq = filedialog.askopenfilenames(filetypes=[("Excel files",".csv")])
arq1 = nomarq(oriarq)
arq2 = arq1.split("/", -1)[-1]
arq2 = arq2.removesuffix('.csv')
arq2 = arq2.lower().replace('-','_')

rsl = open('result.txt', 'a')
rsl.write(arq1 + ' => ' + arq2)

df = pd.read_csv(arq1,sep=';',quotechar='\'',encoding='utf8')
df.to_sql(arq2,con=engine,index=False,if_exists='replace')

qtd = pd.read_sql(sa.text('SELECT count(*) FROM ' + arq2),engine)
xyz=qtd.values
rows = str(xyz[0][0])

rsl.write(' ===> ' + rows + ' linhas.\n')
rsl.close()