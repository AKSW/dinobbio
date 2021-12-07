import csv, yaml, string

config = None
try:
    with open("./rdf-transformer/config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
except Exception as e:
    print('Exception when opening config.yaml' + ": %s\n" % e)

file = open("./rdf-transformer/nubbe.csv")
csvreader = csv.reader(file)
rows = []

# Generating metadata
for row in csvreader:
    columnIndx=0
    for column in row:
        if(columnIndx != 3 and columnIndx < 14 and row[columnIndx]):
            rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
            + ' <' + config['namespaces'][config['mappings'].split(' ')[columnIndx].split(':')[0]]
            + config['mappings'].split(' ')[columnIndx].split(':')[1] + '>'
            + ' "' + row[columnIndx] + '"'
            + ' .')
        columnIndx+=1
file.close()

file = open("./rdf-transformer/nubbe.csv")
csvreader = csv.reader(file)
# Generating classes
for row in csvreader:
    if(row[3]):
        type = row[3].split(':')[len(row[3].split(':'))-1]
        if(type == ' -'):
            type = row[3].split(':')[len(row[3].split(':'))-2]
        rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
        + ' <' + config['namespaces'][config['mappings'].split(' ')[3].split(':')[0]]
        + config['mappings'].split(' ')[3].split(':')[1] + '>'
        + ' <' + config['namespaces']['nubberesource'] + type.title().replace(" ", "") + '>'
        + ' .')

file.close()
print(rows)

file = open("./rdf-transformer/nubbe.csv")
csvreader = csv.reader(file)
# Generating classes
for row in csvreader:
    if(row[3]):
        type = row[3].split(':')[len(row[3].split(':'))-1]
        if(type == ' -'):
            type = row[3].split(':')[len(row[3].split(':'))-2]
        rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
        + ' <' + config['namespaces'][config['mappings'].split(' ')[3].split(':')[0]]
        + config['mappings'].split(' ')[3].split(':')[1] + '>'
        + ' <' + config['namespaces']['nubberesource'] + type.title().replace(" ", "") + '>'
        + ' .')

file.close()
print(rows)
