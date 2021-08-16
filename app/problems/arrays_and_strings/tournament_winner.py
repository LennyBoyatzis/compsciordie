from typing import List
from collections import defaultdict

# n = number of competitions/games
# O(n) runtime
# O(n) space to maintain scores for n games

def tournament_winner(competitions: List[List[str]], results: List[int]) -> str:
    """Returns winner of a competition"""
	score_board = defaultdict(int)
	
	for idx, game in enumerate(competitions):
		home_team, away_team = game
		home_win = results[idx] == 1
		if home_win:
			score_board[home_team] += 3
		else:
			score_board[away_team] += 3
	
	winner = max(score_board.items(), key=lambda x: x[1])
	return winner[0]
