SERVER = 'pdstatasvsql03'
DATABASE = 'avstat_rttg'

PROXY_DICT = {'https': "http://dpdstatasvsql05:dpdstatasvsql05_@proxy1.bs.ch:3128"}

GRID_HEIGHT = 600
ERROR_CODE = '%ERROR%'
MONTH_NAMES = ['jan','feb','mrz','apr','mai','jun','jul','aug','sep','okt','nov','dez']

WKHTMLTOPDF_WIN_PATH = {
    'pdnb3094919':'C:\\apps\\wkhtmltopdf\\bin\\wkhtmltopdf.exe',
    'pdstatasvtweb04': 'e:\\app_install\\wkhtmltopdf\\bin\\wkhtmltopdf.exe',
    'pdstatasvpweb05': 'e:\\app_install\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
}
DASHBOARD_LST = [
    {'schluessel': 'einsaetze_bis_heute_vorjahresvergleich',
        'organisation': 5,
        'name': 'Vergleich Einsätze bis heute',
        'beschreibung':"""Anzahl und Summe der Gesamteinsatzzeit der Einsätze für die ausgewählte Organisation.
        """,
        'vergleichswert_feld': 'abweichung',
        'vergleichswert_richtung_ueberschreitgung': 1,
        'vergleichswert': 20,
        'query':'v_kz_einsaetze_nach_org_mit_vorjahr_per_heute',      
    },
]

BERICHTE_LST = [ 
    {'schluessel': 'bericht2',
    'organisation': 5,
    'name_kurz': 'Simultaneinsätze',
    'name': 'Einsätze, die im Einzugsgebiet einer anderen Organisation gefahren werden.',
    'beschreibung':"""Der Bericht enthält eine Tabelle pro Kombination von Organisation für Einsatz und Zuständigkeit. 
Die Anzahl Einsätze sind nach P-/S-Typ und Dringlichkeit (P1, P2, S1, S2 etc.) aufgeschlüsselt. Pro Monat wird eine Zeile angezeigt""",
    'titel': 'Simultaneinsätze {}',
    'query':'bericht_simultaneinsaetze',
    'group_feld': 'gruppe',
    'tabellen_felder':['Monat','P1','P2','P3','S1','S2','S3','Andere','Total'],
    'html_template': 'template2.html'
    },
]

MAP_LEGEND_SYMBOL_SIZE: int = 10
MAPBOX_STYLE: str = "mapbox://styles/mapbox/light-v10"
GRADIENT: str = 'blue-green'
TOOLTIP_FONTSIZE = 'x-small'
TOOLTIP_BACKCOLOR = 'white'
TOOLTIP_FORECOLOR = 'black'
default_plot_width = 600
default_plot_height = 400

# https://www.schemecolor.com/rainbow-tones.php
COLOR_SCHEMAS = {
    'rainbow tones': {
        'red': {'hex': '#EC2029', 'r': 236, 'g': 32, 'b': 41},
        'orange': {'hex': '#FA7909', 'r': 250, 'g': 121, 'b': 9},
        'yellow': {'hex': '#F6E60B', 'r': 246, 'g': 230, 'b': 11},
        'green': {'hex': '#0F9944', 'r': 15, 'g': 153, 'b': 68},
        'sapphire': {'hex': '#0356C2', 'r': 3, 'g': 86, 'b': 194},
        'indigo': {'hex': '#4F058C', 'r': 79, 'g': 5, 'b': 140},
        'LightGray': {'hex': '#D3D3D3', 'r': 211, 'g': 211, 'b': 211}
    }
}

STAMMDATEN = r'.\static\stammdaten\stammdaten.xlsx'
DATE_FORMAT_DMY = "%d.%m.%Y"

