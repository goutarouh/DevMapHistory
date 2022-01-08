import folium
import folium.plugins as folium_plugins
from pandas import DataFrame
from matplotlib import colors as cl
import matplotlib.pyplot as plt


def map_creator(data: DataFrame):

    color_map = plt.get_cmap('jet')
    c = cl.to_hex(color_map(0.1))

    times = data['time_stamp'].tolist()
    coordinates = [[longitude, latitude] for latitude, longitude in zip(
        data['latitude'].tolist(), data['longitude'].tolist()
    )]

    features = []
    for timestamp, coordinate in zip(times, coordinates):
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': coordinate,
            },
            'properties': {
                'time': timestamp,
                'popup': "popup",
                'icon': 'circle',
                'iconstyle': {
                    'color': c,
                    'fill': True,
                    'radius': 5
                },
                'style': {
                    'fillOpacity': 1,
                    'weight': 1
                }
            }
        })
    folium_map = folium.Map(location=[34.390921, 135.900258], zoom_start=7)
    folium_plugins.TimestampedGeoJson(
        data={
            'type': 'FeatureCollection',
            'features': features
        }
        , transition_time=500
        , date_options='YYYY/MM/DD HH:mm:ss'
        , period='PT1M'
        , duration='PT1M'
        , add_last_point=True
        , auto_play=False
        , loop=False
        , max_speed=1
        , loop_button=True
        , time_slider_drag_update=True
    ).add_to(folium_map)

    folium_map.save("output/sample.html")
