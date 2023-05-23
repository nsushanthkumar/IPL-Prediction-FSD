import csv
from turtle import color
from matplotlib.pyplot import title
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objs as go
from CricketProj.settings import STATIC_ROOT
csvPath2='CricketApp\static\CSV\Ball.csv'
csvPath1='CricketApp\static\CSV\match.csv'

matches=pd.read_csv(csvPath1)
balls=pd.read_csv(csvPath2)

def team1Name():
    l1 = list(matches["Team1"])
    l2 = list()
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2

def team2Name():
    l1 = list(matches["Team2"])
    l2 = list()
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2

def tossName():
    l1 = list(matches["TossWinner"])
    l2 = list()
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2

def venueName():
    l1 = list(matches["Venue"])
    l2 = list()
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2

def TossDecision():
    l1 = list(matches["TossDecision"])
    l2 = list()
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2

def predict_winner(team1,team2,tossWin):
    data = matches.loc[(matches.Team1==team1) & (matches.Team2==team2) & (matches.TossWinner==tossWin)]
    ans = data["WinningTeam"].mode()
    return "Match Winner Will be "+ans.to_string(index=False)

def predict_venue(team1,team2,venue):
    data = matches.loc[(matches.Team1==team1) & (matches.Team2==team2) & (matches.Venue==venue)]
    ans = data["WinningTeam"].mode()
    return "Match Winner Will be "+ans.to_string(index=False)+" on "+venue

def predict_decision(team):
    data = matches.loc[(matches.TossWinner==team)]
    ans = data["TossDecision"].mode()
    return "If "+team+" is Toss Winner then Toss Decision Will be "+ans.to_string(index=False)