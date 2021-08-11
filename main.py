from __future__ import print_function
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

import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
external_stylesheets = [dbc.themes.BOOTSTRAP]

cred = credentials.Certificate("./horario-f7ff5-firebase-adminsdk-xebih-c86b730d5a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
###############################################################################
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SPREADSHEET_ID = '16_jhdhBcgBVSwtFpl_BGEHOwJObfEeO_wCs-Nqw3fSY'
###############################################################################
df  = pd.read_csv('2022-1f.csv')
app = dash.Dash(__name__, external_stylesheets = external_stylesheets,suppress_callback_exceptions=True, 
                update_title= None, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=0.8"}])
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
    'width': '90%'

}
style_bar = {  
    'border-top-style': 'double',
    'border-top-color': '#f9aa3a',#'#1866B9',
    'width': '90%',
    'margin-left': 'auto',
    'margin-right': 'auto'
}
app.layout = html.Div( children = [
    html.Header(
        children = [html.Img (src="https://i.ibb.co/dcJMCTP/Logotipo-Final-Negro.png", 
                    style = {"margin-bottom":0, "display":"block","width": '70%', "height": "auto", "margin-left": "auto", "margin-right": "auto", "padding-top": 1,"margin-bottom": 0,"text-align":"center", 'padding-top':30}),
                    html.H3('Información de horarios 2022-1', style={'margin-bottom':0, 'margin-top':10}),html.Br()],
        style= {
           # 'backgroundColor': '#79003E',#colors['text'],#colors['background'],
            'color': '#f9aa3a',#'#FFFFFF',#colors['text'],
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
            children = dcc.Dropdown(id = 'Semestre', #options = group_dict,
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
                                            #'margin':80,
                                            #'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            #'margin-bottom':40,
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
    

    #html.P("(Beta) El ID te permite recordar tu selección de horario.", style ={'text-align':'center'}),
    html.Div(dbc.Input(id = "text-id"), id = "input-id", style = {'width': "10%", 'margin-left':'auto', 'margin-right':'auto'},),
    dbc.FormText(id = "text-generate-id", style ={'text-align':'center','margin-bottom':10, 'font-size':"2rem"} ),
    dbc.Spinner(children =    html.P(id = 'guardado', style ={'text-align':'center', 'font-size':'0.8rem'}), color="primary"),
    #dbc.FormText("El ID te permite recordar tu selección de horario.", style ={'text-align':'center'}),
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
                                        #'border-top-style': 'double',
                                        #'border-top-color': '#1866B9',
                                        'margin-left': 'auto',
                                        'margin-right': 'auto',
                                        'margin-top': 15
                                        
                                }
                    )


   

],style={'margin-top':0, 'background-color':'#343a40', 'color':'white'}
)
def get_groups_wa(carrera, grupo, asignatura):
    
    if carrera == 'LIM':
        RANGE_NAME = 'LIM!A4:D118'
    elif carrera == 'LFM':
        RANGE_NAME = 'LFM!A4:D176'
    else:
        RANGE_NAME = 'LMA!A4:D27'

    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME).execute()
    values = result.get('values', []) 
    if not values:
        return None
    else:
        for row in values:
            
            if row[0] == grupo and row[1] == asignatura:
                return row
            if int(row[0][0]) > int(grupo[0]):
                return None
        return None

def traslapesd(dfdic2, materias):
    def limpiador(dic):
        """
        @Rudolph
        Recibe un diccionario con los horarios de las asignaturas de cada día 
        """
        llaves = dic.keys()
        horasini=[]
        horasfin=[]
        traslape = []
        bandera=2
        for llave in llaves:
            if dic[llave] != '\xa0' and type(dic[llave]) != float and dic[llave] != '\n':
                print(dic[llave].replace('\n', ''), llave)
                if '-' in dic[llave]:
                    inicio,final = dic[llave].replace('.', ':').split("-")
                else:
                    #print('entraste')
                    inicio, final = dic[llave].replace('.', ':').split("\n")
                hinicio,hfinal = float(inicio.split(":")[0]),float(final.split(":")[0])
                minicio,mfinal = float(inicio.split(":")[1])/60,float(final.split(":")[1])/60
                horasini.append([hinicio+minicio,hfinal+mfinal])
            else:
                horasini.append([])
        return horasini
    
    dias = ['Lun','Mar','Mie','Jue','Vie']
    dias2 = {llave: dia.lower() for llave,dia in zip(['Lun','Mar','Mie','Jue','Vie'], ['Lunes','Martes','Miércoles','Jueves','Viernes'])}
    
    dictionary = {dias2[llave]: limpiador(dfdic2[llave]) for llave in dias}

    llaves = dictionary.keys()
    lista = []
    traslapes = []
    for llave in llaves:
        for x in range(len(dictionary[llave])):
            for y in range(len(dictionary[llave])):
                bandera = 0
                if x == y or  dictionary[llave][x]==[]or  dictionary[llave][y]==[]:
                    pass
                else:
                    
                    if dictionary[llave][x][0]>=dictionary[llave][y][0] and dictionary[llave][x][0]<dictionary[llave][y][0]:    
                        bandera = 1
                    elif dictionary[llave][x][1]>dictionary[llave][y][0]  and dictionary[llave][x][1]<=dictionary[llave][y][1]:
                        bandera = 1
                    if bandera == 1:
                        
                        x0 = dictionary[llave][x][0]
                        x1 = dictionary[llave][x][1]
                        y0 = dictionary[llave][y][0]
                        y1 = dictionary[llave][y][1]

                        iniciox = str(int(x0)) + ':00' if x0%1==0 else str(int(x0)) +':'+str(int((x0%1)*60))
                        inicioy = str(int(y0)) + ':00' if y0%1==0 else str(int(y0)) +':'+str(int((y0%1)*60))
                        finalx = str(int(x1)) + ':00' if x1%1==0 else str(int(x1)) +':'+str(int((x1%1)*60))
                        finaly = str(int(y1)) + ':00' if y1%1==0 else str(int(y1)) +':'+str(int((y1%1)*60))
                        
                        tsp =  f'Hay traslapes los {llave} con {materias[x]} de {iniciox + " - " + finalx} y {materias[y]} de {inicioy + " - " + finaly} '
                        if set([materias[x], materias[y], llave]) not in traslapes: 
                            traslapes.append(set([materias[x], materias[y], llave]))
                            lista.append(tsp)
                        
    return lista

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
            [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, 
                                        hover = True, #bordered = True,
                                        borderless = True, dark = True)]
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

            ], [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, hover = True, #bordered = True,
                                        borderless = True, dark = True)] ]

