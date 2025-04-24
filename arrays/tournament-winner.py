# Arrays (Tournament Winner)
# Given an array of competitions and an array of results, the task is to determine the winner of the tournament.
# A competition is represented by an array of two strings, the first one being the home team and the second one being the away team.
# The results array contains 1 if the home team wins and 0 if the away team wins.
# The winner of the tournament is the team with the most wins. If there is a tie, the team that appears first in the competitions array is the winner.
# The function tournament_winner takes two arguments: competitions and results.
# competitions is a list of lists, where each inner list contains two strings representing the home and away teams.
# results is a list of integers, where each integer represents the result of the corresponding competition in competitions.
# The function returns the name of the winning team as a string.
# The time complexity of this solution is O(n), where n is the number of competitions.
# The space complexity is O(k), where k is the number of unique teams in the competitions.

# Approach:
# 1. Initialize a dictionary to keep track of the scores of each team.
# 2. Initialize variables to keep track of the current best team and its score.
# 3. Iterate through the competitions and results arrays simultaneously.
# 4. For each competition, determine the winning team based on the result.
# 5. Update the score of the winning team by adding 3 points.
# 6. Check if the winning team's score is greater than the current best score.
# 7. If it is, update the current best team and its score.
# 8. After iterating through all competitions, return the name of the current best team.

def tournament_winner(competitions, results):
    current_best_team = ""
    scores ={}

    for idx, game in enumerate(competitions):
        result = results[idx]
        home_team, away_team = game

        winning_team = home_team if result == 1 else away_team
        updateScores(scores, winning_team, 3)

        if current_best_team == "" or scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team

    return current_best_team
    
def updateScores(scores, team, points):
    if team not in scores:
        scores[team] = 0
    scores[team] += points


competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]

print(tournament_winner(competitions, results)) 

