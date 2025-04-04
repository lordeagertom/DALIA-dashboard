import streamlit as st


def add_sidebar():
    st.header("Definitions")
    st.write("meteoblue's validation API returns several metrics for each point of interest validated. "
             "The metrics displayed in this dashboard are selected using the radio buttons in the app. "
             "Their meanings are explained below. ")
    st.subheader("Bias")
    st.write("The difference between forecast and observed quantities of precipitation at the given weather station. "
             "Negative values indicate that the forecast quantity is less than was observed, and vice versa. "
             "Differences are summed over the entire year. In addition to forecast accuracy, bias is influenced by "
             "the conditions at a weather station: bias tends to be lower when there is less actual rainfall.")

    st.subheader("Skill")
    st.write(
        "Skill scores compare the instances of false positives, false negatives, true positives and true negatives "
        "when forecasting 'events'. In precipitation we define events as periods with at least a threshold amount "
        "of rainfall. Here we show the [Heidke Skill Score](https://resources.eumetrain.org/data/4/451/english/msg/ver_categ_forec/uos3/uos3_ko1.htm) "
        "(HSS) considering hours with more than 0.1mm precipitation. An HSS of greater than 0 indicates the forecast is "
        "better than random chance. An HSS of 1 indicates perfect agreement between forecast and observations.")

    st.subheader("NaNs")
    st.write("Invalid measurements have a large impact on our ability to verify precipitation forecasts. For instance, "
             "bias is generally smaller for IFS04 because of missing forecast data. For our examples, most missing "
             "comparisons are due to missing forecast data. For DPS5, about half of the measurements are missing.")
