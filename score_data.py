import sqlite3

db = sqlite3.connect(":memory:")
cur = db.cursor()
cur.execute('CREATE TABLE players(name text, score int)')

def enter_row(name, score):
    try:
        with db:
            cur.execute("insert into players values (?, ?)", (name, score))
            return True
    except Exception as why:
        return False


def return_row():
    try:
        with db:
            cur.execute('SELECT * FROM players ORDER BY score')
            sorted_scores = cur.fetchall()
            return sorted_scores
    except Exception as why:
        return False

def delete_scores():
    try:
        with db:
            cur.execute('DELETE FROM players')
            return True
    except Exception as why:
        return False