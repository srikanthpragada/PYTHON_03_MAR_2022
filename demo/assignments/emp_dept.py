data = ["IT,Neil", "IT,Jack", "FI,Mark", "MK,Andy", "MK,Joe", "IT,Jason"]
depts = {}

for entry in data:
    dname, empname = entry.split(",")
    emps = depts.get(dname, [])
    emps.append(empname)
    if len(emps) == 1:
       depts[dname] = emps

for dname, emps in sorted(depts.items()):
     print(f'{dname:10} - {",".join(emps)}')

