import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import datetime
from plotly import tools

prose_df = pd.read_json("prose.json").T
top_streams_df = pd.read_csv('top_streams.csv')

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

top_data = [ozuna,sheeran,chainsmokers,malone,drake]

top_layout = go.Layout(
    title = "Streams per Day of Top 5 Artists",
    xaxis = dict(
        range = ['2017-01-01','2017-12-31']
    ),
    yaxis = dict(
        range = [0,40000000]
    )
)

jumbotron = dbc.Jumbotron(
    [
        html.H1("{{A title might go here.}}", className="display-3"),
        html.P("{{Some semblance of a tagline might go here.}}")
    ],
    className = 'my-div text-center',
)

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
                            html.H2(prose_df.loc["week_ratios", "title"]),
                            html.P(prose_df.loc["week_ratios", "prose_1"]),
                            html.P(prose_df.loc["week_ratios", "prose_2"]),
                            html.P(prose_df.loc["week_ratios", "prose_3"]),
                            html.P(prose_df.loc["week_ratios", "prose_4"]),
                            html.P(prose_df.loc["song_features", "prose_1"]),
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
    html.H2(prose_df.loc["lil_peep", "title"]),
    html.P(prose_df.loc["lil_peep", "prose_1"]),
    html.P(prose_df.loc["lil_peep", "prose_2"]),
    html.H2(prose_df.loc["x", "title"]),
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
                        html.P("{{Some semblance of an introduction might go here.}}"),
                        html.P("{{Some semblance of an introduction might go here.}}"),
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
