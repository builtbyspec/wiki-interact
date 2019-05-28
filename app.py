import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import datetime
from plotly import tools

prose_df = pd.read_json("prose.json").T
ratios_df = pd.read_csv('ratios.csv').dropna()
streams_df = pd.read_csv('streams.csv').reset_index(drop=True)
top_streams_df = pd.read_csv('top_streams.csv')
spec_ratios_df = pd.read_csv('spec_ratios.csv')
travis_df = pd.read_csv('travis.csv')
top_df = pd.read_csv('top.csv')
lil_peep_df = pd.read_csv('lil_peep.csv')
x_df = pd.read_csv('x.csv')
f_df = pd.read_csv('mean_features.csv')
options_list = [{'label':artist,'value':artist} for artist in top_df.Artist.unique()]


len = ratios_df.ratio.size
low_ratios_vals = ratios_df.ratio[len-5:len].tolist()
low_ratios_labels = ratios_df.Artist[len-5:len].tolist()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

song_1 = travis_df[travis_df.track_name == "SICKO MODE"]
song_2 = travis_df[travis_df.track_name == "Butterfly Effect"]
song_3 = travis_df[travis_df.track_name == "CAROUSEL"]
song_4 = travis_df[travis_df.track_name == "R.I.P. SCREW"]
song_5 = travis_df[travis_df.track_name == "STARGAZING"]

travis_1 = go.Scatter(
                x= song_1.date,
                y= song_1.mean_streams,
                name = "SICKO MODE",
                line = dict(color = '#90DAB5'),
                opacity = 0.8)

travis_2 = go.Scatter(
                x=song_2.date,
                y=song_2.mean_streams,
                name = "Butterfly Effect",
                line = dict(color = '#3F94AB'),
                opacity = 0.8)

travis_3 = go.Scatter(
                x=song_3.date,
                y=song_3.mean_streams,
                name = "CAROUSEL",
                line = dict(color = '#6285B2'),
                opacity = 0.8)

travis_4 = go.Scatter(
                x=song_4.date,
                y=song_4.mean_streams,
                name = "R.I.P. SCREW",
                line = dict(color = '#4B4782'),
                opacity = 0.8)

travis_5 = go.Scatter(
                x=song_5.date,
                y=song_5.mean_streams,
                name = "STARGAZING",
                line = dict(color = '#3E3E3E'),
                opacity = 0.8)

ozuna = go.Scatter(
                x=top_streams_df[top_streams_df.artist == "Ozuna"].date,
                y=top_streams_df[top_streams_df.artist == "Ozuna"].total_streams,
                name = "Ozuna",
                line = dict(color = '#90DAB5'),
                opacity = 0.8)

sheeran = go.Scatter(
                x=top_streams_df[top_streams_df.artist == "Ed Sheeran"].date,
                y=top_streams_df[top_streams_df.artist == "Ed Sheeran"].total_streams,
                name = "Ed Sheeran",
                line = dict(color = '#3F94AB'),
                opacity = 0.8)

malone = go.Scatter(
                x=top_streams_df[top_streams_df.artist == "Post Malone"].date,
                y=top_streams_df[top_streams_df.artist == "Post Malone"].total_streams,
                name = "Post Malone",
                line = dict(color = '#6285B2'),
                opacity = 0.8)

drake = go.Scatter(
                x=top_streams_df[top_streams_df.artist == "Drake"].date,
                y=top_streams_df[top_streams_df.artist == "Drake"].total_streams,
                name = "Drake",
                line = dict(color = '#4B4782'),
                opacity = 0.8)

chainsmokers = go.Scatter(
                x=top_streams_df[top_streams_df.artist == "The Chainsmokers"].date,
                y=top_streams_df[top_streams_df.artist == "The Chainsmokers"].total_streams,
                name = "The Chainsmokers",
                line = dict(color = '#3E3E3E'),
                opacity = 0.8)

lil_peep = go.Scatter(
                x=lil_peep_df["date"],
                y=lil_peep_df["mean_streams"],
                showlegend = False
)

lil_peep_pos = go.Scatter(
                x=lil_peep_df["date"],
                y=lil_peep_df["max_position"],
                showlegend = False
)

