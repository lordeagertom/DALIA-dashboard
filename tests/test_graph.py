from dalia_dashboard.dps import dps_instances
from dalia_dashboard.plot import plot_nan, plot_diff, plot_skill, title_text
import pytest


def test_diffs():
    data = dps_instances[0].data
    fig = plot_diff(data, title_text(dps_instances[0]))
    fig.show()

def test_skills():
    data = dps_instances[0].data
    fig = plot_skill(data, title_text(dps_instances[0]))
    fig.show()

def test_nans():
    data = dps_instances[5].data
    fig = plot_nan(data, title_text(dps_instances[5]))
    fig.show()