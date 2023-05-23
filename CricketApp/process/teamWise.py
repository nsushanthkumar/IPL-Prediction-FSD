from multiprocessing.managers import BaseListProxy
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objs as go

from CricketProj.settings import STATIC_ROOT
csvPath2='CricketApp\static\CSV\Ball.csv'
csvPath1='CricketApp\static\CSV\match.csv'
csvPath3 = 'CricketApp\static\CSV\Ball_match.csv'

balls=pd.read_csv(csvPath2)
matches=pd.read_csv(csvPath1)
ballMatch = pd.read_csv(csvPath3)

def team_match(team):
    df1 = ballMatch.groupby(['Season','Team1']).size().reset_index(name="Count")
    df2 = df1[df1['Team1']==team]
    fig = px.bar(df2,x='Season',y='Count', title="Total matches played by "+team)
    return fig.to_html()

def venue_match(team):
    df1 = matches.groupby(['Venue','Team1']).size().reset_index(name='Count')
    df2 = df1[df1['Team1']==team]
    fig = px.bar(df2,x='Venue',y='Count', title="Total matches played by "+team+" on all grounds")
    return fig.to_html()

def year_match(team):
    df1 = matches.groupby(['Season','WinningTeam']).size().reset_index(name='Count')
    df2 = df1[df1['WinningTeam']==team]
    fig = px.bar(df2,x='Season',y='Count', title="Total matches Won by "+team+" in all years")
    return fig.to_html()