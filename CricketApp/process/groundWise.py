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

def total_match(venue):
    df1 = matches.groupby(['Venue','Team1']).size().reset_index(name='TotalMatch')
    df2 = df1[df1['Venue']==venue]
    fig = px.bar(df2,x='Team1',y='TotalMatch',title="Total matches played by each team on "+venue)
    return fig.to_html()

def venue_won(venue):
    df1 = matches.groupby(['Venue','WinningTeam']).size().reset_index(name='TeamWon')
    df2 = df1[df1['Venue']==venue]
    fig = px.bar(df2,x='WinningTeam',y='TeamWon', title="Match won by each team on "+venue)
    return fig.to_html()


def check_loss(row):
        if row['Team1'] == row['WinningTeam']:
            row['losing_match'] = row['Team2']
            return row['Team2']
        else:
            row['losing_match'] = row['Team1']
            return row['Team1']

def venue_loss(venue):
    new_df = matches.loc[(matches.Venue==venue),['ID','Team1','Team2','WinningTeam','Venue']]
    new_df['losing_match'] = np.nan
    new_df['losing_match'] = new_df.apply(check_loss,axis=1)
    fig = px.bar(new_df.losing_match.value_counts(), title="Matches loss by each team on "+venue)
    return fig.to_html()

def toss_won(venue):
    df1 = matches.groupby(['Venue','TossWinner']).size().reset_index(name='TossWon')
    df2 = df1[df1['Venue']==venue]
    fig = px.bar(df2,x='TossWinner',y='TossWon', title="Toss won by each team on "+venue)
    return fig.to_html()

def check_loss1(row):
        if row['Team1'] == row['TossWinner']:
            row['losing_toss'] = row['Team2']
            return row['Team2']
        else:
            row['losing_match'] = row['Team1']
            return row['Team1']

def toss_loss(venue):
    new_df = matches.loc[(matches.Venue==venue),['ID','Team1','Team2','TossWinner','Venue']]
    new_df['losing_toss'] = np.nan
    new_df['losing_toss'] = new_df.apply(check_loss1,axis=1)
    fig = px.bar(new_df.losing_toss.value_counts(), title="Toss loss by each team on "+venue)
    return fig.to_html()