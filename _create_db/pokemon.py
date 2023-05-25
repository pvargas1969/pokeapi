import pandas as pd

df = pd.read_csv("../data/v2/csv/pokemon.csv")

#print(df)
#print(df.columns)
#print(df.size, df.shape)
fils, cols = df.shape
#print(fils, cols)

columnas = df.columns

ftabla = open("sqls/pokemon_tabla.sql", "w")

ftabla.write("CREATE TABLE pokemon\n")
ftabla.write("    (\n")
for nom_col in columnas:
    ftabla.write(" " * 4 + nom_col.ljust(20," ") + "Integer,\n")
ftabla.write("    )\n")
ftabla.write("GO\n")
ftabla.close()

df['base_experience'] = df['base_experience'].fillna(0)
df['base_experience'] = df['base_experience'].astype('Int64')

df['order'] = df['order'].fillna(0)
df['order'] = df['order'].astype('Int64')

fdata = open("sqls/pokemon_data.sql", "w")

for fil in range(fils):
    stLinea = "INSERT pokemon VALUES("
    #print(fil, end=" ")
    for col in range(cols):
        nom_col = columnas[col]
        #print(fil, nom_col, df[nom_col][fil])
        #print(df[nom_col][fil], end=" ")
        if col == 1:
            stLinea += "'" + (df[nom_col][fil]).title() + "', "
        elif col == 7:
            stLinea += str(df[nom_col][fil]).strip() + ")"
        else:
            #if (df[nom_col][fil]).isnull:
            #    stLinea += "0, "
            #else:
            stLinea += str(df[nom_col][fil]).strip() + ", "

    #print(stLinea)
    fdata.write(stLinea + "\n")

fdata.close()

#print(df.info())
#print(df.describe())
print(columnas)
for c in df.columns:
    print(c, df[c].dtype)
