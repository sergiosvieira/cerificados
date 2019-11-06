import pyexcel_ods3 as pods
import json
import unidecode
#unaccented_string = unidecode.unidecode(accented_string)
input_file = open("modelo.tex", "r")
model = input_file.read()
data = pods.get_data("fonte.ods")
for i in data['Sheet1']:
    if len(i) == 0:
        continue
    name = i[0]
    task = i[1]
    title = i[2]
    filename = unidecode.unidecode(i[0]).replace(" ", "_").lower()
    output_file = open("_" + filename + ".tex", "a")
    output_file.write(model.replace("@name", name).replace("@task", task).replace("@title", title)) 
    output_file.close()
