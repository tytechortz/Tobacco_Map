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
    get_Tobacco_Retailers
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
        # dbc.Col([
        #     dcc.Checklist(
        #         id="stores",
        #         options=[
        #             {"label": i, "value": i}
        #             for i in ["Safeway", "King Sooper", "Sprouts", "Walmart SC", "Walmart NM", "Whole Foods", "Trader Joe's", "Target", "Save A Lot", "Sams", "Natural Grocers", "Costco", "Lowe's", "El Mercado De Colorado" ]
        #         ],
        #         value=["Safeway", "King Sooper", "Sprouts", "Walmart SC", "Walmart NM", "Whole Foods", "Trader Joe's", "Target", "Save A Lot", "Sams", "Natural Grocers", "Costco", "Lowe's", "El Mercado De Colorado" ],
        #         inline=True
        #     ),
        # ], width=6),
        dbc.Col([
            dcc.Input(
                id='buffer',
                type='number',
                value=.5,
                step=.1,
                placeholder='Input radius in km'
            )
        #     dcc.Slider(0, 2, value=1.6,
        #         marks={
        #             0: {'label': '0', 'style': {'color': 'white'}},
        #             1.6: {'label': '1.6', 'style': {'color': 'white'}},
        #             2: {'label': '2', 'style': {'color': 'white'}},
        #         },
        #         id = 'radius',
        #     ),
        ], width=2),
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
    Input("buffer", 'value'))
def update_Choropleth(radius):
    
    df = get_Tobacco_Retailers()
    # print(df)
    # print(df['x'])
    # print(df.columns)
    
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.x, df.y), crs="EPSG:4326" 
    )
    # gdf = gpd.GeoDataFrame(
    #     df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326" 
    # )

    # gdf.to_crs(26913)

    # print(gdf.columns)
    # schools = pd.read_csv("/Users/jamesswank/Downloads/CDPHE_CDOE_School_Locations_and_District_Office_Locations.csv")
    schools = get_schools()
    # print(schools.columns)



    fig = get_figure(gdf, schools)








    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)


