"""
. any character
.* 0 or more char
.+ 1 or more char
? optional

^ start
$ end
"""
import sqlite3


DB = sqlite3.connect("movies.db")


def main():
    cur = DB.cursor()

    cur.execute("SELECT * FROM MOVIES")
    rows = cur.fetchone()
    print(rows)

    cur.close()
    DB.close()


if __name__ == "__main__":
    main()
