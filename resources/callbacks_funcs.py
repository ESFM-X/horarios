### Installed
import dash_html_components as html
import dash_bootstrap_components as dbc
from pandas import DataFrame, concat
### Built in
import time
### Local
from config import (df, loc_list)
from core.DB import db
from .utils import (gen_id, get_groups_wa, traslapesd )

def open_input(clicks, texto, materia, ide):
    if clicks:
        if texto  == ["Aceptar"] or texto == ["Intentar de nuevo"]:
            return [dbc.Input(placeholder="Ingresar ID de 3 caracteres", type="text", id = 'text-id')]
        else:
            return [dbc.Input(value = ide,disabled =True, id = "text-id")]
    else:
        return [html.P(id = "text-id")]

def change_input(clicks, ide):
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

def set_dict(carrera):
    global group_dict
    first = [{'label': '-','value':'all'}]
    group_dict = [{'label': group,'value':group} for group in df[df["Programa"] == carrera]['Grupo'].unique()]
    group_dict = first + group_dict
    return group_dict

def set_2dict(carrera):
    global group_dict
    first = [{'label': '-','value':'all'}]
    group_dict = [{'label': materia,'value':materia} for materia in df[df["Programa"] == carrera]['Asignatura'].unique()]
    group_dict = first + group_dict
    return group_dict

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

def generate_table(semestre,carrera, dataframe = df, max_rows = 100):
    if semestre:
        if semestre != 'all':
            dataframe = dataframe[(dataframe["Programa"] == carrera) & (dataframe['Grupo'] == semestre)]
        else:
            dataframe = dataframe
        dataframe = dataframe.iloc[:,loc_list]
        return [[None], 
            [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, 
                                        hover = True, 
                                        borderless = True, dark = True)]
            ]

def generate_2table(materia,carrera, dataframe = df, max_rows = 100):
    if materia:
        dataframe = dataframe[(dataframe["Programa"] == carrera) & (dataframe['Asignatura']==materia)]

        dataframe = dataframe.iloc[:,loc_list]
        return [ [None,
            ], [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, hover = True, 
                                        borderless = True, dark = True)] ]

def generate_3table(materia_grupo,carrera, dataframe = df, max_rows = 100):
    
    dataframe = df[dataframe["Programa"] == carrera]
    new_df = DataFrame()
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
                
        new_df = concat([  new_df, df[(df["Programa"] == carrera) &  (df['Asignatura']== materia) & (df['Grupo']== grupo)]  ])
    if flag: 
        
        new_df['Grupo WA'] = grupo_wa
    dataframe = new_df
    
    try:
        dataframe = dataframe.iloc[:,loc_list + ([-1] if flag else [])]
    except:
        dataframe = df[df['Asignatura'] == '']
    
    dicc = dataframe.to_dict()
    diccionario_traslapes = traslapesd(dicc, list(dicc['Asignatura'].values()))
    if materia_grupo == []:
        dataframe =DataFrame(columns = ["Grupo", 'Asignatura', 'Profesor', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Calificación', 'Plataformas'])
    return [[None 
        ], [html.P( texto , style ={'text-align':'center','margin-bottom':1,'margin-top':1, 'font-size':"0.9rem", "color":"red"}) for texto in diccionario_traslapes],   [dbc.Table.from_dataframe(dataframe,responsive = True, striped = True, hover = True, borderless = True, dark = True)]]
