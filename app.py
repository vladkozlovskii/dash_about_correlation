#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

filepath = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQQKcjObxJfMAOkArbU2-ven8yUOSYjbNiIrqPu7nbElnjE0Ad_IB3yB3I6HQnKYDx-hD34dXtxf7td/pub?gid=0&single=true&output=csv'
#filepath = 'Kara_AMK_all.csv'
data = pd.read_csv(filepath)

quant_list = []
for i in data.columns:
    if data[i].dtype == 'int64' or data[i].dtype =='float64':
        quant_list.append(i)


app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Correlation between two parameters"),

        dcc.Dropdown(
            id="dropdown_1", options=quant_list, value="lat"
        ),
        dcc.Dropdown(
            id="dropdown_2", options=quant_list, value="lon"
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    [Input("dropdown_1", "value"), Input("dropdown_2", "value")])

def scatter_and_corr(dd1, dd2):
    
    if dd1 == dd2:
        fig = px.scatter(
            data,
            x=data[str(dd1)],
            y=data[str(dd2)],
            title = 'Correlation is full, You need different parameters'
)
    
    
    if dd1 != dd2:
        df = data[[str(dd1), str(dd2)]]
        df = df.dropna()
        pearson = round(df[str(dd1)].corr(df[str(dd2)]), 2)
    
        fig = px.scatter(
            df,
            x=df[str(dd1)],
            y=df[str(dd2)],
            title = pearson
)
    
    return fig





if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8080)

# In[ ]:




