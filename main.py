from operator import add as list_concat

def get_winner(board):
	"""
	Returns None if no winner. Otherwise, returns "X" or "O" as winner.
	"""

	winning_lines = get_winning_lines(board)
	for winning_line in winning_lines:
		winning_line_set = set(winning_line)
		if len(winning_line_set) == 1 and "" not in winning_line_set:
			return winning_line[0]
	return None

def get_winning_lines(board):
	N_ROWS = len(board)

	def get_horizontals():
		horizontal_winning_lines = []
		for i in range(N_ROWS):
			horizontal_winning_line = []
			for j in range(N_ROWS):
				horizontal_winning_line.append(board[i][j])
			horizontal_winning_lines.append(horizontal_winning_line)
		return horizontal_winning_lines

	def get_verticals():
		vertical_winning_lines = []
		for i in range(N_ROWS):
			vertical_winning_line = []
			for j in range(N_ROWS):
				vertical_winning_line.append(board[j][i])
			vertical_winning_lines.append(vertical_winning_line)
		return vertical_winning_lines

	def get_diagonals():
		diagonal_winning_lines = [[], []]

		""" top left to bottom right """
		for i in range(N_ROWS):
			diagonal_winning_lines[0].append(board[i][i])

		""" top right to bottom left """
		for i in range(N_ROWS):
			diagonal_winning_lines[1].append(board[i][N_ROWS - i])

		return diagonal_winning_lines


	winning_lines_fs = [get_horizontals, get_verticals, get_diagonals]
	return reduce(list_concat, [winning_lines_f() for winning_lines_f in winning_lines_fs])
