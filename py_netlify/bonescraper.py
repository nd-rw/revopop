#import sqlite3
# add postgres api libraries here

def create_sqlite_event_query(event, table_name):
    # TODO hard-coded to revo fitness event length, re-write to be more generic
    cols = list(event.keys())
    query = F"INSERT INTO {table_name} VALUES ('{event[cols[0]]}', {event[cols[1]]}, {event[cols[2]]})"
    return query

def update_sqlite(update_query):
    # TODO hard-coded, add db_location paramgeter to input
    conn = sqlite3.connect('revopop.db')
    cur = conn.cursor()
    cur.execute(update_query)
    conn.commit()
    conn.close()

def print_sqlite_rows():
    # TODO hard-coded gym_population, make function more generic
    conn = sqlite3.connect('revopop.db')
    cur = conn.cursor()
    cur.execute("select * from gym_population")
    sqlite_reponse = cur.fetchall()
    print(sqlite_reponse)
    conn.close()