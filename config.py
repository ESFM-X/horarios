### Installed
from pandas import read_csv

df  = read_csv('./static/2022-1f.csv')

first = [{'label': '-','value':'all'}]
group_dict = [{'label': group,'value':group} for group in df['Grupo'].unique()]
group_dict = first + group_dict
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