"""
File: boggle.py
Name: Jeffrey Lin 2020/12
----------------------------------------
This program aim to find words that can be constructed from sequentially
adjacent letters from the 4×4 grid. “Adjacent” letters are those horizontally, vertically,
and diagonally neighbouring. Words must be at least four letters long, but may not use the same letter.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global Variable
dictionary = []
d = {}
row_list = []
num = 0
check = 0
ans_list = []


def main():
	"""
	find words that can be constructed from sequentially adjacent letters
	from the 4×4 grid. Words must be at least four letters long, but may not use the same letter.
	"""
	global d, num
	read_dictionary()
	input_boggle_letter()
	if check == 0:
		current_index = []
		for row, col in d:
			current_index.append((row, col))
			find_word(row, col, d, d[(row, col)], current_index)
			current_index.pop()
		print(f'There are {num} words in total.')


def input_boggle_letter():
	global row_list, check
	for i in range(4):
		row = input(str(i+1)+' row of letters: ').lower()
		if len(row) == 7:
			row_list = row.split()
			if len(row_list) == 4:
				for j in range(len(row_list)):
					d[(i, j)] = row_list[j]
		else:
			print('Illegal Input')
			check += 1
			break


def find_word(row, col, d, answer, current_index):
	"""
	:param row: int, the number of row
	:param col: int, the number of column
	:param d: dict{(int,int):str(row_character)}
	:param answer: the current answer string
	:param current_index: list[(int,int)] index list has be found
	"""
	global dictionary, num, ans_list
	if len(answer) >= 4:
		if answer in dictionary and answer not in ans_list:
			print(f'Found: "{answer}" ')
			ans_list.append(answer)
			num += 1
	if has_prefix(answer):
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				if 0 <= row + i < 4 and 0 <= col + j < 4:
					if (row+i, col+j) not in current_index:
						# choose
						current_index.append((row+i, col+j))
						find_word(row+i, col+j, d, answer+d[(row+i, col+j)], current_index)
						# un-choose
						current_index.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			dictionary.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global dictionary
	for voc in dictionary:
		if voc.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
