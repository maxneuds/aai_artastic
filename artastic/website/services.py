from SPARQLWrapper import SPARQLWrapper, JSON


def get_all(query):
    sparql = SPARQLWrapper("http://172.17.0.1:3030/ArtOntology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT ?property ?value
        WHERE {
            ?artist rdf:type :abstract_entity ;
            rdfs:label "%s" ;
            ?property ?value .
        }
     
    """ % (query)
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    return result
