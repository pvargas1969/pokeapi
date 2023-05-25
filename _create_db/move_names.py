import pandas as pd

df = pd.read_csv("../data/v2/csv/move_names.csv")

# df['power'] = df['power'].fillna(0) 
# df['power'] = df['power'].astype('Int64')


print(df)
#print(df.columns)
#print(df.size, df.shape)
fils, cols = df.shape
#print(fils, cols)

print(df.info())
#print(df.describe())

columnas = df.columns

# ftabla = open("sqls/move_names_tabla.sql", "w")
# ftabla.write("USE POKEAPI\nGO\n\nCREATE TABLE move_names\n")
# ftabla.write("    (\n")
# for nom_col in columnas:
#     ftabla.write(" " * 4 + nom_col.ljust(20," ") + "Integer not null,\n")
# ftabla.write("    )\n")
# ftabla.write("GO\n")
# ftabla.close()

#print(df)

fdata = open("sqls/move_names_data.sql", "w", encoding='UTF-8')

fdata.write("USE POKEAPI\nGO\n\n")
fdata.write("TRUNCATE TABLE [move_names]\nGO\n\n")

for fil in range(fils):
# # # #     #print(fil, end=" ")
    if (df["local_language_id"][fil] in (5,6,7,8,9)):
        stLinea = "INSERT [move_names] VALUES ("
        for col in range(cols):
            nom_col = columnas[col]
# #     # #         #print(fil, nom_col, df[nom_col][fil])
# #     # #         #print(df[nom_col][fil], end=" ")
            if col == 2:
                stLinea += "'" + (df[nom_col][fil]).title() + "')"
#             elif col == 14:
#             stLinea += str(df[nom_col][fil]).strip() + ")"
            else:
# #     # # #             #if (df[nom_col][fil]).isnull:
# #     # # #             #    stLinea += "0, "
# #     # # #             #else:
                stLinea += str(df[nom_col][fil]).strip() + ", "

        print(stLinea)
        fdata.write(stLinea + "\n")

fdata.close()

# #print(df.info())
# #print(df.describe())
# #print(columnas)
# #for c in df.columns:
# #    print(c, df[c].dtype)