x_streams = go.Scatter(
                x=x_df["date"],
                y=x_df["mean_streams"],
                showlegend = False
)

x_pos = go.Scatter(
                x=x_df["date"],
                y=x_df["max_position"],
                showlegend = False
)

trace0 = go.Scatter(
    x=["2017-11-15", "19-01-01", "18-09-19"],
    y=[2100000, 2100000, 2300000],
    text=['Death', 'COWYS Pt. 2 drops', 'Falling Down drops'],
    mode='text',
    showlegend = False,
    textfont=dict(
        size=14,
        color='rgb(29,185,84)',
        family='Overpass'
    )
)

trace1 = go.Scatter(
    x=["2017-11-15", "19-01-01", "18-09-19"],
    y=[225, 210, 225],
    text=['Death', 'COWYS Pt. 2 drops', 'Falling Down drops'],
    mode='text',
    showlegend = False,
    textfont=dict(
        size=14,
        color='rgb(29,185,84)',
        family='Overpass'
    )
)

trace_x = go.Scatter(
    x=["17-08-25", "18-01-16", "18-06-18", "18-12-07"],
    y=[1300000, 1300000, 1300000, 1300000],
    text=['17 drops', '? drops', 'X passes', 'Skins drops'],
    mode='text',
    showlegend = False,
    textfont=dict(
        size=14,
        color='rgb(29,185,84)',
        family='Overpass'
    )
)

trace_x_pos = go.Scatter(
    x=["17-08-25", "18-03-16", "18-06-18", "18-12-07"],
    y=[235, 235, 235, 235],
    text=['17 drops', '? drops', 'X Passes', 'Skins drops'],
    mode='text',
    showlegend = False,
    textfont=dict(
        size=14,
        color='rgb(29,185,84)',
        family='Overpass'
    )
)

stream_ratio = go.Bar(
    x=low_ratios_vals,
    y=low_ratios_labels,
    text=[str(i)[1:4] + ' more weekday streams' for i in low_ratios_vals],
    textposition='auto',
    orientation='h',
    marker=dict(
        color='rgba(158,202,225,0.6)',
        line=dict(
            color='rgba(8,48,107,0.7)',
            width=1
        ),
    )
)
low_stream_ratio = go.Bar(
    x=spec_ratios_df.ratio.tolist(),
    y=spec_ratios_df.Artist.tolist(),
    text=[str(i)[1:4] + ' more weekend streams' for i in spec_ratios_df.ratio.tolist()],
    textposition='auto',
    orientation='h',
    marker=dict(
        color='rgba(158,202,225,0.6)',
        line=dict(
            color='rgba(8,48,107,0.7)',
            width=1
        ),
    )
)

trace_acou = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_energy,
    showlegend = False,
    marker=dict(
        color='rgb(29,185,84)'
    )
    #hoverinfo
)

trace_danc = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_loudness,
    showlegend = False,
    marker=dict(
        color='rgb(29,185,84)'
    )
)

trace_ener = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_acousticness,
    showlegend = False,
    marker=dict(
        color='rgb(29,185,84)'
    )
)

trace_instr = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_danceability,
    showlegend = False,
    marker=dict(
        color='rgb(29,185,84)'
    )
)

trace_live = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_speechiness,
    showlegend = False,
    marker=dict(
        color='rgb(29,185,84)'
    )
)

trace_loud = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_instrumentalness,
    showlegend = False,
    marker=dict(
        color='rgb(29,185,84)'
    )
)

trace_spee = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_liveness,
    showlegend = False,
    marker=dict(
        color='rgb(29,185,84)'
    )
)

trace_vale = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_valence,
    showlegend = False,
    marker=dict(
        color='rgb(29,185,84)'
    )
)

fig = tools.make_subplots(rows=4, cols=2, subplot_titles=(
    'Energy', 'Loudness','Liveness', 'Danceability', 'Speechiness', 'Valence', 'Acousticness','Instrumentalness'
), print_grid=False)

fig.append_trace(trace_acou, 1, 1)
fig.append_trace(trace_danc, 1, 2)

fig.append_trace(trace_spee, 2, 1)
fig.append_trace(trace_instr, 2, 2)

fig.append_trace(trace_live, 3, 1)
fig.append_trace(trace_vale, 3, 2)

