# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:34:45 2020

@author: Pooja
"""

''' Title : Tic Tac Toe game
Roll No :3946
'''

import numpy as np 
import random 
from time import sleep 


def create_board(): 
	return(np.array([[0, 0, 0], 
					[0, 0, 0], 
					[0, 0, 0]])) 


def possibilities(board): 
	l = [] 
	
	for i in range(len(board)): 
		for j in range(len(board)): 
			
			if board[i][j] == 0: 
				l.append((i, j)) 
	return(l) 

def random_place(board, player): 
	selection = possibilities(board) 
	current_loc = random.choice(selection) 
	board[current_loc] = player 
	return(board) 

def row_win(board, player): 
	for x in range(len(board)): 
		win = True
		
		for y in range(len(board)): 
			if board[x, y] != player: 
				win = False
				continue
				
		if win == True: 
			return(win) 
	return(win) 


def col_win(board, player): 
	for x in range(len(board)): 
		win = True
		
		for y in range(len(board)): 
			if board[y][x] != player: 
				win = False
				continue
				
		if win == True: 
			return(win) 
	return(win) 

 
def diag_win(board, player): 
	win = True
	
	for x in range(len(board)): 
		if board[x, x] != player: 
			win = False
	return(win) 


def check(board): 
	winner = 0
	
	for player in [1, 2]: 
		if (row_win(board, player) or
			col_win(board,player) or
			diag_win(board,player)): 
				
			winner = player 
			
	if np.all(board != 0) and winner == 0: 
		winner = -1
	return winner 


def start_game(): 
	game, winner, counter = create_board(), 0, 1
	print(game) 
	sleep(2) 
	
	while winner == 0: 
		for player in [1, 2]: 
			game = random_place(game, player) 
			print("Board after " + str(counter) + " move") 
			print(game) 
			sleep(2) 
			counter += 1
			winner = check(game) 
			if winner != 0: 
				break
	return(winner) 


print(" The winning player is: " + str(start_game())) 

'''
Output

[[0 0 0]
 [0 0 0]
 [0 0 0]]
Board after 1 move
[[0 0 0]
 [0 1 0]
 [0 0 0]]
Board after 2 move
[[0 0 0]
 [2 1 0]
 [0 0 0]]
Board after 3 move
[[0 0 0]
 [2 1 1]
 [0 0 0]]
Board after 4 move
[[0 0 0]
 [2 1 1]
 [0 0 2]]
Board after 5 move
[[0 0 1]
 [2 1 1]
 [0 0 2]]
Board after 6 move
[[0 0 1]
 [2 1 1]
 [2 0 2]]
Board after 7 move
[[0 0 1]
 [2 1 1]
 [2 1 2]]
Board after 8 move
[[2 0 1]
 [2 1 1]
 [2 1 2]]
Winner is: 2

runfile('C:/Users/Pooja/Desktop/joc/python/tictactoe.py', wdir='C:/Users/Pooja/Desktop/joc/python')
[[0 0 0]
 [0 0 0]
 [0 0 0]]
Board after 1 move
[[0 0 0]
 [0 0 0]
 [0 1 0]]
Board after 2 move
[[0 0 0]
 [2 0 0]
 [0 1 0]]
Board after 3 move
[[0 0 0]
 [2 0 0]
 [0 1 1]]
Board after 4 move
[[0 0 0]
 [2 0 0]
 [2 1 1]]
Board after 5 move
[[0 0 1]
 [2 0 0]
 [2 1 1]]
Board after 6 move
[[0 0 1]
 [2 0 2]
 [2 1 1]]
Board after 7 move
[[0 1 1]
 [2 0 2]
 [2 1 1]]
Board after 8 move
[[2 1 1]
 [2 0 2]
 [2 1 1]]
 The winning player is: 2

runfile('C:/Users/Pooja/Desktop/joc/python/tictactoe.py', wdir='C:/Users/Pooja/Desktop/joc/python')
[[0 0 0]
 [0 0 0]
 [0 0 0]]
Board after 1 move
[[0 1 0]
 [0 0 0]
 [0 0 0]]
Board after 2 move
[[0 1 0]
 [0 0 0]
 [0 0 2]]
Board after 3 move
[[0 1 0]
 [0 0 1]
 [0 0 2]]
Board after 4 move
[[0 1 0]
 [0 2 1]
 [0 0 2]]
Board after 5 move
[[0 1 1]
 [0 2 1]
 [0 0 2]]
Board after 6 move
[[0 1 1]
 [2 2 1]
 [0 0 2]]
Board after 7 move
[[1 1 1]
 [2 2 1]
 [0 0 2]]
 The winning player is: 1
 '''