import dash
from dash_bootstrap_components import themes


external_stylesheets = [themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets = external_stylesheets, suppress_callback_exceptions=True, 
                update_title= None, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=0.8"}])
app.title = 'ESFM | Horario'
server = app.server
import callbacks