@app.callback([Output('third_table','children'),Output('traslapes','children'), Output('table-prueba', 'children')],[Input('Materia_y_grupo','value'),Input('Carrera','value')])
def generate_3table(materia_grupo,carrera, dataframe = df, max_rows = 100):
    
    dataframe = df[dataframe["Programa"] == carrera]
    new_df = pd.DataFrame()
    grupo_wa = []
    flag = 0
    for materia_g in materia_grupo:
        materia = materia_g.split('*')[0]
        try:
            grupo = materia_g.split('*')[1]
        except:
            grupo = ''
        
        row = get_groups_wa(carrera, grupo, materia)
        if row:
            if len(row) == 4:
                flag = 1
                grupo_wa.append(html.A(f'{row[3][:30]}...', href = row[3]))
            else:
                grupo_wa.append('')
                
        new_df = pd.concat([  new_df, df[(df["Programa"] == carrera) &  (df['Asignatura']== materia) & (df['Grupo']== grupo)]  ])
    if flag: 
        
        new_df['Grupo WA'] = grupo_wa
    dataframe = new_df
    
    try:
        dataframe = dataframe.iloc[:,loc_list + ([-1] if flag else [])]
    except:
        dataframe = df[df['Asignatura'] == '']
    
    if True:
        
    #     dataframe = dataframe[(dataframe['Programa']==carrera) & (dataframe['Unidad de aprendizaje']==materia)]

    #     dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,[0,1,3,5,6,7,8,9,10,16]]
        dicc = dataframe.to_dict()
        diccionario_traslapes = traslapesd(dicc, list(dicc['Asignatura'].values()))
        #diccionario_traslapes = traslape(dataframe.loc[:,['Lun', 'Mar','Mie', 'Jue', 'Vie']].to_dict())
        if materia_grupo == []:
            dataframe = pd.DataFrame(columns = ["Grupo", 'Asignatura', 'Profesor', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Calificación', 'Plataformas'])
        

        return [[None 
            # html.Thead(
            #         html.Tr([html.Th(col) for col in dataframe.columns])
            #     ),

            #     html.Tbody([html.Tr([
            #             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            #         ], style = {'height':40}) for i in range(min(len(dataframe), max_rows))
            #     ], style = {'color':'#414242' })

            ], [html.P( texto , style ={'text-align':'center','margin-bottom':1,'margin-top':1, 'font-size':"0.9rem", "color":"red"}) for texto in diccionario_traslapes],   [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, hover = True, borderless = True, dark = True)]]

if __name__ == '__main__':
    app.run_server(debug = True)