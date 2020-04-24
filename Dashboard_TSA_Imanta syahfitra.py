import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import dash_table
from dash.dependencies import Input, Output, State

def generate_table(dataframe, page_size=10):
    return dash_table.DataTable(
        id='dataTable',
        columns=[{
            "name": i,
            "id": i
        } for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action='native',
        page_current=0,
        page_size=page_size,
        style_table={'overflowX':'scroll'}
    )

tsa = pd.read_csv('C:\\Users\\denny\\Desktop\tsa_claims_ujian.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div(children=[
    html.H1(children = 'Ujian Modul 2 Dashboar TSA'), html.Div(
        children='''
        Created By: Imanta Syahfitra
        '''
    ), html.Div([
        dcc.Tabs([
            dcc.tab(label='Dataframe Table', value='tab-1', children=[
                html.Div(children=[
                    html.Div([html.P('Claim Site'), dcc.Dropdown(
                        value='All',
                        id='filter-claim-site',
                        options=[
                            {'label':'Checked Baggage','value':'Checked Baggage'},
                            {'label':'Checkpoint','value':'Checkpoint'},
                            {'label':'Motor Vehicle','value':'Motor Vehicle'},
                            {'label':'Other','value':'Other'},
                            {'label':'All','value':''}
                        ]
                    )], className='col-3')
                ], className='row'),
                html.Br(),
                html.Div([
                    html.P('Max Rows: '),
                    dcc.Input(
                        id='filter-row',
                        type='number',
                        value=10
                    )
                ], className='row col-3'),
                html.Div(children=[
                    html.Button('search', id='filter')
                ], className='row col-4'),
                html.Div(id='div-table', children=[generate_table(tips)])
            ]),
            dcc.Tab(label='Bar-Chart', value='tab-2', children=[
                html.Div(
                    children=[
                        html.Div([html.P('Y1'), dcc.Dropdown(
                            value='Claim Count',
                            id='filter-category-y1',
                            options=[
                                {'label':'Claim Amount','value':'Claim Amount'},
                                {'label':'Close Amount','value':'Close Amount'},
                            
                            ]
                        )], className='col-4')
                    ]
                ),
                html.Div(children=[
                    
                ])
            ])
        ])
    ])
])