import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd


from utilities import (
    get_Arap_Outline
)

Arap_outline = get_Arap_Outline()
# print(Arap_outline)


def get_Choropleth(gdf, schools, marker_opacity, marker_line_width, marker_line_color, fig=None):
    # print(gd['geometry'])
    # print(gd.columns)
    # print(gdf['Retailer_Name'])
    # print(schools.columns)
    
    if fig is None:
        fig = go.Figure(
        )


    # fig.add_trace(
    #     go.Choroplethmapbox(
    #         geojson=eval(df['geometry'].to_json()),
    #         # geojson=gd,
    #         locations=df.index,
    #         z=df['Total'],
    #         marker_opacity = marker_opacity,
    #         marker_line_width = marker_line_width,
    #         marker_line_color = marker_line_color,
    #         # customdata=gwb["GEOID20"],
    #         hoverinfo='z',
    #         colorscale='fall',
    #         zmax=1000,
    #         zmin=500
    #     )
    # )
    

    fig.add_trace(
        go.Scattermapbox(
            lat=gdf['Y'],
            lon=gdf['X'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=5,
                color=gdf['color']
            ),
            customdata=gdf['DOING_BUSINESS_AS'],
            hoverinfo='text',
            # showlegend=False,
            hovertemplate='<br>'.join([
            'Store: %{customdata}',
            ]),
            name='Retailer'
        )
    )

    # fig.add_trace(
    #     go.Scattermapbox(
    #         lat=schools['lat'],
    #         lon=schools['lon'],
    #         mode='markers',
    #         marker=go.scattermapbox.Marker(
    #             size=10,
    #             color='green'
    #         ),
    #         # line=schools['Name'],
    #         hoverinfo="text",
    #         # customdata=schools['Name'],
    #         # hoverinfo='text',
    #         # showlegend=False,
    #         # hovertemplate='<br>'.join([
    #         # 'School: %{customdata}',
    #         # ]),
    #         # hovertemplate= 'School: %{line}'
    #     )
    # )

    # fig.update_traces(
    #     customdata=schools['Name'],
    #     hovertemplate='<br>'.join([
    #         'School: %{customdata}',
    #         ]),
    # )

    return fig

# def get_map(df, ):

#     fig = go.Figure()
  

    

#     return fig


def get_figure(gdf, schools):

    # print(df)
    fig = get_Choropleth(gdf, schools, marker_opacity=1,
                         marker_line_width=.1, marker_line_color='#6666cc')
    
    layer = [
            {
                "source": Arap_outline["geometry"].__geo_interface__,
                "type": "line",
                "color": "blue"
            }
        ]
    
    
    fig.update_layout(mapbox_style="carto-positron", 
                            mapbox_zoom=10.4,
                            mapbox_layers=layer,
                            mapbox_center={"lat": 39.65, "lon": -104.8},
                            margin={"r":0,"t":0,"l":0,"b":0},
                            autosize=True,
                            uirevision='constant'),
    
                        
    
    # if len(geo_tracts_highlights) != 0:
    #     fig = get_Choropleth(df, geo_tracts_highlights, marker_opacity=1.0,
    #                          marker_line_width=3, marker_line_color='aqua', fig=fig)
    

    return fig