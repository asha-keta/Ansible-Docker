from json2html import *
import json
import sys
import ast
import csv
import pandas as pd
from pandas.io.json import json_normalize

fileName = sys.argv[1]
output_file = sys.argv[2]
#data = pd.read_json(fileName)
#df = pd.DataFrame.from_dict(data, orient='index')
#html_data = df.to_html()
#print(html_output)

with open(fileName) as file:
    json_data = json.load(file)
html_data = json2html.convert(json = json_data)
html_file= open(output_file,"w")
html_file.write("<!DOCTYPE html>")
html_file.write("<html>")
html_file.write("<body>")
html_file.write("<h2>Linux Server discovery</h2>")
html_file.write("<div id= {{ fileName }} class=tabcontent>")
html_file.write(html_data)
html_file.write("</div>")
html_file.write("<div id=London class=tabcontent>")
html_file.write(html_data)
html_file.write("</div>")
html_file.write("</body>")
html_file.write("</html>")
#html_file.write(data)
html_file.close()

