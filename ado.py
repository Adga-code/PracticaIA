import src.database.connect as con

ado = con.getAll(con.getCollection("estadistica"))
odo = []
for i in ado:
    if i["acciones"] in odo:
        continue
    odo.append(i["acciones"])

for i in odo:
    print("\n=============================")
    print(i)
    print("")