fig.append_trace(trace_ener, 4, 1)
fig.append_trace(trace_loud, 4, 2)


fig['layout'].update(height=1000)

stream_ratio_data = [stream_ratio]
low_stream_ratio_data = [low_stream_ratio]
top_data = [ozuna,sheeran,chainsmokers,malone,drake]
lil_peep_data = [lil_peep, trace0]
lil_peep_pos_data = [lil_peep_pos, trace1]
x_streams_data = [x_streams, trace_x]
x_pos_data = [x_pos, trace_x_pos]
travis_data = [travis_1, travis_2, travis_3, travis_4, travis_5]

travis_layout = go.Layout(
    title = "Travis Scott's Top Songs",
)

top_layout = go.Layout(
    title = "Streams per Day of Top 5 Artists",
    xaxis = dict(
        range = ['2017-01-01','2017-12-31']
    ),
    yaxis = dict(
        range = [0,40000000]
    )
)

top_ratio_layout = go.Layout(
    title = "Artists with Lowest Weekend to Weekend Stream Ratios",
    xaxis = dict(
        range = [0,1.5]
    ),
)

low_ratio_layout = go.Layout(
    title= "Artists with Highest Weekend to Weekday Stream Ratios",
    xaxis = dict(
        range = [0,1.5]
    ),
)

