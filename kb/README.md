# Querying

### Linux & Mac

Lifting a Web Client with the NuBBE RDF dataset and ontology.

#### 1) Python
Execute:
```
pip install kbox # install kbox latest version
kbox -server -kb "http://nubbe.db,http://nubbe.db/ontology" -install
```
Default Web Client: http://localhost:8080


### Windows, Linux & Mac

#### 2) Jar

* Download KBox jar file here: https://github.com/AKSW/KBox/releases/download/v0.0.2-alpha/kbox-v0.0.2-alpha.jar

* Execute:
```
java -jar kbox-v.0.0.2-alpha -server -kb "http://nubbe.db,http://nubbe.db/ontology" -install
```

Default Web Client: http://localhost:8080


#### 3) Docker
Execute:
```
docker pull aksw/kbox # install kbox latest version
docker aksw/kbox -server -kb "http://nubbe.db,http://nubbe.db/ontology" -install
```
Default Web Client: http://localhost:8080


For more information and commands, please visit the KBox project web-page: https://github.com/AKSW/KBox


