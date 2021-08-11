### Installed
from dash.dependencies import Input, Output, State
### Local
from resources import (layout, utils)
from resources.callbacks_funcs import (
    open_input, change_input, display_table, generate_disabled,
    set_dict, set_2dict, set_3dict, generate_table, generate_2table,
    generate_3table
)
from core import app

app.layout = layout


app.callback(Output('input-id','children'),
            [
                Input('ingresar-id','n_clicks'), 
                Input('ingresar-id','children'), 
                State('Materia_y_grupo','value'),
                State('text-id','value')
            ], prevent_initial_call=True)(
    open_input
)

app.callback(Output('ingresar-id','children'),
            [
                Input('ingresar-id','n_clicks'),
                State('text-id','value')
            ])(
    change_input
)

app.callback([
                Output('Materia_y_grupo','value'),
                Output('guardado','children')],
            [
                Input('ingresar-id','children'),
                State('text-id','value'), 
                State('Materia_y_grupo', 'value')
            ])(
    display_table
)
app.callback([
                Output('Materia_y_grupo','disabled'),
                Output('text-generate-id','children'),
                Output('generar-id','disabled'),
                Output('ingresar-id','disabled'),
                Output('cache', 'children')
            ],
            [
                Input('Materia_y_grupo','value'), 
                Input('ingresar-id','children'),
                Input('generar-id','n_clicks'), 
                Input('Materia_y_grupo','value'), 
                State('generar-id','disabled')])(
    generate_disabled
)

app.callback(Output('Semestre','options'),[Input('Carrera','value')])(
    set_dict
)

app.callback(Output('Materia','options'),[Input('Carrera','value')])(
    set_2dict
)

app.callback(Output('Materia_y_grupo','options'),[Input('Carrera','value')])(
    set_3dict
)

app.callback([
                Output('First_table','children'), 
                Output('First_table2', 'children')
            ], 
            [
                Input('Semestre','value'),
                Input('Carrera','value')
            ])(
    generate_table
)

app.callback([
                Output('second_table','children'), 
                Output('second_table2', 'children')
            ],
            [
                Input('Materia','value'),
                Input('Carrera','value')])(
    generate_2table
)

app.callback([
                Output('third_table','children'),
                Output('traslapes','children'), 
                Output('table-prueba', 'children')
            ],
            [
                Input('Materia_y_grupo','value'),
                Input('Carrera','value')
            ])( 
    generate_3table
)