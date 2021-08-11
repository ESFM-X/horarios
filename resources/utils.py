### Installed 
from googleapiclient.discovery import build
from google.oauth2 import service_account
### Built in
from random import choice

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './private/keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SPREADSHEET_ID = '16_jhdhBcgBVSwtFpl_BGEHOwJObfEeO_wCs-Nqw3fSY'

def gen_id():
    a =  choice('qwertyuiopasdfghjklñzxcvbnm1234567890') + choice('qwertyuiopasdfghjklñzxcvbnm1234567890') + choice('qwertyuiopasdfghjklñzxcvbnm1234567890')
    return a.upper()
    
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
