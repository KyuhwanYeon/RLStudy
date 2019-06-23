# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:52:57 2019

@author: Kyuhwan
"""
HEIGHT = 5  # 그리드월드 세로
WIDTH = 5  # 그리드월드 가로
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌표로 나타낸 행동
@staticmethod
def check_boundary(state):
    state[0] = (0 if state[0] < 0 else WIDTH - 1
                if state[0] > WIDTH - 1 else state[0])
    state[1] = (0 if state[1] < 0 else HEIGHT - 1
                if state[1] > HEIGHT - 1 else state[1])
    return state
def state_after_action(state, action_index):
    action = ACTIONS[action_index]
    return check_boundary([state[0] + action[0], state[1] + action[1]])

b= state_after_action([0,1],1)

#%%

(0 if state[0] < 0 else (WIDTH - 1 if state[0] > WIDTH - 1 else state[0]))

#%%

import tkinter as tk



root = tk.Tk()
canvas = tk.Canvas(root,width=200,height=200,bg="white")
canvas.grid()
firstRect = canvas.create_rectangle(50,0,100,100,fill="red")
secondRect = canvas.create_rectangle(5,5,15,15,fill="blue")
canvas.tag_raise(firstRect)

root.mainloop() #

