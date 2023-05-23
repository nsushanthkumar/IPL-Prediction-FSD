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

def player_runs(batsman,year):
    runs = ballMatch[(ballMatch.Season==int(year)) & (ballMatch.batter==batsman)].batsman_run.sum()
    return "Total run of "+batsman+" in "+str(year)+" are "+str(runs)

def player_wickets(bowler,year):
    wickets = ballMatch[(ballMatch.Season==int(year)) & (ballMatch.bowler==bowler)].isWicketDelivery.sum()
    return "Total Wickets of "+bowler+" in "+str(year)+" are "+str(wickets)

def strike_rate(batsman,year):
    balls_faced = len(ballMatch[(ballMatch.batter==batsman) & (ballMatch.Season==int(year))].batsman_run)
    runs = ballMatch[(ballMatch.batter==batsman) & (ballMatch.Season==int(year))].batsman_run.sum()
    SR = (runs/balls_faced)*100
    return "Strike rate of "+batsman+" in "+str(year)+" is "+str(SR)

def total_match(year):
    df1 = matches.groupby(['Season','Team1']).size().reset_index(name='TotalMatch')
    df2 = df1[df1['Season']==int(year)]
    fig = px.bar(df2,x='Team1',y='TotalMatch',title="Total matches played by each team in "+str(year))
    return fig.to_html()

def team_won(year):
    df1 = matches.groupby(['Season','WinningTeam']).size().reset_index(name='TeamWon')
    df2 = df1[df1['Season']==int(year)]
    fig = px.bar(df2,x='WinningTeam',y='TeamWon',title="Matches won by each team in "+str(year))
    return fig.to_html()

def check_loss(row):
        if row['Team1'] == row['WinningTeam']:
            row['losing_match'] = row['Team2']
            return row['Team2']
        else:
            row['losing_match'] = row['Team1']
            return row['Team1']

def team_loss(year):
    new_df = matches.loc[(matches.Season==int(year)),['ID','Team1','Team2','WinningTeam','Season']]
    new_df['losing_match'] = np.nan
    new_df['losing_match'] = new_df.apply(check_loss,axis=1)
    fig = px.bar(new_df.losing_match.value_counts(), title="Matches loss by each team in "+str(year))
    return fig.to_html()

def toss_won(year):
    df1 = matches.groupby(['Season','TossWinner']).size().reset_index(name='TossWon')
    df2 = df1[df1['Season']==int(year)]
    fig = px.bar(df2,x='TossWinner',y='TossWon', title="Toss won by each team in "+str(year))
    return fig.to_html()

def check_loss1(row):
        if row['Team1'] == row['TossWinner']:
            row['losing_toss'] = row['Team2']
            return row['Team2']
        else:
            row['losing_toss'] = row['Team1']
            return row['Team1']

def toss_loss(year):
    new_df = matches.loc[(matches.Season==int(year)),['ID','Team1','Team2','TossWinner','Season']]
    new_df['losing_toss'] = np.nan
    new_df['losing_toss'] = new_df.apply(check_loss1,axis=1)
    fig = px.bar(new_df.losing_toss.value_counts(), title="Toss loss by each team in "+str(year))
    return fig.to_html()