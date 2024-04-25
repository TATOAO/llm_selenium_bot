import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite, SQLite version: {sqlite3.version}")
    except Exception as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def drop_table_with_confirm(conn, table_name):

    drop_table_name = f"""
    DROP TABLE IF EXISTS {table_name};
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


def main():
    # SQL statement for creating a new table
    f = open('./message_history_table_schema.sql')
    sql_create_messages_table = ''.join(f.readlines())

    # Main execution
    db_file = "local.db"
    conn = create_connection(db_file)
    create_table(conn, sql_create_messages_table)
    conn.close()

if __name__ == "__main__":
    main()

