import database
import nbaplayers
import matplotlib.pyplot as plt
from basketball_reference_scraper.players import get_player_headshot

menu = """---- PLEASE SELECT AN OPTION ----
1)Import all Players\t 2)View MVP Candidates\t 3)Show Final Results\t 4)Who Voted for MVP\t 5)Vote Now\t 6) Exit\t INPUT: """


# KEYBOARD INPUT = 3
# SHOWS ALL THE MVP CANDIDATES & THEIR VOTE COUNT
# PARAM: ALL CANDIDATES
# RETURNS: PIE CHART AND PICTURE OF MVP (MOST VOTES)
def show_final_results(mvp_candidates):
    print("---- MVP CANDIDATES ----")
    name = []
    vote = []

    for mvp_candidate in mvp_candidates:
        print(f"\t {mvp_candidate[0]}: {mvp_candidate[1]}")
        name.append(mvp_candidate[0])
        vote.append(mvp_candidate[1])
    print("----")

    plt.pie(vote,
            labels=name,
            startangle=90,
            shadow=True,
            autopct='%1.1f%%')
    url = get_player_headshot(name[0])
    print(f"MVP {name[0]} Portrait: {url}")

    plt.title('MVP RESULTS!')
    plt.show()


# KEYBOARD INPUT = 4
# FINDS OUT WHO VOTED FOR A PARTICULAR MVP CANDIDATE
# PARAM: none
# RETURNS: DATABASE OF SEARCHED MVP CANDIDATE
def who_voted_for_mvp():
    search_term = input("Enter MVP candidate : ")
    return database.who_voted_for_mvp(search_term)


# KEYBOARD INPUT = 4
# PRINT WHO VOTED FOR A PARTICULAR MVP CANDIDATE
# PARAM: mvp_candidate
# RETURNS: none
def print_search_username_list(mvp_candidate):
    print(f"---Voters for {mvp_candidate[1][1]}---")
    voters_count = 0
    for name in mvp_candidate:
        print(f"\t{name[0]}")
        voters_count += 1
    print(f"---{voters_count} Voters Total---")
    print()


# KEYBOARD INPUT = 5
# ADDS MVP VOTES FOR PLAYER
# PARAM: NONE
# RETURNS: none
def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


###########################################################################
# CREATE 2 TABLES
database.create_tables()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        nbaplayers.add_all_players()

    elif user_input == "2":
        nbaplayers.view_mvp_candidates()

    elif user_input == "3":
        view_mvp = database.show_mvp()
        show_final_results(view_mvp)

    elif user_input == "4":
        mvp_voter = who_voted_for_mvp()
        if mvp_voter:
            print_search_username_list(mvp_voter)
        else:
            print(f"No Such Player --{mvp_voter}-- found!")
            print()

    elif user_input == "5":
        prompt_add_user()

    else:
        print("Invalid input, please try again!")
