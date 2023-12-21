import pandas as pd
import numpy as np
from dash import Dash, html, dcc, Input, Output, State, ctx, dash_table
import dash_bootstrap_components as dbc
from datetime import date
import geopandas as gpd


from figures_utilities import (
    get_figure,
)

from utilities import (
    get_schools,
    get_Tobacco_Retailers,
    get_compliance_records,
    get_combo
)




app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

header = html.Div("Arapahoe County Tobacco Retailers", className="h2 p-2 text-white bg-primary text-center")

bgcolor = "#f3f3f1"  # mapbox light map land color

template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }



app.layout = dbc.Container([
    header,
    dbc.Row([
        dbc.Col([
            dcc.Checklist(
                id="checks",
                options=[
                    {"label": i, "value": i}
                    # for i in ["1", "2", "3", "4", "5"]
                    for i in [1, 2, 3, 4, 5]
                ],
                # value=["1", "2", "3", "4", "5"],
                inline=True
            ),
        ], width=6),
        # dbc.Col([
        #     dcc.Input(
        #         id='buffer',
        #         type='number',
        #         value=1,
        #         step=1,
        #         placeholder='Input radius in km'
        #     )
        #     dcc.Slider(0, 2, value=1.6,
        #         marks={
        #             0: {'label': '0', 'style': {'color': 'white'}},
        #             1.6: {'label': '1.6', 'style': {'color': 'white'}},
        #             2: {'label': '2', 'style': {'color': 'white'}},
        #         },
        #         id = 'radius',
        #     ),
        # ], width=2),
    ]),
    dbc.Row([
        html.Div([
            dbc.Card(
                dcc.Graph(id='fd-map', figure=blank_fig(500))),
        ]),
    ]),
])

@app.callback(
    Output("fd-map", "figure"),
    Input("checks", 'value'))
def update_Choropleth(checks):
    print(checks)
    df = get_Tobacco_Retailers()
    # print(df)
    # print(df['x'])
    # print(df.columns)
    
    # gdf = gpd.GeoDataFrame(
    #     df, geometry=gpd.points_from_xy(df.x, df.y), crs="EPSG:4326" 
    # )
    # gdf = gpd.GeoDataFrame(
    #     df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326" 
    # )

    # gdf.to_crs(26913)

    # print(gdf.columns)
    # schools = pd.read_csv("/Users/jamesswank/Downloads/CDPHE_CDOE_School_Locations_and_District_Office_Locations.csv")
    schools = get_schools()
    # print(schools.columns)

    gdf = get_combo()
    # print(gdf['count'].max())
    # print(gdf['count'].min())

    # print(type(checks[0]))


    color_dict = {1: 'blue', 2: 'green', 3: 'orange', 4: 'red'}


    gdf['color'] = gdf['count'].map(color_dict)
    # print(gdf.dtypes)

    gdf = gdf.loc[gdf['count'].isin(checks)]
    # print(gdf)
    # gdf = gdf[gdf['count'] == radius]
    # gdf.to_csv('counts.csv')

    fig = get_figure(gdf, schools)








    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)


