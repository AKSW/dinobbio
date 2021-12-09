import csv, yaml, string

config = None
try:
    with open("./rdf-transformer/config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
except Exception as e:
    print('Exception when opening config.yaml' + ": %s\n" % e)

file = open("./rdf-transformer/nubbe.csv")
csvreader = csv.reader(file)
next(csvreader)
rows = []

# Generating metadata
for row in csvreader:
    columnIndx=0
    for column in row:
        if(columnIndx != 3 and columnIndx != 2 and columnIndx < 14 and row[columnIndx]):
            rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
            + ' <' + config['namespaces'][config['mappings'].split(' ')[columnIndx].split(':')[0]]
            + config['mappings'].split(' ')[columnIndx].split(':')[1] + '>'
            + ' "' + row[columnIndx] + '"'
            + ' .')
        columnIndx+=1
file.close()

file = open("./rdf-transformer/nubbe.csv")
csvreader = csv.reader(file)
next(csvreader)
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

file = open("./rdf-transformer/nubbe.csv")
csvreader = csv.reader(file)
next(csvreader)
# Generating classes

for row in csvreader:
    if(row[14]):
        row14 = row[14].split(';')
        i = 0
        for row14field in row14:
            if(i is 0):
                doi = row14field
                rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
                    + ' <' + config['namespaces'][config['mappings'].split(' ')[14].split(':')[0]]
                    + config['mappings'].split(' ')[14].split(':')[1] + '>'
                    + ' "' + doi.strip() + '"'
                    + ' .')
            if(i > 0):
                if(row14field.find('Atividades') is not -1):
                    bilogicalActivities = row14field.replace('Atividades Biológicas:','').split(',')
                    for biologicalActivity in bilogicalActivities:
                        rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
                        + ' <' + config['namespaces'][config['mappings'].split(' ')[15].split(':')[0]]
                        + config['mappings'].split(' ')[15].split(':')[1] + '>'
                        + ' "' + biologicalActivity.strip() + '"@en'
                        + ' .')
                if(row14field.find('Espécies') is not -1):
                    specieField = row14field.replace('Espécies:','')
                    specieLoc = specieField.split('[')
                    specie = specieLoc[0].strip()
                    rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
                        + ' <' + config['namespaces'][config['mappings'].split(' ')[16].split(':')[0]]
                        + config['mappings'].split(' ')[16].split(':')[1] + '>'
                        + ' "' + specie + '"'
                        + ' .')
                    if(len(specieLoc) > 1):
                        location = specieLoc[1].replace(']', '').strip()
                    location = location.replace('Local:', '').strip()
                    rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
                        + ' <' + config['namespaces'][config['mappings'].split(' ')[17].split(':')[0]]
                        + config['mappings'].split(' ')[17].split(':')[1] + '>'
                        + ' "' + location + '"'
                        + ' .')
                if(row14field.find('Tipo') is not -1):
                    collectionType = row14field.replace('Tipo:', '').strip()
                    rows.append("<" + config['namespaces']['nubberesource'] + row[0] + ">" 
                    + ' <' + config['namespaces'][config['mappings'].split(' ')[18].split(':')[0]]
                    + config['mappings'].split(' ')[18].split(':')[1] + '>'
                    + ' "' + collectionType.strip() + '"@en'
                    + ' .')
            i+=1
      
file.close()

f = open('nubbe.db.ttl', "w")
for row in rows:
    f.write(row + '\n')
f.close()
