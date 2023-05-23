from multiprocessing.managers import BaseListProxy
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objs as go

from CricketProj.settings import STATIC_ROOT
csvPath2='CricketApp\static\CSV\Ball.csv'
csvPath1='CricketApp\static\CSV\match.csv'

balls=pd.read_csv(csvPath2)
matches=pd.read_csv(csvPath1)

def player_name():
    l1=list(balls['batter'])
    l3=list()
    for i in l1:
        if i not in l3:
            l3.append(i)
    return l3

def top_five_players():
    m1=matches['Player_of_Match'].value_counts()[0:5].keys()
    m2=matches['Player_of_Match'].value_counts()[0:5]
    fig=px.scatter(x=m1,y=m2)
    fig.update_layout(title='Top five most players')
    return fig.to_html()

def most_player_of_match():
    m1=matches['Player_of_Match'].value_counts()[:20]
    m2=matches['Player_of_Match'].value_counts()[:20]
    fig=px.bar(m1,m2,title="player who won most player of match",color="Player_of_Match")
    return fig.to_html()
 
def highest_run_scoring_player():
    batting_tot=balls.groupby('batter').apply(lambda x:np.sum(x['batsman_run'])).reset_index(name='Runs')
    batting_sorted=batting_tot.sort_values(by='Runs',ascending=False)
    top_batsmen=batting_sorted[:10] 

    data = [go.Bar(
        x = top_batsmen.batter,
        y = top_batsmen.Runs,
        )]

    layout = go.Layout(title="Top 10 Batsmen in IPL- Seasons till 2021",
                   xaxis=dict(title="Top 10 Batsmen"),
                   yaxis=dict(title="Runs Scored"))

   
    fig = go.Figure(data=data, layout=layout)
    return fig.to_html()

def top_bowlers():
    m1=balls['bowler'].value_counts()[:10]
    m2=balls['bowler'].value_counts().values[:10]
    fig=px.line(m1,m2,markers=True,title="Top 10 best bowlers")
    return fig.to_html()
    
def top_batsman():
    m1=balls['batter'].value_counts()[:10]
    m2=balls['batter'].value_counts().values[:10]
    fig=px.scatter(m1,m2,color="batter",size="batter",title="Top 10 best batsman")
    return fig.to_html()

def century():
    df_cen = balls.groupby(['batter','ID']).agg({'batsman_run':'sum'})
    df_cen = df_cen[df_cen['batsman_run']>=100]
    df_cen = df_cen.groupby(['batter']).agg({'count'})
    df_cen.columns = df_cen.columns.droplevel()
    df_cen = df_cen.sort_values(by='count',ascending=False).reset_index()
    top_10_cen=df_cen.sort_values("count", axis=0,ascending=False)
    fig = px.bar(top_10_cen, x='batter', y='count', color='batter',title="Centuries made by Batsman")
    return fig.to_html()

def half_century():
    
    df_half_cen = balls.groupby(['batter','ID']).agg({'batsman_run':'sum'})
    df_half_cen = df_half_cen[df_half_cen['batsman_run']>=50]
    df_half_cen = df_half_cen[df_half_cen['batsman_run']<100]
    df_half_cen = df_half_cen.groupby(['batter']).agg({'count'})
    df_half_cen.columns = df_half_cen.columns.droplevel()
    df_half_cen = df_half_cen.sort_values(by='count',ascending=False).reset_index()
    top_10_half_cen=df_half_cen.sort_values("count", axis=0,ascending=False)
    fig = px.bar(top_10_half_cen, x='batter', y='count', color='batter',title="Half centuries made by batsman")
    return fig.to_html()