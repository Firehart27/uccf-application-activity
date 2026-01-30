import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

import requests
import pandas as pd

url = "https://v1.data.uccf.io/api/christian-unions/expand"
response = requests.get(url)
data = response.json()

datadf = pd.DataFrame(data)

# institution is compiled here:
# institutions = datadf['institutions']
# manual appending of data so that institutions is a list of dicts
institutions = []

for i in range(len(datadf)):
    institutions.append(datadf['institutions'][i][0])
    institutions[i]["full_name"] = datadf['full_name'][i]
    # check if the social links exist
    for socials in ['website', 'twitter', 'facebook', 'instagram']:
        if datadf[socials][i] != None:
            # if exists, add to the insitutions dict
            institutions[i][socials] = datadf[socials][i]


# Parse geocodes
lats = []
lons = []
names = []
full_names = []

for i in range(len(institutions)):
    if institutions[i]['geocode'] is not None:
        lat, lon = (institutions[i]['geocode'].split(','))
        lats.append(float(lat))
        lons.append(float(lon))
    else:
        lats.append(0)
        lons.append(0)
    names.append(institutions[i]['name'])

# Create the Dash app
app = dash.Dash(__name__)

# Create the map figure
fig = go.Figure(go.Scattermap(
    lat=lats,
    lon=lons,
    mode='markers',
    marker=dict(size=12),
    text=names,
    hoverinfo='text'
))

fig.update_layout(
    mapbox=dict(
        style='open-street-map',  # Free, no token needed
        center=dict(lat=sum(lats)/len(lats), lon=sum(lons)/len(lons)),
        zoom=5
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    height=600,
    clickmode='event+select'  # Enable click events
)

app.layout = html.Div([
    html.H1('UK Institutions Map'),
    dcc.Graph(id='map', figure=fig),
    html.Div(id='institution-info', style={
        'padding': '20px',
        'marginTop': '20px',
        'border': '1px solid #ddd',
        'borderRadius': '5px'
    })
])

@app.callback(
    Output('institution-info', 'children'),
    Input('map', 'clickData')
)

def display_click_data(clickData):
    if clickData is None:
        return html.P('Click on a marker to see institution details and links')
    
    # Get the clicked institution index position
    point_index = clickData['points'][0]['pointIndex']
    inst = institutions[point_index]
    
    # Create the links display
    links = [
        html.H3(inst['name']),
        html.H3(inst['full_name']),
        html.P(f"Postcode: {inst['postcode']}"),
        html.P(f"Region: {inst['region']['name']}"),
        html.Hr(),
        html.H4('Links:'),

    ]

    # Define all possible social links with their icons and labels
    social_config = {
        'website': {'icon': '🌐', 'label': 'Official Website'},
        'twitter': {'icon': '🐦', 'label': 'Twitter'},
        'instagram': {'icon': '📷', 'label': 'Instagram'},
        'facebook': {'icon': '📘', 'label': 'Facebook'},
    }

    # logic to only show existing links
    found_links = False

    # logic to add only existing links
    for key, config in social_config.items():
        if key in inst:
            links.append(
                html.A(f"{config['icon']} {config['label']}", 
                       href=inst[key], 
                       target='_blank',
                       style={'display': 'block', 'margin': '10px 0', 'fontSize': '16px'})
            )
            found_links = True

    if not found_links:
        links.append(html.P("No links available for this institution."))
            
    
    return html.Div(links)

if __name__ == '__main__':
    app.run(debug=True)