lil_peep_layout = {
    'title' : "Streams on Spotify Charts over Time",
    'xaxis': {
        'range': ['2017-08-01','2019-06-01']
    },
    'yaxis': {
        'range': [0, 2500000]
    },
    'shapes': [
        # Line Vertical Death
        {
            'type': 'line',
            'x0': "2017-11-15",
            'y0': 0,
            'x1': "2017-11-15",
            'y1': 2000000,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical Falling Down
        {
            'type': 'line',
            'x0': "18-11-09",
            'y0': 0,
            'x1': "18-11-09",
            'y1': 2000000,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical Album
        {
            'type': 'line',
            'x0': "18-09-19",
            'y0': 0,
            'x1': "18-09-19",
            'y1': 2000000,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
    ]
}

lil_peep_pos_layout = {
    'title' : "Position on Spotify Charts over Time",
    'xaxis': {
        'range': ['2017-08-01','2019-06-01']
    },
    'yaxis': {
        'range': [0, 250]
    },
    'shapes': [
        # Line Vertical Death
        {
            'type': 'line',
            'x0': "2017-11-15",
            'y0': 0,
            'x1': "2017-11-15",
            'y1': 200,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical Falling Down
        {
            'type': 'line',
            'x0': "18-11-09",
            'y0': 0,
            'x1': "18-11-09",
            'y1': 200,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical Album
        {
            'type': 'line',
            'x0': "18-09-19",
            'y0': 0,
            'x1': "18-09-19",
            'y1': 200,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
    ]
}

x_streams_layout = {
    'title' : "Streams on Spotify Charts over Time",
    'xaxis': {
        'range': ['2017-01-01','2019-06-01']
    },
    'yaxis': {
        'range': [0, 1500000]
    },
    'shapes': [
        # Line Vertical Death
        {
            'type': 'line',
            'x0': "18-06-18",
            'y0': 0,
            'x1': "18-06-18",
            'y1': 1200000,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical ?
        {
            'type': 'line',
            'x0': "18-03-16",
            'y0': 0,
            'x1': "18-03-16",
            'y1': 1200000,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical Skins
        {
            'type': 'line',
            'x0': "18-12-7",
            'y0': 0,
            'x1': "18-12-7",
            'y1': 1200000,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical 17
        {
            'type': 'line',
            'x0': "17-08-25",
            'y0': 0,
            'x1': "17-08-25",
            'y1': 1200000,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
    ]
}

x_pos_layout = {
    'title' : "Position on Spotify Charts over Time",
    'xaxis': {
        'range': ['2017-01-01','2019-06-01']
    },
    'yaxis': {
        'range': [0, 250]
    },
    'shapes': [
        # Line Vertical Death
        {
            'type': 'line',
            'x0': "18-06-18",
            'y0': 0,
            'x1': "18-06-18",
            'y1': 215,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical ?
        {
            'type': 'line',
            'x0': "18-03-16",
            'y0': 0,
            'x1': "18-03-16",
            'y1': 215,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical Skins
        {
            'type': 'line',
            'x0': "18-12-7",
            'y0': 0,
            'x1': "18-12-7",
            'y1': 215,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
        # Line Vertical 17
        {
            'type': 'line',
            'x0': "17-08-25",
            'y0': 0,
            'x1': "17-08-25",
            'y1': 215,
            'line': {
                'color': 'rgb(29,185,84)',
                'width': 1,
            },
        },
    ]
}

jumbotron = dbc.Jumbotron(
    [
        html.H1("Spotify Through the Ears", className="display-3"),
        html.P(
            "An exploration of bops, beats, bangers, and the listeners who play them"
        )
    ],
    className = 'my-div text-center',
)

stock_fig = go.Figure(data=top_data, layout=top_layout)
travis_fig = go.Figure(data=travis_data, layout=travis_layout)
top_ratio_fig = go.Figure(data=stream_ratio_data, layout=top_ratio_layout)
low_ratio_fig = go.Figure(data=low_stream_ratio_data, layout=low_ratio_layout)
peep_fig = go.Figure(data = lil_peep_data, layout = lil_peep_layout)
peep_pos_fig = go.Figure(data = lil_peep_pos_data, layout = lil_peep_pos_layout)
x_streams_fig = go.Figure(data=x_streams_data, layout=x_streams_layout)
x_pos_fig = go.Figure(data=x_pos_data, layout=x_pos_layout)
date_obj = datetime.datetime.today()
month_str = ("0" + str(date_obj.month))[-2:]
day_str = ("0" + str(date_obj.day))[-2:]
date_str = "-".join(["2017", month_str, day_str])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
i = top_streams_df[top_streams_df.date == date_str]["total_streams"].idxmax()
today_artist = top_streams_df.loc[i, "artist"]
tab1_content = (
    dbc.Container([
        dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2(prose_df.loc["top_streams", "title"] + str(months[date_obj.month - 1]) + " " + str(date_obj.day) + " (today) in 2017, you would most likely be listening to " + today_artist + "."),
                            html.P(prose_df.loc["top_streams", "prose_1"]),
                            html.P(prose_df.loc["top_streams", "prose_2"], className="sidenote-text"),
                            dcc.Graph(
                                id='flyingdog',
                                config={
                                    "displaylogo": False,
                                    'modeBarButtonsToRemove': ['pan2d', 'lasso2d']
                                },
                                figure=stock_fig
                            ),
                            #html.Div([
                            #    dcc.Dropdown(
                            #    id='input-component',
                            #   options=options_list,
                            #   placeholder="Select an artist"
                            #   ),
                            #   html.Div(id='output-component')
                            #]),
                            html.H2(prose_df.loc["week_ratios", "title"]),
                            html.P(prose_df.loc["week_ratios", "prose_1"]),
                            html.P(prose_df.loc["week_ratios", "prose_2"]),
                            html.P(prose_df.loc["week_ratios", "prose_3"]),
                            dcc.Graph(
                                 figure=low_ratio_fig
                            ),
                            html.P(prose_df.loc["week_ratios", "prose_4"]),
                            dcc.Graph(
                                figure=top_ratio_fig
                            ),
                            html.P(prose_df.loc["song_features", "prose_1"]),
                            dcc.Graph(
                                figure=fig
                            ),
                            html.P(prose_df.loc["song_features", "prose_2"])
                            #html.P(prose_df.loc["", ""]),
                            #html.P(prose_df.loc["", ""]),
                            #html.P(prose_df.loc["", ""]),
                            #html.P(prose_df.loc["", ""]),
                            #html.P(prose_df.loc["", ""]),
                            #html.P(prose_df.loc["", ""]),
                            #html.P(prose_df.loc["", ""]),
                        ],
                        md=12,
                    )
                ]
            )

        ]
    )
)

tab2_content = (
    html.H2(prose_df.loc["travis", "title"]),
    html.P(prose_df.loc["travis", "prose_1"]),
    dcc.Graph(
        figure= travis_fig
    ),
    html.P(prose_df.loc["travis", "prose_2"]),
    html.H2(prose_df.loc["lil_peep", "title"]),
    html.P(prose_df.loc["lil_peep", "prose_1"]),
    dcc.Graph(
        figure= peep_fig
    ),
    html.P(prose_df.loc["lil_peep", "prose_2"]),
    dcc.Graph(
        figure= peep_pos_fig
    ),
    html.H2(prose_df.loc["x", "title"]),
    dcc.Graph(
        figure= x_streams_fig
    ),
    dcc.Graph(
        figure=x_pos_fig
    ),
    html.P(prose_df.loc["x", "prose_1"])
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Streaming Behavior"),
        dbc.Tab(tab2_content, label="Selected Artists")
    ]
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Introduction"),
                        html.P(prose_df.loc["intro", "prose_1"]),
                        html.P(prose_df.loc["intro", "prose_2"]),
                        html.Div(
                            [html.P("Choose topic")],
                            className="sidenote-text"
                        ),
                        tabs,
                        html.H2("Looking for Something to Stream?"),
                        html.P("Our team's favorite albums:"),
                        html.Div([
                            html.A(
                                dbc.Button(
                                    ["Kids At Play EP", dbc.Badge("Louis The Child", color="light", className="ml-1")],
                                    color="success",
                                ), href='https://open.spotify.com/album/21R2CiMVZH2MY514Sq2DIG', target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Attack & Release", dbc.Badge("The Black Keys", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/1YHS3Fw8THvsKVVQ1znAqi", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Rodeo", dbc.Badge("Travis Scott", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/4PWBTB6NYSKQwfo79I3prg", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Swimming", dbc.Badge("Mac Miller", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/5wtE5aLX5r7jOosmPhJhhk", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Blonde", dbc.Badge("Frank Ocean", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/3mH6qwIy9crq0I9YQbOuDf", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Scorpion", dbc.Badge("Drake", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/1ATL5GLyefJaxhQzSPVrLX", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["The Sun's Tirade", dbc.Badge("Isaiah Rashad", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/6jjX8mGrsWtrpYpFhGMrg1", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["My Beautiful Dark Twisted Fantasy", dbc.Badge("Kanye West", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/20r762YmB5HeofjMCiPMLv", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Stoney", dbc.Badge("Post Malone", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/5s0rmjP8XOPhP6HhqOhuyC", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Blue Album", dbc.Badge("Weezer", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/playlist/0XFK5bQFCI72mqiTR94oBM", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Melodrama", dbc.Badge("Lorde", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/2B87zXm9bOWvAJdkJBTpzF", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Camp", dbc.Badge("Childish Gambino", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/32KdoFFhgjCLdU0DWL71tx", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Nation of Two", dbc.Badge("Vance Joy", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/5f6Eu9QtujgGggq5qbbycV", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Section 80", dbc.Badge("Kendrick Lamar", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/13WjgUEEAQp0d9JqojlWp1", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["The Dark Side of the Moon", dbc.Badge("Pink Floyd", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/4LH4d3cOWNNsVw41Gqt2kv", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Doris", dbc.Badge("Earl Sweatshirt", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/5vRfIDOPJHy3W2wHWbzLlE", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["Salad Days", dbc.Badge("Mac DeMarco", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/1l9d1Zj9Iv2eOcdObVhdMy", target="_blank"
                            ),
                            html.A(
                                dbc.Button(
                                    ["In the Aeroplane Over the Sea", dbc.Badge("Neutral Milk Hotel", color="light", className="ml-1")],
                                    color="success",
                                ), href="https://open.spotify.com/album/5COXoP5kj2DWfCDg0vxi4F", target="_blank"
                            ),

                        ])
                    ],
                    md=12,
                )
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_scripts=['https://raw.githubusercontent.com/robin-dela/hover-effect/master/example/js/three.min.js','https://raw.githubusercontent.com/robin-dela/hover-effect/master/example/js/TweenMax.min.js','https://raw.githubusercontent.com/robin-dela/hover-effect/master/dist/hover-effect.umd.js'], external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div(
    children=[
        jumbotron,
        body,
        html.Div(
            [html.P("Built by Spec with 💚 and data")],
            className='footer-text')
    ]
)
app.title = "Spotify Through the Ears"

if __name__ == '__main__':
    app.run_server(debug=True)
