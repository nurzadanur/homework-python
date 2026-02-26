import sqlite3


def create_connection():
    return sqlite3.connect("content_creators.db")


def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS creators (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        class_name TEXT NOT NULL,
        inheritance TEXT NOT NULL,
        live_from TEXT NOT NULL
    )
    """)


def clear_table(cursor):
    cursor.execute("DELETE FROM creators")


def insert_data(cursor):
    data = [
        ("GlowStreamer", "Streamer, Mutant", "Streamer"),
        ("ViralCyborg", "TikToker, Mutant", "TikToker"),
        ("DonateMage", "Streamer, TikToker", "Streamer")
    ]

    cursor.executemany("""
    INSERT INTO creators (class_name, inheritance, live_from)
    VALUES (?, ?, ?)
    """, data)


def show_data(cursor):
    cursor.execute("SELECT * FROM creators")
    rows = cursor.fetchall()

    print("\n=== DATABASE TABLE ===")
    print(f"{'ID':<5} {'Class':<15} {'Inheritance':<30} {'live() from':<15}")
    print("-" * 70)

    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<30} {row[3]:<15}")


def main():
    conn = create_connection()
    cursor = conn.cursor()

    create_table(cursor)
    clear_table(cursor)
    insert_data(cursor)

    conn.commit()

    show_data(cursor)

    conn.close()


if __name__ == "__main__":
    main()