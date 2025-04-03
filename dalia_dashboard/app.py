import streamlit as st
from map import add_map_column
from plot import add_graph_column

st.set_page_config(layout="wide")

if "selected_dps" not in st.session_state:
    st.session_state["selected_dps"] = None  # This will hold the currently selected POI data


def main():
    col1, col2 = st.columns([2, 1])

    with col1:
        add_map_column()

    with col2:
        add_graph_column()


if __name__ == "__main__":
    main()
