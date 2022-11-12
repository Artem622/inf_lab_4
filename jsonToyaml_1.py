file_yaml = open('table.yaml', 'w')
f = open('table.json')
g = f.readline()
file = f.read()
data = file.split('{')
data = file.split('}')

for i in range(len(data)):

    data[i] = data[i].replace('','')
    data[i] = data[i].replace(',','')
    data[i] = data[i].replace('{','')
    data[i] = data[i].replace('}','')
    data[i] = data[i].replace('[','')
    data[i] = data[i].replace(']','')
    data[i] = data[i].replace('"2"',"- '2'")
    data[i] = data[i].replace('"4"',"- '4'")
    data[i] = data[i].replace('"6"',"- '6'")
    data[i] = data[i].replace('"8"',"- '8'")
    data[i] = data[i].replace('"10"',"- '10'")
    data[i] = data[i].replace('"12"',"- '12'")
    data[i] = data[i].replace('"14"',"- '14'")
    data[i] = data[i].replace('"16"',"- '16'")
    data[i] = data[i].replace('"1"',"- '1'")
    data[i] = data[i].replace('"3"',"- '3'")
    data[i] = data[i].replace('"5"',"- '5'")
    data[i] = data[i].replace('"7"',"- '7'")
    data[i] = data[i].replace('"9"',"- '9'")
    data[i] = data[i].replace('"11"',"- '11'")
    data[i] = data[i].replace('"13"',"- '13'")
    data[i] = data[i].replace('"15"',"- '15'")
    data[i] = data[i].replace('"17"',"- '17'")
    data[i] = data[i].replace('"', '')
    if len(data[i])>0:
        file_yaml.write(data[i]+'\n')
file_yaml.close()

f = open('table.yaml')
g = f.readline()
file = f.read()
file = file.replace('       ','   ')
file_yaml = open('table_yaml.yaml', 'w')
file_yaml.write('timetable:\n')
file_yaml.write(file)




