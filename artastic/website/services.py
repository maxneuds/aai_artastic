from SPARQLWrapper import SPARQLWrapper, JSON


def get_artwork(data):
    _, label = extract_query_params(data)
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT  ?label ?description ?abstract ?image ?artist ?movement ?material
        WHERE {{
            ?a rdf:type :artwork ; 
            rdfs:label "{0}" ;
            rdfs:label ?label;
            :description ?description;
            :abstract ?abstract;
            :image ?image;
            :artist/rdfs:label ?artist;
            :movement/rdfs:label ?movement;
            :material/rdfs:label ?material;
        }}
    """.format(label)
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    return result


def get_artist(data):
    _, label = extract_query_params(data)
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT  ?la ?l ?db ?pb ?dd ?pd
        WHERE {{ 
            ?a rdf:type :artwork ;
            rdfs:label ?l ;
            :artist/:date_of_birth ?db;
            :artist/:place_of_birth ?pb ;
            :artist/:date_of_death ?dd;
            :artist/:place_of_death ?pd ;
            :artist/rdfs:label ?la;
            :artist/rdfs:label "{0}" . 
        }}
    """ .format(label)
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    return result


def get_all(data):
    obj_class, label = extract_query_params(data)
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT ?property ?value
        WHERE {{
            ?artist rdf:type :{0} ;
            rdfs:label "{1}" ; 
            ?property ?value .
        }}
    """.format(obj_class, label)
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    return result


def extract_query_params(data):
    obj_class = data.get('objClass')
    if not obj_class:
        obj_class = "artwork"
    label = data.get('label')
    return obj_class, label
