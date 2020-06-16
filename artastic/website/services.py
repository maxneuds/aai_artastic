from SPARQLWrapper import SPARQLWrapper, JSON

def get_artwork(query):
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql/ArtOntology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT  ?d ?ab ?i ?la ?ml ?matl
        WHERE {
            ?a rdf:type :artwork ; 
            rdfs:label "%s" ;
            :description ?d;
            :abstract ?ab;
            :image ?i;
            :artist/rdfs:label ?la;
            :movement/rdfs:label ?ml;
            :material/rdfs:label ?matl;
        }
        Limit 1

    """ % query
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    return result

def get_artist(query):
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql/ArtOntology/sparql")
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
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql/ArtOntology/sparql")
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
