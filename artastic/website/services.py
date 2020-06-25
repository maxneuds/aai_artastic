from SPARQLWrapper import SPARQLWrapper, JSON
import spacy


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
    print(result)
    search_words = search_result(result)
    return {
        "result": result,
        "searchWords": search_words
    }


def get_artist(data):
    _, label = extract_query_params(data)
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT  ?label ?description ?image ?abstract ?wikilink ?gender ?dateOfBirth ?dateOfDeath ?placeOfBirth ?placeOfDeath ?movement
        WHERE{{
            ?p rdf:type :person ;
            rdfs:label ?label;
            rdfs:label "{0}";
            :description ?description;
            :image ?image;
            :abstract ?abstract;
            :wikipediaLink ?wikilink;
            :gender ?gender;
            :date_of_birth ?dob;
            :date_of_death ?dod;
            :place_of_birth ?pob;
            :place_of_death ?pod;
            :movement ?mov;
        }}

    """ .format(label)
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    print(result)
    search_words = search_result(result)
    return {
        "result": result,
        "searchWords": search_words
    }


def get_location(data):
    _, label = extract_query_params(data)
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT  ?label ?description ?abstract ?wikipediaLink ?image ?country ?website ?lat ?lon
        WHERE {{ ?a rdf:type :location ;
                rdfs:label ?label ;
                rdfs:label "{0}" ;
                :description ?description;
                :abstract ?abstract;
                :wikipediaLink ?wikipediaLink;
                :image ?image;
                :country ?country;
                :website ?website;
                :lat ?lat;
                :lon ?lon.
        }}

    """ .format(label)
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    print(result)
    search_words = search_result(result)
    return {
        "result": result,
        "searchWords": search_words
    }


def get_standard_entity_data(data):
    obj_class, label = extract_query_params(data)
    sparql = SPARQLWrapper("http://neuds.de:3030/artontology/sparql")
    query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX : <http://h-da.de/fbi/artontology/>

        SELECT  ?label ?description ?abstract ?wikipediaLink ?image
        WHERE {{ ?a rdf:type :{1} ;
                rdfs:label ?label ;
                rdfs:label "{0}" ;
                :description ?description;
                :abstract ?abstract;
                :wikipediaLink ?wikipediaLink;
                :image ?image;
        }}

    """ .format(label, obj_class)
    sparql.setQuery(query_string)
    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    print(result)
    search_words = search_result(result)
    return {
        "result": result,
        "searchWords": search_words
    }


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


def search_result(result):
    if len(result.get('results').get('bindings')) > 0:
        search_words = get_search_words(result.get('results').get('bindings')[
                                        0].get('abstract').get('value'))
    else:
        search_words = []
    return search_words


def extract_query_params(data):
    obj_class = data.get('objClass')
    if not obj_class:
        obj_class = "artwork"
    label = data.get('label')
    return obj_class, label


def get_search_words(text):
    # Load model to return language object
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    # Entity White - listing
    whitelist = ["ORG", "PERSON", "GPE", "EVENT",
                 "FAC", "WORK_OF_ART", "PRODUCT", "LOC"]

    text = []
    label = []

    for entity in doc.ents:
        if (entity.label_ in whitelist) and not (entity.text in text):
            text.append(entity.text)
            label.append(entity.label_)

    return text
