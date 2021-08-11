### Installed packages
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

### Local
from config import(
    group_dict, loc_list,colors,
    style_subtitles, style_bar
)

layout = html.Div( children = [
    html.Header(
        children = [html.Img (src="https://i.ibb.co/dcJMCTP/Logotipo-Final-Negro.png", 
                    style = {"margin-bottom":0, "display":"block","width": '70%', "height": "auto", "margin-left": "auto", "margin-right": "auto", "padding-top": 1,"margin-bottom": 0,"text-align":"center", 'padding-top':30}),
                    html.H3('Información de horarios 2022-1', style={'margin-bottom':0, 'margin-top':10}),html.Br()],
        style= {
            'color': '#f9aa3a',
            'margin-top':0,
            'margin-bottom':0,
            'margin-left':'auto',
            'margin-right':'auto',
            'text-align':'center',
            'margin-left':0,
            'height':"30%"
        }
    ),
    
    html.P('IMPORTANTE: La información se ha actualizado por los horarios oficiales', style = {
                                                                                       'margin-left':'5%',
                                                                                       'width': "80%",
                                                                                        'font-size':'0.8rem',
                                                                                        'color':'#3AF9AA'}
          ),
    html.H3(children = 'Filtrar por grupo', style = style_subtitles),
    
    html.Div('', style = style_bar),
    dbc.Row( [
        dbc.Col(
            children = dcc.Dropdown(id = 'Carrera', options = [{'label':'Ingeniería Matemática',
                                                                'value':'LIM'},
                                                                {'label':'Física y Matemáticas',
                                                                'value':'LFM'},
                                                                {'label':'Matemática Algorítmica',
                                                                'value':'LMA'}
                                                                ],
                                                    value = 'LIM',
                                                    searchable = False,
                                                    clearable = False,
                                                    style = {'color':'black'}),
            
             width = 8,
             md = 3
        
        ),
        dbc.Col(
            children = dcc.Dropdown(id = 'Semestre',
                                                    value = '1MV2',
                                                    searchable = False,
                                                    clearable = False,
                                                    placeholder = "Selecciona una opción",
                                                    style = {'color':'black'}),
        
            width = 4,
            md = 2
           
    
    )],justify="center", style = {'width': '90%', 'margin-left':'auto', 'margin-right':'auto', 'margin-top':20}),

    html.Table(id = 'First_table',style = {
                                            'textAlign': 'center',
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'width': "80%",
                                            'height':'auto'
                                           }
    ),
    html.Div(id = 'First_table2', style = {
                                            'textAlign': 'center',
                                            'margin':80,
                                            'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'margin-bottom':40,
                                            'width': "90%",
                                            'height':'auto',
                                            'font-size': '0.8rem'
                                           }),
    html.H3(children = 'Filtrar por materia', style = style_subtitles),
    html.Div('', style = style_bar),
    html.Div(children=[
    html.Div(
        children = dcc.Dropdown(id = 'Materia', 
                                                value = '1MV2',
                                                clearable = False,
                                                placeholder = "Selecciona una opción",
                                                    style = {'color':'black'}),
        style = {
            'margin':40,
            'width': "40%",
            'margin-top':20,
            'margin-bottom':20,
            'margin-left':"auto",
            'margin-right':"auto"
        },
        className = 'six columns'
    
    )
    ], className = 'row', style = {'width': "100%", 'margin-left':'auto', 'margin-right':'auto'}),

    html.Table(id = 'second_table',style = {
                                            'textAlign': 'center',
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'width': "80%",
                                            'height':'auto'
                                           }
    ),
    html.Div(id = 'second_table2', style = {
                                            'textAlign': 'center',
                                            'margin':80,
                                            'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'margin-bottom':40,
                                            'width': "90%",
                                            'height':'auto',
                                            'font-size': '0.8rem'
                                           }),
    html.H3(children = 'Organizar horario', style = style_subtitles),
    html.Div('', style = style_bar),
    html.Div(children = [
        html.Div(
            children = dcc.Dropdown(id = 'Materia_y_grupo',
                                                    value = ['1MV2','0'],
                                                    multi=True,
                                                    clearable = True,
                                                    placeholder = "Selecciona una opción",
                                                    style = {'color':'black'}),
            style = {
                'margin':40,
                'width': "60%",
                'margin-top':20,
                'margin-bottom':20,
                'margin-left':"auto",
                'margin-right':"auto",
            
            },
            
            className = 'two columns'
        
        ),
        
    ], className = 'row', style = {'width': "100%", 'margin-left':'auto', 'margin-right':'auto'}),
    html.P(["Si tu asignatura no cuenta con grupo de WhatsApp créalo tú y publica su link en el ", html.A('Índice de grupos', target="_blank", href = 'https://docs.google.com/spreadsheets/d/16_jhdhBcgBVSwtFpl_BGEHOwJObfEeO_wCs-Nqw3fSY/edit?usp=sharing', style ={'color': '#F9AA3A'})], style ={'text-align':'center', 'margin-bottom':1, 'font-size':'1rem'}),
    html.Div(id = "traslapes", style = {'margin-bottom':10, 'padding-bottom':1, 'color':'white'}),
    html.Table(id = 'third_table',style = {
                                            'textAlign': 'center',
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'width': "80%",
                                            'height':'auto'
                                           }
    ),
    dbc.Spinner(
        html.Div(id = 'table-prueba', style = {
                                                'textAlign': 'center',
                                                'margin':80,
                                                'margin-top':10,
                                                'margin-left':'auto',
                                                'margin-right':'auto',
                                                'margin-bottom':20,
                                                'width': "90%",
                                                'height':'auto',
                                                'font-size': '0.8rem'
                                            }),
    ),
    html.P("Organiza tu horario y después genera un ID", style ={'text-align':'center', 'margin-bottom':1, 'font-size':'0.8rem'}),
    html.P("Podrás recuperar tu horario y hacer cambios con el mismo ID", style ={'text-align':'center', 'font-size':'0.8rem'}),

    html.Div(dbc.Input(id = "text-id"), id = "input-id", style = {'width': "10%", 'margin-left':'auto', 'margin-right':'auto'},),
    dbc.FormText(id = "text-generate-id", style ={'text-align':'center','margin-bottom':10, 'font-size':"2rem"} ),
    dbc.Spinner(children =    html.P(id = 'guardado', style ={'text-align':'center', 'font-size':'0.8rem'}), color="primary"),
    html.Div(children = [
        
        dbc.Button("Ingresar ID", id = "ingresar-id",color="warning", style = { 'margin-left':'auto', 'margin-right':0}, className = 'three columns'),
        dbc.Button("Generar ID", id = "generar-id" ,color="danger", style = { 'margin-left':10, 'margin-right':'auto'}, className = 'three columns', disabled=True),
        ],
        style = {'width': "100%", 'margin-left':'auto', 'margin-right':'auto', 'margin-top':10},
        className = 'row'
    ),
    html.Div(id='cache', style={'display': 'none'}),
    html.Div(id='nothing', style={'display': 'none'}),
    html.Footer(children= [
                                         html.Div(children = ['Hecho con ❤ por el ', html.A('CdP ESFM. ', href = "https://cdp.esfm-x.com", style ={'color': '#F9AA3A'})
                                                                 ], 
                                                style = {
                                                    'textAlign': 'center',
                                                    'margin': 10,
                                                    'margin-left': 'auto',
                                                    'margin-right': 'auto'
                                                 }
                                         ),
                                         html.Div(children= ['Datos obtenidos de ', html.A('Mis Profesores',href = 'https://www.misprofesores.com/escuelas/ESFM-IPN_1691', style ={'color': '#F9AA3A'}),
                                                                                            ' y ', 
                                                                                            html.A('ESFM',href = 'https://www.esfm.ipn.mx/assets/files/esfm/docs/HORARIOS.pdf', style ={'color': '#F9AA3A'}),
                                                                                            '. '],
                                                  style = {
                                                    'textAlign': 'center',
                                                    'margin': 10,
                                                    'margin-left': 'auto',
                                                    'margin-right': 'auto',
                                                    'margin-bottom':0
                                                 }
                                         
                                         )
     
                            ],
                                style={
                                        'width': "90%",
                                        'margin-left': 'auto',
                                        'margin-right': 'auto',
                                        'margin-top': 15
                                        
                                }
                    )

],style={'margin-top':0, 'background-color':'#343a40', 'color':'white'}
)