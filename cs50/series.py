import pandas as pd
import sqlite3

DB = sqlite3.connect("movies.db")


def main():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('series.csv')

    # Connect to SQLite database
    conn = sqlite3.connect('series.db')

    # Write DataFrame to SQLite database
    df.to_sql('series', conn, if_exists='replace', index=False)

    cursor = conn.cursor()

    # Execute a query to select all rows from the 'series' table
    cursor.execute("SELECT * FROM series")

    # Fetch all rows from the cursor
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
