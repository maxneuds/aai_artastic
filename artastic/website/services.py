from SPARQLWrapper import SPARQLWrapper, JSON


def get_artwork(query):
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT  ?label ?description ?abstract ?image ?artist ?movement ?material
        WHERE {
            ?a rdf:type :artwork ; 
            rdfs:label "%s" ;
            rdfs:label ?label;
            :description ?description;
            :abstract ?abstract;
            :image ?image;
            :artist/rdfs:label ?artist;
            :movement/rdfs:label ?movement;
            :material/rdfs:label ?material;
        }


    """ % query
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    return result


def get_artist(query):
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT  ?la ?l ?db ?pb ?dd ?pd
        WHERE { 
            ?a rdf:type :artwork ;
            rdfs:label ?l ;
            :artist/:date_of_birth ?db;
            :artist/:place_of_birth ?pb ;
            :artist/:date_of_death ?dd;
            :artist/:place_of_death ?pd ;
            :artist/rdfs:label ?la;
            :artist/rdfs:label "Leonardo da Vinci" . 
}

    """ % query
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    return result


def get_all(query):
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT ?property ?value
        WHERE {
            ?artist rdf:type :artwork ;
            rdfs:label "%s" ;
            ?property ?value .
        }

    """ % query
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    return result
