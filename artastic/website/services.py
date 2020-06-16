from SPARQLWrapper import SPARQLWrapper, JSON


def get_all(data):
    obj_class = data.get('objClass')
    if not obj_class:
        obj_class = "artwork"
    label = data.get('label')
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
