import streamlit as st
import plotly.graph_objs as go
from scipy.stats import t, norm
import numpy as np

# Set layout
layout = go.Layout(title='t and z distributions with 0 mean and standard deviation of 1',
                   xaxis=dict(title='Values'),
                   yaxis=dict(title='Density')
                   #,plot_bgcolor='rgb(240,240,240)'
                   )

# Define function to generate t and z distributions
def generate_distributions(df):
    # Generate t-distribution with 0 mean and standard deviation of 1
    t_values = np.linspace(t.ppf(0.01, df), t.ppf(0.99, df), 100)
    t_dist = t.pdf(t_values, df, loc=0, scale=1)

    # Generate z-distribution with 0 mean and standard deviation of 1
    z_values = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
    z_dist = norm.pdf(z_values, loc=0, scale=1)

    # Create traces
    t_trace = go.Scatter(x=t_values, y=t_dist, name='t-distribution', line=dict(color='rgb(252,79,48)'))
    z_trace = go.Scatter(x=z_values, y=z_dist, name='z-distribution', line=dict(color='rgb(48,162,218)'))

    return [t_trace, z_trace]

# Set up Streamlit app
st.title('t and z distributions')
df = st.slider('Degrees of Freedom', min_value=1, max_value=50, value= 4 , step = 2)

# Generate distributions and plot using Plotly
fig = go.Figure(data=generate_distributions(df), layout=layout)
st.plotly_chart(fig, use_container_width=True)
