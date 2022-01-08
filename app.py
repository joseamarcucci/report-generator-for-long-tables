import pandas as pd
import numpy as np
import streamlit as st
import jinja2
import pdfkit
import datetime
import os
import platform

import tools
 

TABLE_TEMPLATE_FILE = 'template1.html'
BASE_HTML = os.path.join(os.getcwd(), 'static','html')
BASE_FIG = os.path.join(os.getcwd(), 'static','images')
PDF_TARGET_FILE = os.path.join(os.getcwd(), 'static','pdf', 'output.pdf') 
CSS_STYLE_FILE = './style.css'
AKTUELLES_JAHR = datetime.datetime.today().year + 1
settings = {}
WKHTMLTOPDF_WIN_PATH = 'C:\\apps\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'


def generate_report():
    def get_data():           
        df = pd.DataFrame(np.random.randint(0,100,size=(1000, 5)), columns=list('ABCDF'))
        return df

    def create_html_tables(report):
        def create_html_table(df, report, page):
            templateLoader = jinja2.FileSystemLoader(searchpath="./")
            templateEnv = jinja2.Environment(loader=templateLoader)
            template = templateEnv.get_template(report['html_template'])
            outputText = template.render(df=df)
            file_name = f"tab-{page}.html"
            file_name = os.path.join(BASE_HTML, f"tab-{page}.html")
            html_file = open(file_name, 'w', encoding='utf-8')
            html_file.write(outputText)
            html_file.close()
        
        row = 0
        for page in range(0, report['pages']):
            df_filtered = report['data'].iloc[row:row+report['rows_per_page']]
            if len(df_filtered) > 0:
                create_html_table(df_filtered, report, page)
    
    def create_pdf_files(pages):
        """
        all options, see: https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
        """
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None,
            'footer-right': '[page]/[topage]',
            'footer-line': None,
            'footer-left': '[isodate]',
            'footer-spacing': '10.0', 
            'header-spacing': '10.0', 
            'header-line': None, 
            'header-center': 'Report Header Line',
            'print-media-type': None
            }

        source_code = ''
        row=0
        for page in range(0, report['pages']):
            file_name = os.path.join(BASE_HTML, f"tab-{page}.html")
            if os.path.isfile(file_name):         
                #read html code to string
                html_file = open(file_name, 'r', encoding='utf-8')
                try:
                    source_code += html_file.read() 
                except Exception as ex:
                    print(f'{file_name} konnte nicht gelesen werden: {ex}')

                # write the page break
                source_code += '<div class="new-page"></div>'
            else:
                st.warning(f'{file_name} not found')

        if platform.system() == "Windows":
            pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', WKHTMLTOPDF_WIN_PATH))
        else:
            os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable) 
            WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], 
                stdout=subprocess.PIPE).communicate()[0].strip()
            pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)    
        
        pdfkit.from_string(source_code, PDF_TARGET_FILE, configuration=pdfkit_config, css=CSS_STYLE_FILE, options=options)
    
    def generate_download_link():
        basereport4_pdf = tools.get_base64_encoded_image(PDF_TARGET_FILE)
        st.markdown(tools.get_binary_file_downloader_html(PDF_TARGET_FILE), unsafe_allow_html=True)

    rows_per_page = st.number_input('Number of rows on page',30)
    df = get_data()
    report = {
        'html_template':'./template1.html',
        'data': df,
        'rows_per_page': rows_per_page,
        'pages': int(len(df) / rows_per_page)
    }

    st.markdown("Report generator")
    st.markdown("[git repo:](https://github.com/lcalmbach/report-generator-for-long-tables/)", unsafe_allow_html=True)
    st.write(report['data'].head())
    if st.button("Generate report"):
        with st.spinner('Creating report, this may take a while'):
            create_html_tables(report)
            create_pdf_files(report)
        st.success('PDF file was created successfully')
        generate_download_link()


if __name__ == '__main__':
    generate_report()

