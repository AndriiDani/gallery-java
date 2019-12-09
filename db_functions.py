import sqlite3

with sqlite3.connect('z201.db', check_same_thread=False) as conn:
    cur = conn.cursor()

    def insert_time(val):
        sql = f"INSERT INTO time_counter VALUES ('{val}')"
        cur.execute(sql)
        conn.commit()

    def avarage_time():
        sql = "SELECT * FROM time_counter"
        cur.execute(sql)
        time_values = cur.fetchall()
        data = []
        for t in time_values:
            data.append(float(t[0]))
        return f"{sum(data)/len(data)}"
