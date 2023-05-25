import pandas as pd

df = pd.read_csv("../data/v2/csv/type_names.csv")

#df['damage_class_id'] = df['damage_class_id'].fillna(0)
#df['damage_class_id'] = df['damage_class_id'].astype('Int64')

#df['order'] = df['order'].fillna(0)
#df['order'] = df['order'].astype('Int64')


print(df)
#print(df.columns)
#print(df.size, df.shape)
fils, cols = df.shape
#print(fils, cols)

print(df.info())
#print(df.describe())

columnas = df.columns

ftabla = open("sqls/type_names_tabla.sql", "w")
ftabla.write("CREATE TABLE type_names\n")
ftabla.write("    (\n")
for nom_col in columnas:
    ftabla.write(" " * 4 + nom_col.ljust(20," ") + "Integer not null,\n")
ftabla.write("    )\n")
ftabla.write("GO\n")
ftabla.close()

#print(df)

fdata = open("sqls/type_names_data.sql", "w")

for fil in range(fils):
    stLinea = "INSERT type_names VALUES("
# #     #print(fil, end=" ")
    if (df["local_language_id"][fil] in (5,6,7,8,9)):
        for col in range(cols):
            nom_col = columnas[col]
    # #         #print(fil, nom_col, df[nom_col][fil])
    # #         #print(df[nom_col][fil], end=" ")
            if col == 2:
                stLinea += "'" + (df[nom_col][fil]).title() + ")"
    #         elif col == 3:
    #             stLinea += str(df[nom_col][fil]).strip() + ")"
            else:
    # # #             #if (df[nom_col][fil]).isnull:
    # # #             #    stLinea += "0, "
    # # #             #else:
                stLinea += str(df[nom_col][fil]).strip() + ", "

        print(stLinea)
        fdata.write(stLinea + "\n")

fdata.close()

#print(df.info())
#print(df.describe())
#print(columnas)
#for c in df.columns:
#    print(c, df[c].dtype)
