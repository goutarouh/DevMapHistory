import folium
import folium.plugins as folium_plugins
from pandas import DataFrame


def map_creator(data: DataFrame):

    times = data['time_stamp_ms'].tolist()
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
                    'color': '#FF0000',
                    'fill': True,
                    'radius': 3
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
        , transition_time=10
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


def plot_target_date_location_history(data: DataFrame):
    folium_map = folium.Map(location=[34.390921, 135.900258], zoom_start=7)

    for index, row in data.iterrows():
        latitude = row['latitude']
        longitude = row['longitude']
        folium.CircleMarker(
            location=(latitude, longitude),
            radius=1,
        ).add_to(folium_map)

    folium_map.save("output/plot_all.html")
