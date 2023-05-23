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
ballMatch = pd.read_csv(csvPath3,low_memory=False)


def strike_rate1(batsman):
    balls_faced = len(ballMatch[(ballMatch.batter==batsman)].batsman_run)
    runs = ballMatch[ballMatch.batter==batsman].batsman_run.sum()
    SR = (runs/balls_faced)*100
    return "Strike rate of "+batsman+" is "+str(SR)

def strike_rate2(batsman,bowler):
    balls_faced = len(ballMatch[(ballMatch.batter==batsman) & (ballMatch.bowler==bowler)].batsman_run)
    runs = ballMatch[(ballMatch.batter==batsman) & (ballMatch.bowler==bowler)].batsman_run.sum()
    SR = (runs/balls_faced)*100
    return "Strike rate of "+batsman+" agaist "+bowler+" is "+str(SR)

def strike_rate3(year,batsman):
    balls_faced = len(ballMatch[(ballMatch.batter==batsman) & (ballMatch.Season==int(year))].batsman_run)
    runs = ballMatch[(ballMatch.batter==batsman) & (ballMatch.Season==int(year))].batsman_run.sum()
    SR = (runs/balls_faced)*100
    return "Strike rate of "+batsman+" in "+str(year)+" is "+str(SR)

def player_runs(batsman,year):
    runs = ballMatch[(ballMatch.Season==int(year)) & (ballMatch.batter==batsman)].batsman_run.sum()
    return "Total run of "+batsman+" in "+str(year)+" are "+str(runs)

def player_wickets(bowler,year):
    wickets = ballMatch[(ballMatch.Season==int(year)) & (ballMatch.bowler==bowler)].isWicketDelivery.sum()
    return "Total Wickets of "+bowler+" in "+str(year)+" are "+str(wickets)

# def year_runs(year,batsman):
#     df1 = ballMatch.groupby(['Season','batter','batsman_run']).size().reset_index(name='TotalRuns')
#     df2 = df1[df1['Season']==year]
#     df3 = df2[df2['batter']==batsman]
#     fig = px.bar(df3,x='Season',y='TotalRuns',title="Total Runs by "+batsman+" in all years")
#     return fig.to_html()

# def year_runs(year,batsman):
#     df1 = ballMatch[(ballMatch['Season']==int(year)) & (ballMatch['batter']==batsman)].batsman_run().sum()
#     fig= px.bar(df1,x="Season", y="batsman_run")
#     return fig.to_html()