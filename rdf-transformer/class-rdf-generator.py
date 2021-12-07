import csv, yaml, string

file = open("./rdf-transformer/nubbe.csv")
csvreader = csv.reader(file)
classDic = {}
rows = ""
# Generating classes
for row in csvreader:
    if(row[3]):
        type = row[3].split(':')[len(row[3].split(':'))-1]
        superClass = None
        if(type == ' -'):
            type = row[3].split(':')[len(row[3].split(':'))-2]
        else:
            superClass = row[3].split(':')[len(row[3].split(':'))-2]
            superClass = superClass.title().strip().replace(" ", "")
        label = type.title().strip()
        clazz = label.replace(" ", "")
        if(clazz not in classDic):
            rows += '\n'
            rows += '\n'
            comment = "A " + label + "."
            try:
                f = open('./rdf-transformer/class.template', 'r')
                class_statement = f.read()
                class_statement = class_statement.replace("{class}", clazz)
                if(superClass):
                    class_statement = class_statement.replace("{superClass}", superClass)
                else:
                    class_statement = class_statement.replace('  rdfs:subClassOf :{superClass};\n','')
                class_statement = class_statement.replace("{label}", label)
                class_statement = class_statement.replace("{comment}", comment)
                rows += class_statement
                classDic[clazz] = clazz
            except Exception as e:
                print("Exception when generating class: %s" % e)

file.close()

classes_file = "auto_generated_classes.ttl"
print('registering classes at ' + classes_file)
f = open(classes_file, "w")
f.write(rows)
f.close()
