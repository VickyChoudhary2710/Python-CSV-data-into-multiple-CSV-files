import pandas as pd

df = pd.read_csv('Data_File.csv')

d = {}
for name in df.Grade.unique():
    d[name] = pd.DataFrame()
for name in d:
    df_s={}
    for level in df.Grade.unique():
        df_s = df.loc[df.Grade == name]
        #print(d[name])
        df_s
    d[name] =df_s
    #print(name)
    #print(d[name])
    
print('File names:')
for name in d:
    df1 = d[name]
    file_name = df1['File_name'].unique()
    df1 = df1.drop('File_name',1)
    f = list(file_name)
    f = ','.join(f)
    print(f)
    df1.to_csv(f,index = False)    
