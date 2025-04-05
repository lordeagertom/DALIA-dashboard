import plotly.graph_objects as go
import streamlit as st
from dalia_dashboard.dps import common_indexes


def title_text(dps):
    return f"DPS{dps.number}: {dps.name}"

def get_combined_figure(fig_diff, fig_skill, fig_nan, dps):
    # Combine traces from all figures into one figure with clear visibility control
    fig = go.Figure()

    # Add traces from fig_diff
    for trace in fig_diff.data:
        trace.visible = True  # Initially visible
        fig.add_trace(trace)

    # Add traces from fig_skill
    for trace in fig_skill.data:
        trace.visible = False  # Initially hidden
        fig.add_trace(trace)

    # Add traces from fig_nan
    for trace in fig_nan.data:
        trace.visible = False  # Initially hidden
        fig.add_trace(trace)

    return fig

def render_graph_as_html(fig):
    # Render the combined graph as HTML
    return fig.to_html(full_html=False)

def popup(dps):

    data = dps.data.loc[common_indexes]
    fig_diff = plot_diff(data, title_text(dps))
    fig_skill = plot_skill(data, title_text(dps))
    fig_nan = plot_nan(data, title_text(dps))
    fig = get_combined_figure(fig_diff, fig_skill, fig_nan, dps)
    return render_graph_as_html(fig)


def plot_diff(data, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['Difference in Totals ()'], y=data.index, name="Difference in Totals", orientation="h"))
    fig.update_layout(
        title={"text": title, "x": 0.5, "xanchor": "center"},
        xaxis={"automargin": True, "title": "Total Forecast - Observation (mm)", "range": [-600, 600]},  # Set initial x-axis limits
        yaxis={"automargin": True},  # Prevent truncation
        margin=dict(l=150, r=50, t=50, b=50)  # Manual adjustment (if needed)
    )
    return fig


def plot_skill(data, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['Heidke Skill Score at 0.1 '], y=data.index, name="Heidke Skill Score at 0.1", orientation="h"))
    fig.update_layout(
        title={"text": title, "x": 0.5, "xanchor": "center"},
        xaxis={"automargin": True, "title": "HSS at 0.1mm", "range": [0, 0.5]},  # Dynamically adjust
        yaxis={"automargin": True},  # Prevent truncation
        margin=dict(l=150, r=50, t=50, b=50)  # Manual adjustment (if needed)
    )
    return fig


def plot_nan(data, title):
    data['Hits'] = data['Expected Observations'] - data['Total NaNs']
    data['Model Missing'] = data['NaNs in Model']
    data['Meas. Missing'] = data['Total NaNs'] - data['NaNs in Model']
    data['Model'] = data.index
    fig = go.Figure()
    fig.add_trace(go.Bar(y=data['Model'], x=data['Hits'], name="Hits", marker_color="green", orientation="h"))
    fig.add_trace(go.Bar(y=data['Model'], x=data['Model Missing'], name="Model Missing", marker_color="blue", orientation="h"))
    fig.add_trace(go.Bar(y=data['Model'], x=data['Meas. Missing'], name="Meas. Missing", marker_color="red", orientation="h"))
    fig.update_layout(
        title={"text": title, "x": 0.5, "xanchor": "center"},
        xaxis={"automargin": True, "title": "hours with/without data"},  # Dynamically adjust
        yaxis={"automargin": True},  # Prevent truncation
        margin=dict(l=150, r=50, t=50, b=50),  # Manual adjustment (if needed)
        barmode="stack"
    )
    return fig


def add_graph_column():
    selected_graph = st.radio(
        label="Select a graph to display:",
        options=["Bias", "Skill", "NaNs"],  # Options to toggle between
        index=0,  # Default to the first graph
        horizontal=True  # Display options in a horizontal row
    )
    if st.session_state["selected_dps"] is not None:
        selected_dps = st.session_state["selected_dps"]
        data = selected_dps.data.loc[common_indexes]
        st.markdown(f"<h3 style='text-align: center;'>{title_text(selected_dps)}</h3>", unsafe_allow_html=True)
        if selected_graph == "Bias":
            fig = plot_diff(data, title_text(selected_dps))
        elif selected_graph == "Skill":
            fig = plot_skill(data, title_text(selected_dps))
        elif selected_graph == "NaNs":
            fig = plot_nan(data, title_text(selected_dps))
        st.plotly_chart(fig, use_container_width=True)  # Display the selected graph
    else:
        st.write("Click a PoI to see validation.")
