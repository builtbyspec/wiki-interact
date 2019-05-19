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
        html.H1("Spotify Through the Ears", className="display-3"),
        html.P(
            "An exploration of bops, beats, bangers, and the listeners who play them"
        )
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
