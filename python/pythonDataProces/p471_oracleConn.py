import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="/Users/kim-incheol/OracleXE/instantclient_19_8")
conn = None
cur = None

try:
    loginfo = 'hr/1234@192.168.1.192:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    print(type(conn))

    cur = conn.cursor()
    print(type(cur))

    sql = 'select power(2,10) from dual'
    cur.execute(sql)

    for item in cur:
        print(item)

except Exception as err:
    print(err)

finally:
    if cur != None:
        cur.close()

    if conn != None:
        conn.close()

print('fin')