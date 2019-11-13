import pyexcel_ods3 as pods
import json
import unidecode
import datetime

input_file = open("modelo.tex", "r")
model = input_file.read()
data = pods.get_data("fonte.ods")
for i in data['Sheet1']:
    if len(i) == 0:
        continue
    name = i[0]
    task = i[1]
    title = i[2]
    d = i[3]
    filename = unidecode.unidecode(i[0]).replace(" ", "_").lower()
    output_file = open("_" + filename + ".tex", "a")
    str_output = model.replace("@name", name).replace(
        "@task", task).replace("@title", title)
    formated_date = str(d)
    str_output = str_output.replace("@coursed", formated_date)
    output_file.write(str_output)
    output_file.close()
