import streamlit as st
from dalia_dashboard.map import add_map_column
from dalia_dashboard.plot import add_graph_column
from dalia_dashboard.sidebar import add_sidebar

st.set_page_config(layout="wide")

if "selected_dps" not in st.session_state:
    st.session_state["selected_dps"] = None  # This will hold the currently selected POI data


def main():
    st.title("DPS Validation Dashboard")
    st.write("Selected results from meteoblue's validation API corresponding to "
             "DALIA Pilot Sites")

    with st.sidebar:
        add_sidebar()

    col1, col2 = st.columns([1, 1])  # Adjust column ratio back to equal

    with col1:
        add_map_column()

    with col2:
        add_graph_column()


if __name__ == "__main__":
    main()
