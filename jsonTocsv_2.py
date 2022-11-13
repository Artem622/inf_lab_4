file = open('table.json').read()
file_csv = open('csv_2','w')
data = file.split('{')
for i in range(len(data)):
    data[i] = data[i].replace('"',"'")
    data[i] = data[i].replace('\n','')
    data[i] = data[i].replace('       ','')
    data[i] = data[i].replace('    ','')
    if i > 2:
        file_csv.write('{')
        file_csv.write(data[i])
file_csv.close()


file = open('csv_2').read()
file = list(file)
file.pop(-1)
file.pop(-2)
file.pop(-3)
File = ''
for i in file:
    File += ''.join(i)
file_csv = open('table_2.csv','w')
file_csv.write('"')
file_csv.write(File)
file_csv.write('}')
file_csv.write('"')