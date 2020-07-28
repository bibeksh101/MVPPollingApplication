import sqlite3
connection = sqlite3.connect("data.db")

###########################################################################

# CREATE TABLES
CREATE_PLAYERS_TABLE = """CREATE TABLE IF NOT EXISTS players (
    username TEXT PRIMARY KEY,
    voted BOOLEAN
);"""

CREATE_VOTES_TABLE = """CREATE TABLE IF NOT EXISTS votes (
    user_username TEXT,
    mvp_vote INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username)
);"""


def create_tables():
    with connection:
        connection.execute(CREATE_PLAYERS_TABLE)
        connection.execute(CREATE_VOTES_TABLE)


###########################################################################

# KEYBOARD INPUT = 3
# SORT BY VOTE COUNT AND RETURN IT
# PARAM: NONE
# RETURNS: FETCHES ALL MVP CANDIDATES
SHOW_MVP = """SELECT mvp_vote AS "NAMES" , COUNT(*) AS "Final Count"
FROM votes
GROUP BY mvp_vote
HAVING COUNT(*) >= 1
ORDER BY COUNT(*) DESC
LIMIT 10;"""


def show_mvp():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SHOW_MVP)
        return cursor.fetchall()


###########################################################################

# KEYBOARD INPUT = 4
# FINDS OUT WHO VOTED FOR A PARTICULAR MVP CANDIDATE
# PARAM: none
# RETURNS: DATABASE OF SEARCHED MVP CANDIDATE
WHO_VOTED_FOR_MVP = "SELECT * FROM votes WHERE mvp_vote LIKE ?"


def who_voted_for_mvp(search_player):
    with connection:
        cursor = connection.cursor()
        cursor.execute(WHO_VOTED_FOR_MVP, (f"%{search_player}%",))
        return cursor.fetchall()


###########################################################################

# KEYBOARD INPUT = 5
# ADDS MVP VOTES FOR PLAYER
# PARAM: NONE
# RETURNS: none

def check_valid_voter(name):
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM players')
        check_username = cursor.fetchall()
        for username in check_username:
            if name.lower() == username[0].lower() and username[1] is None:
                return True
        return False


UPDATE_VOTE = """UPDATE players
set voted = true
WHERE username = ?"""

INSERT_VOTES = "INSERT INTO votes (user_username, mvp_vote) VALUES (?, ?)"


def player_vote(username, mvp_vote):
    with connection:
        connection.execute(INSERT_VOTES, (username, mvp_vote))


def add_user(username):
    with connection:
        cursor = connection.cursor()

        if check_valid_voter(username):
            print("User exists and has not Voted yet!")
            vote_for_mvp = input("Vote For: ")
            player_vote(username, vote_for_mvp)
            cursor.execute(UPDATE_VOTE, (username,))
            print(f"---- Thank you for your vote {username}.----")
            print()

        else:
            print("User Does not exists or has already voted!")
            print()

###########################################################################
