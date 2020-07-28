from basketball_reference_scraper.teams import get_roster
from basketball_reference_scraper.players import get_stats, get_game_logs

import sqlite3
connection = sqlite3.connect("data.db")

teams = ['ATL', 'WAS', 'BOS']#, 'BRK', 'CHI', 'CHO', 'CLE',
         #'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         #'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL',
         #'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

# KEYBOARD INPUT = 1
# ADDS PLAYERS TO THE PLAYER TABLE
# PARAM: none
# RETURNS: ADDS Players and Voted (Boolean) to the "Players" Table
def add_all_players():
    with connection:
        cursor = connection.cursor()
        count = 0
        for team in teams:
            df = get_roster(team, 2020)
            index = 0
            for _ in df.PLAYER:
                name = df.PLAYER[index]
                cursor.execute('INSERT INTO players (username) VALUES (?)', (name,))
                index = index + 1
                count = count + 1
    print(f"{count} Players Imported to Database. Ready to Take Poll!")

# KEYBOARD INPUT = 2
# VIEW MVP CANDIDATES & THEIR STATISTICS
# PARAM: none
# RETURNS: SHOWS 2019/2020 GAME LOGS AND PLAYER SEASONAL STATS
def view_mvp_candidates():
    mvp_candidates = ['LeBron James',
                      'Giannis Antetokounmpo',
                      'James Harden',
                      'Anthony Davis',
                      'Kawhi Leonard',
                      'Jimmy Butler',
                      'Chris Paul']

    display_rank = 1
    for mvp_candidate in mvp_candidates:
        print(f"Our Ranking #{display_rank}: {mvp_candidate}")
        display_rank += 1

    print()
    mvp_candidate = input("Whose stats would like to see? ")
    # ADD Check Condition Here.
    # Loop if Player not one of the above.
    # Error when entry is 1.
    game_logs = get_game_logs(mvp_candidate, '2019-10-22', '2020-03-01', playoffs=False)
    game_stats = get_stats(mvp_candidate, stat_type='PER_GAME', playoffs=False, career=False)
    print(f"-----------{mvp_candidate}'s 2019-2020 GAME LOGS-----------")
    print(game_logs)
    print(f"-----------{mvp_candidate}'s CAREER GAME STATS-----------")
    print(game_stats)

