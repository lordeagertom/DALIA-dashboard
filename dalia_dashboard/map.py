import folium
import streamlit as st
from streamlit_folium import st_folium
from dalia_dashboard.dps import dps_instances


def add_marker_to_map(poi, folium_map):
    folium.Marker(
        location=[poi.lat, poi.lon],
        tooltip=f"DPS{poi.number}",
        icon=folium.Icon(icon="info-sign", color="blue")
    ).add_to(folium_map)


def add_map_column():
    m = folium.Map(location=[47.23137670455077, 19.312211215415363], zoom_start=5)
    for dps in dps_instances:
        add_marker_to_map(dps, m)
    map_data = st_folium(m, width=1000, height=600, returned_objects=["last_object_clicked"])

    if map_data["last_object_clicked"] is not None:

        clicked_lat = map_data["last_object_clicked"]["lat"]
        clicked_lon = map_data["last_object_clicked"]["lng"]

        for dps in dps_instances:
            if (round(dps.lat, 5) == round(clicked_lat, 5) and
                    round(dps.lon, 5) == round(clicked_lon, 5)):
                st.session_state["selected_dps"] = dps  # Update the selected POI in session state
                break
