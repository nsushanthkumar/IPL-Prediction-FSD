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
def won_by_wickets():
    fig = px.pie(matches,
             values=matches[matches['WonBy']=='Wickets']['WinningTeam'].value_counts(), 
             names=matches[matches['WonBy']=='Wickets']['WinningTeam'].value_counts().keys(),
            color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(
    title='Teams with 10 wicket victory',
    legend_title="Team Name "
    )
    return fig.to_html()

def team_name():
    team_name=list()
    name=list(matches['Team1'])
    for x in name:
        if x not in team_name:
            team_name.append(x)
    return team_name

def won_by_superover():
    fig = px.pie(matches,
             values=matches[matches['WonBy']=='SuperOver']['WinningTeam'].value_counts(), 
             names=matches[matches['WonBy']=='SuperOver']['WinningTeam'].value_counts().keys(),
            color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(
    title='Teams won by SuperOver',
    legend_title="Team Name "
    )
    return fig.to_html()

def won_by_runs():
    fig = px.pie(matches,
             values=matches[matches['WonBy']=='Runs']['WinningTeam'].value_counts(), 
             names=matches[matches['WonBy']=='Runs']['WinningTeam'].value_counts().keys(),
            color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(
    title='Teams won by Runs',
    legend_title="Team Name "
    )
    return fig.to_html()

def total_matches():
    fig = px.scatter(matches, x=matches['City'].value_counts().keys(),
             y=matches['City'].value_counts(),
             color=matches['City'].value_counts().keys(),
             labels={
                     'x': "City",
                     'y': "Total number of matches"
                     
                 })
    fig.update_layout(title='Total number of matches played on the specific ground')
    return fig.to_html()

def toss_desicion():
    winner_field=matches[(matches['TossWinner']==matches['WinningTeam'])& (matches['TossDecision']=='field')&(matches['TossWinner']=='Royal Challengers Bangalore')].count()[0]
    winner_bat=matches[(matches['TossWinner']==matches['WinningTeam'])& (matches['TossDecision']!='field')&(matches['TossWinner']=='Royal Challengers Bangalore')].count()[0]
    # matches won when won the toss
    fig = px.bar(matches, x=[winner_field,winner_bat],
             y=['Field','Bat'],
             color=['Field','Bat'],
             labels={
                     'x': "Decision",
                     'y': "Count"
                     
                 })
    fig.update_layout(title='Influence of toss Decision on match result of team Royal Challengers Bangalore')
    return fig.to_html()

def most_win():
    matches['WinningTeam'].value_counts()[:5]

    # Number of matches played per venue
    fig = px.bar(matches, x=matches['WinningTeam'].value_counts().keys()[:5],
             y=matches['WinningTeam'].value_counts()[:5],
             color=matches['WinningTeam'].value_counts().keys()[:5],
             labels={
                     'x': "Team name",
                     'y': "Total number of Matches Won"
                     
                 })
    fig.update_layout(title='Top five most consistant teams throught the IPL Seasons')
    return fig.to_html()

def matches_per_season():
    fig = px.histogram(matches, x=matches['Season'].value_counts().keys(),
             y=matches['Season'].value_counts(),
             color=matches['Season'].value_counts().keys(),
             labels={
                     'x': "Year",
                     'y': "Number of matches"
                     
                 })
    fig.update_layout(title='Total matches per season')
    fig.to_html()
    return fig.to_html()

def total_run():
    mergeData = matches[['ID','Season']].merge(balls, left_on='ID', right_on='ID', how='left').drop('ID',axis=1)

    season_runs = mergeData.groupby(['Season'])['total_run'].sum().reset_index()
    fig = px.line(season_runs,x='Season',y='total_run',markers=True)
    fig.update_layout(title='Total Runs Per Season')
    return fig.to_html()


def no_of_times_team_won_toss():
    trace1 = go.Bar(x=matches["WinningTeam"].value_counts().index, y=matches["WinningTeam"].value_counts().values,name="match win")
    trace2 = go.Bar(x=matches["TossWinner"].value_counts().index, y=matches["TossWinner"].value_counts().values,name="toss win")
    data = [trace1, trace2]
    layout = go.Layout(title="Total number of wins for every team till 2021",
                   xaxis=dict(title="Teams"),
                   yaxis=dict(title="Number of Matches"),
                   legend=dict(x=1.0, y=0.5)
                   ,barmode="group"     )
    fig= go.Figure(data=data, layout=layout)
    return fig.to_html()

def played_win_WinPercentage():
    matches_played=pd.concat([matches['Team1'],matches['Team2']])
    matches_played=matches_played.value_counts().reset_index()
    matches_played.columns=['Team','Total Matches']
    matches_played['wins']=matches['WinningTeam'].value_counts().reset_index()['WinningTeam']

    matches_played.set_index('Team',inplace=True)
    totm = matches_played.reset_index().head(8)



    trace1 = go.Bar(x=matches_played.index,y=matches_played['Total Matches'],
                name='Total Matches',opacity=0.4)

    trace2 = go.Bar(x=matches_played.index,y=matches_played['wins'],
                name='Matches Won',marker=dict(color='red'),opacity=0.4)

    trace3 = go.Bar(x=matches_played.index,
               y=(round(matches_played['wins']/matches_played['Total Matches'],3)*100),
               name='Win Percentage',opacity=0.6,marker=dict(color='gold'))

    data = [trace1, trace2, trace3]

    layout = go.Layout(title='Match Played, Wins And Win Percentage',xaxis=dict(title='Team'),
                    yaxis=dict(title='Count'),bargap=0.2,bargroupgap=0.1, plot_bgcolor='rgb(245,245,245)')

    fig = go.Figure(data=data, layout=layout)
    return fig.to_html()

def toss_desicion():
    fig=px.pie(names = matches.TossDecision.value_counts().index,
       values=matches.TossDecision.value_counts().values,title = "Toss Desicions Fielding or Batting")
    return fig.to_html()

def no_of_toss_wins():
    fig=px.pie(values=matches['TossWinner'].value_counts(),names=matches['TossWinner'].value_counts().keys()
    ,title="Number of toss wins With respect to teams")
    return fig.to_html()
 