# Load data from JSON file to DB

import sqlite3
import json
import dbutil

f = open("newemployees.json", "rt")
employees = json.load(f)    # Convert array of JSON objects to list of dict

con = sqlite3.connect(dbutil.DBNAME)
cur = con.cursor()
count = 0
for emp in employees:
    try:
        # Check whether a row with the same data is already present
        cur.execute("select count(id) from employees where fullname = ? and job = ? and salary = ?",
                    (emp['name'], emp['job'], emp['salary']))
        count = cur.fetchone()[0]
        if count == 0:  # no employee found
            cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                  (emp['name'], emp['job'], emp['salary']))
            count += 1
    except Exception as ex:
        print("Error : ", ex)

con.commit()
cur.close()
con.close()
print(f"Inserted {count} employees")
