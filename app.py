import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import time
external_stylesheets = [dbc.themes.BOOTSTRAP]

cred = credentials.Certificate("./horario-f7ff5-firebase-adminsdk-xebih-c86b730d5a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

df  = pd.read_csv('2021-3.csv')
app = dash.Dash(__name__, external_stylesheets = external_stylesheets,suppress_callback_exceptions=True)
server = app.server
first = [{'label': '-','value':'all'}]
group_dict = [{'label': group,'value':group} for group in df['Grupo'].unique()]
group_dict = first + group_dict
app.title = 'ESFM | Horario'
loc_list = [1,2,3,6,7,8,9,10,12,14]
colors = {
    'text': '#1866B9',
    'background': '#FFFFFF'
}

style_subtitles= {
    'margin-left':"5%",
    'margin-right':'auto',
    'width': 300

}
style_bar = {  
    'border-top-style': 'double',
    'border-top-color': '#7b1448',#'#1866B9',
    'width': '90%',
    'margin-left': 'auto',
    'margin-right': 'auto'
}
app.layout = html.Div( children = [
    html.Header(
        children = [html.Img (src="https://fotos.subefotos.com/076df224d0bb0b75749aa140d0c955afo.png", 
                    style = {"margin-bottom":0,'min-width':350, "display":"block","width": '55%', "height": "auto", "margin-left": "auto", "margin-right": "auto", "margin-top": 1,"margin-bottom": 0,"text-align":"center", 'padding-top':30}),
                    html.H2('Información de horarios ', style={'font-size':"2.2rem",'margin-bottom':0, 'margin-top':10}),html.P(children = 'Página no oficial del IPN', style = {'color':'#959595'}), html.Br()],
        style= {
           # 'backgroundColor': '#79003E',#colors['text'],#colors['background'],
            'color': '#7b1448',#'#FFFFFF',#colors['text'],
            'margin-top':0,
            'margin-bottom':0,
            'margin-left':'auto',
            'margin-right':'auto',
            'text-align':'center',
            'margin-left':0,
            'height':"30%"
            #'width':730
        }
    ),
    # html.Div(style= {
    #         'backgroundColor': '#79003E',#colors['text'],#colors['background'],
    #         'height':10,
    #         'margin-left':30,
    #         ''
    #         }
    # ),
    html.P('ESFM ha estado modificando los horarios, revisa si hay algún cambio en el tuyo.', style = {
                                                                                       'margin-left':100,
                                                                                       'margin-right':'auto',
                                                                                       'width': "80%",
                                                                                        'margin-right':100,
                                                                                        'font-size':'0.8rem'}
          ),
    html.H3(children = 'Filtrar por grupo', style = style_subtitles),
  
    html.Div('', style = style_bar),
    html.Div(children = [
        html.Div(
            children = dcc.Dropdown(id = 'Carrera', options = [{'label':'Ingeniería Matemática',
                                                                'value':'LIM'},
                                                                {'label':'Física y Matemáticas',
                                                                'value':'LFM'},
                                                                {'label':'Matemática Algorítmica',
                                                                'value':'LMA'}
                                                                ],
                                                    value = 'LIM',
                                                    searchable = False,
                                                    clearable = False),
            style = {
                'margin':40,
                'width': "40%",
                'margin-bottom':10,
                'margin-top': 20,
                'margin-right':10
                
            },
            className = 'six columns'
        
        ),
        html.Div(
            children = dcc.Dropdown(id = 'Semestre', #options = group_dict,
                                                    value = '1MV2',
                                                    searchable = False,
                                                    clearable = False,
                                                    placeholder = "Selecciona una opción"),
            style = {
                'margin':40,
                'width': 150,
                'margin-top':20,
                'margin-bottom':20,
                'margin-left':0
            },
            className = 'six columns'
    
    )],className = 'row', style = {'width': 500, 'margin-left':'auto', 'margin-right':'auto'}),

    html.Table(id = 'First_table',style = {
                                            'textAlign': 'center',
                                            #'margin':80,
                                            #'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            #'margin-bottom':40,
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
    # html.Div(
    #     children = dcc.Dropdown(id = 'Carrera_2', options = [{'label':'Ingeniería Matemática',
    #                                                         'value':'LIM'},
    #                                                         {'label':'Física y Matemáticas',
    #                                                         'value':'LFM'}
    #                                                         ],
    #                                             value = 'LIM',
    #                                             searchable = False,
    #                                             clearable = False),
    #     style = {
    #         'margin':40,
    #         'width': 200,
    #         'margin-bottom':10,
    #         'margin-top': 20,
    #         'margin-right':10
    #     },
    #     className = 'six columns'
    
    # ),
    html.Div(
        children = dcc.Dropdown(id = 'Materia', #options = group_dict,
                                                value = '1MV2',
                                                #searchable = False,
                                                clearable = False,
                                                placeholder = "Selecciona una opción"),
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
                                            #'margin':80,
                                            #'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            #'margin-bottom':40,
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
        #html.Div(
        #    children = dcc.Dropdown(id = 'Carrera_3', options = [{'label':'Ingeniería Matemática',
        #                                                        'value':'LIM'},
         #                                                       {'label':'Física y Matemáticas',
         #                                                       'value':'LFM'}
         #                                                       ],
         #                                           value = 'LIM',
         #                                           searchable = False,
         #                                           clearable = False),
        #     style = {
        #         'margin':40,
        #         'width': 200,
        #         'margin-bottom':10,
        #         'margin-top': 20,
        #         'margin-right':10
        #     },
        #     className = 'two columns'
        
        # ),
        html.Div(
            children = dcc.Dropdown(id = 'Materia_y_grupo', #options = group_dict,
                                                    value = ['1MV2','0'],
                                                    #searchable = False,
                                                    multi=True,
                                                    clearable = True,
                                                    placeholder = "Selecciona una opción"),
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
    html.Div(id = "traslapes", style = {'margin-bottom':10, 'padding-bottom':1}),
    html.Table(id = 'third_table',style = {
                                            'textAlign': 'center',
                                            #'margin':80,
                                            #'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            #'margin-bottom':40,
                                            'width': "80%",
                                            'height':'auto'
                                           }
    ),
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
   
    html.P("Organiza tu horario y después genera un ID.", style ={'text-align':'center', 'margin-bottom':1, 'font-size':'0.8rem'}),
    html.P("Podrás recuperar tu horario y hacer cambios con el mismo ID.", style ={'text-align':'center', 'font-size':'0.8rem'}),
    

    #html.P("(Beta) El ID te permite recordar tu selección de horario.", style ={'text-align':'center'}),
    html.Div(dbc.Input(id = "text-id"), id = "input-id", style = {'width': "10%", 'margin-left':'auto', 'margin-right':'auto'},),
    dbc.FormText(id = "text-generate-id", style ={'text-align':'center','margin-bottom':10, 'font-size':"2rem"} ),
    dbc.Spinner(children =    html.P(id = 'guardado', style ={'text-align':'center', 'font-size':'0.8rem'}), color="primary"),
    #dbc.FormText("El ID te permite recordar tu selección de horario.", style ={'text-align':'center'}),
    html.Div(children = [
        
        dbc.Button("Ingresar ID", id = "ingresar-id",color="success", style = { 'margin-left':'auto', 'margin-right':0}, className = 'three columns'),
        dbc.Button("Generar ID", id = "generar-id" ,color="primary", style = { 'margin-left':10, 'margin-right':'auto'}, className = 'three columns', disabled=True),
        ],
        style = {'width': "100%", 'margin-left':'auto', 'margin-right':'auto', 'margin-top':10},
        className = 'row'
    ),
    html.Div(id='cache', style={'display': 'none'}),
    html.Div(id='nothing', style={'display': 'none'}),
    html.Footer(children= [
                                         html.Div(children = ['Hecho con ❤ por el CdP ESFM. '
                                                                 ], 
                                                style = {
                                                    'textAlign': 'center',
                                                    'margin': 10,
                                                    'margin-left': 'auto',
                                                    'margin-right': 'auto'
                                                 }
                                         ),
                                         html.Div(children= ['Datos obtenidos de ', html.A('Mis Profesores',href = 'https://www.misprofesores.com/escuelas/ESFM-IPN_1691'),
                                                                                            ' y ', 
                                                                                            html.A('ESFM',href = 'https://www.esfm.ipn.mx'),
                                                                                            '. '],
                                                  style = {
                                                    'textAlign': 'center',
                                                    'margin': 10,
                                                    'margin-left': 'auto',
                                                    'margin-right': 'auto'
                                                 }
                                         
                                         )
     
                            ],
                                style={
                                        'width': "90%",
                                        #'border-top-style': 'double',
                                        #'border-top-color': '#1866B9',
                                        'margin-left': 'auto',
                                        'margin-right': 'auto',
                                        'margin-top': 15
                                        
                                }
                    )


   

],style={'margin-top':0}
)

def traslape(a_dic):
    dias_dic = {'Lun':'lunes', 'Mar':'martes', 'Mie':'miércoles', 'Jue':'jueves','Vie':'viernes'}
    def intervalo_maker(x):
        x = str(x)
        if len(x) > 8:
            x1,x2 = x.split('-')

            x11,x12 = x1.split(':') 
            x21,x22 = x2.split(':') 

            num1 = int(x11) + int(x12)/60
            num2 = int(x21) + int(x22)/60
        else:
            num1 = num2 =  0
        return [num1, num2]
    def desintervalo(x):
        x = str(x)
        x1,x2 = x.split('.')
        return x1 + ':' + str(str(int(x2)*60) + str(0))[0:2]
        
    traslapes = {}
    for dia, horario in a_dic.items():
        intervalos = []
        
        for hora in horario.values():
            intervalos.append(intervalo_maker(hora))
        for intervalo1 in range(len(intervalos)):
            for intervalo2 in range(intervalo1+1, len(intervalos)):
                if intervalos[intervalo1][0] >= intervalos[intervalo2][0] and intervalos[intervalo1][0] < intervalos[intervalo2][1]:
                    llave =  str(dia) + str(intervalos[intervalo2][0]) + str(intervalos[intervalo1][0])
                    if llave not in traslapes: 
                        traslapes[llave] = f"Hay traslapes los {dias_dic[dia]} de {desintervalo(intervalos[intervalo2][0])} - {desintervalo(intervalos[intervalo1][1])}"
                        
    return traslapes

@app.callback(Output('input-id','children'),[Input('ingresar-id','n_clicks'), Input('ingresar-id','children'), State('Materia_y_grupo','value'),State('text-id','value')], prevent_initial_call=True)
def open_input(clicks, texto, materia, ide):
    if clicks:
        if texto  == ["Aceptar"] or texto == ["Intentar de nuevo"]:
            return [dbc.Input(placeholder="Ingresar ID de 3 caracteres", type="text", id = 'text-id')]
        else:
            #if materia != []:
                #users_ref = db.collection(u'ides')
                #docc = users_ref.document(ide)
                #docc.update({"Horario": materia })
            return [dbc.Input(value = ide,disabled =True, id = "text-id")]
    else:
        return [html.P(id = "text-id")]

@app.callback(Output('ingresar-id','children'),[Input('ingresar-id','n_clicks'),State('text-id','value')])
def change_input(clicks, ide):
    #print("*****", ide)
    
    if clicks:
        if clicks<2:
            return ["Aceptar"]
        else:
            users_ref = db.collection(u'ides')
            docs = users_ref.stream()
            ides = [i.id for i in docs]
            if ide not in ides:
                return["Intentar de nuevo"]
            else:
                return ["Guardar cambios"]
    else:
        return ["Ingresar ID"]


@app.callback([Output('Materia_y_grupo','value'),Output('guardado','children')],[Input('ingresar-id','children'),State('text-id','value'), State('Materia_y_grupo', 'value')])
def display_table(ingresar, ide, materia):
    
    if ingresar ==  ["Guardar cambios"]:
        if materia != []:
            users_ref = db.collection(u'ides')
            docc = users_ref.document(ide)
            docc.update({"Horario": materia })
        users_ref = db.collection(u'ides')
        query_ref = users_ref.where(u'ID', u'==', ide)
        for doc in query_ref.stream():
            materias = doc.to_dict()['Horario']
        if materia == materias: 
            time.sleep(0.5)
            return [materias, '✔️ Guardado exitoso']
        else:
            return [materias, None]
    else:
        return [[], None]

def gen_id():

    a =  random.choice('qwertyuiopasdfghjklñzxcvbnm1234567890') + random.choice('qwertyuiopasdfghjklñzxcvbnm1234567890') + random.choice('qwertyuiopasdfghjklñzxcvbnm1234567890')
    return a.upper()

@app.callback([Output('Materia_y_grupo','disabled'),Output('text-generate-id','children'),Output('generar-id','disabled'),Output('ingresar-id','disabled'), Output('cache', 'children')],[Input('Materia_y_grupo','value'), Input('ingresar-id','children'),Input('generar-id','n_clicks'), Input('Materia_y_grupo','value'), State('generar-id','disabled')])
def generate_disabled(materia_grupo, ingresar, n_clicks, opciones, ide):

    if n_clicks:
        ides = gen_id()
        users_ref = db.collection(u'ides')
        docs = users_ref.stream()
        ids = [i.id for i in docs]
        
        while  ides in ids:
            ides = gen_id()
        
        coleccion = db.collection('ides').document(ides) 
        coleccion.set({'ID':ides, 'Horario': opciones })
        return [True,ides, True, True,['1']]
    else:
        if materia_grupo != ['1MV2', '0'] and materia_grupo != [] and ingresar == ["Ingresar ID"]:
            return [False,[],False, False,['0']]
        else:
            return [False,[],True, False,['0']]


@app.callback(Output('Semestre','options'),[Input('Carrera','value')])
def set_dict(carrera):
    global group_dict
    first = [{'label': '-','value':'all'}]
    group_dict = [{'label': group,'value':group} for group in df[df["Programa"] == carrera]['Grupo'].unique()]
    group_dict = first + group_dict
    return group_dict

@app.callback(Output('Materia','options'),[Input('Carrera','value')])
def set_2dict(carrera):
    global group_dict
    first = [{'label': '-','value':'all'}]
    group_dict = [{'label': materia,'value':materia} for materia in df[df["Programa"] == carrera]['Asignatura'].unique()]
    group_dict = first + group_dict
    return group_dict

@app.callback(Output('Materia_y_grupo','options'),[Input('Carrera','value')])
def set_3dict(carrera):
    group_dict = []
    df2 = df[df["Programa"] == carrera]
    df3 = df2.reset_index()
    first = [{'label': '-','value':'all'}]
    for ind in range(df3.shape[0]):
        grupo = df3.loc[ind,'Grupo']
        materia = df3.loc[ind,'Asignatura']
        group_dict.append( {'label': materia +' '+ grupo,'value':materia+'*'+grupo})
    group_dict = first + group_dict
    return group_dict

@app.callback([Output('First_table','children'), Output('First_table2', 'children')], [Input('Semestre','value'),Input('Carrera','value')])
def generate_table(semestre,carrera, dataframe = df, max_rows = 100):
    if semestre:
        if semestre != 'all':
            dataframe = dataframe[(dataframe["Programa"] == carrera) & (dataframe['Grupo'] == semestre)]
        else:
            dataframe = dataframe
        dataframe = dataframe.iloc[:,loc_list]
        return [[None], 
            # html.Thead(
            #         html.Tr([html.Th(col) for col in dataframe.columns])
            #     ),

            #     html.Tbody([html.Tr([
            #             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            #         ], style = {'height':40}) for i in range(min(len(dataframe), max_rows))
            #     ], style = {'color':'#414242' , 'width': 200})
            [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, hover = True)]
            ]

@app.callback([Output('second_table','children'), Output('second_table2', 'children')],[Input('Materia','value'),Input('Carrera','value')])
def generate_2table(materia,carrera, dataframe = df, max_rows = 100):
    if materia:
        dataframe = dataframe[(dataframe["Programa"] == carrera) & (dataframe['Asignatura']==materia)]

        dataframe = dataframe.iloc[:,loc_list]
        return [ [None,
            # [ html.Thead(
            #         html.Tr([html.Th(col) for col in dataframe.columns])
            #     ),

            #     html.Tbody([html.Tr([
            #             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            #         ], style = {'height':40}) for i in range(min(len(dataframe), max_rows))
            #     ], style = {'color':'#414242' })

            ], [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, hover = True)] ]

@app.callback([Output('third_table','children'),Output('traslapes','children'), Output('table-prueba', 'children')],[Input('Materia_y_grupo','value'),Input('Carrera','value')])
def generate_3table(materia_grupo,carrera, dataframe = df, max_rows = 100):
    
    dataframe = df[dataframe["Programa"] == carrera]
    new_df = pd.DataFrame()
    for materia_g in materia_grupo:
        materia = materia_g.split('*')[0]
        try:
            grupo = materia_g.split('*')[1]
        except:
            grupo = ''

        new_df = pd.concat([  new_df, df[(df["Programa"] == carrera) &  (df['Asignatura']== materia) & (df['Grupo']== grupo)]  ])
    
    dataframe = new_df
    
    try:
        dataframe = dataframe.iloc[:,loc_list]
    except:
        dataframe = df[df['Asignatura'] == '']
    
    if True:
        
    #     dataframe = dataframe[(dataframe['Programa']==carrera) & (dataframe['Unidad de aprendizaje']==materia)]

    #     dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,[0,1,3,5,6,7,8,9,10,16]]
        diccionario_traslapes = traslape(dataframe.loc[:,['Lun', 'Mar','Mie', 'Jue', 'Vie']].to_dict())
        if materia_grupo == []:
            dataframe = pd.DataFrame(columns = ["Grupo", 'Asignatura', 'Profesor', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Calificación', 'Correo'])
        return [[None 
            # html.Thead(
            #         html.Tr([html.Th(col) for col in dataframe.columns])
            #     ),

            #     html.Tbody([html.Tr([
            #             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            #         ], style = {'height':40}) for i in range(min(len(dataframe), max_rows))
            #     ], style = {'color':'#414242' })

            ], [dbc.FormText( texto , style ={'text-align':'center','margin-bottom':1,'margin-top':1, 'font-size':"0.9rem", "color":"red"}) for texto in diccionario_traslapes.values()],   [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, hover = True)]]

if __name__ == '__main__':
    app.run_server(debug = True)