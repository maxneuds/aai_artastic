let es = require('elasticsearch');

let client = new es.Client({
  host: 'neuds.de:9200/objects',
  log: 'trace'
});

function search (searchText) {
  return client.search({
    "body":{
      "query": {
        "query_string": {
          "query": searchText
        }
      },
      "size": 5
    }
  }).then(function (resp) {
      return parseResultsForAutocomplete(resp.hits.hits);
  }, function (err) {
    console.trace(err.message);
})}

function parseResultsForAutocomplete(hits){
  return hits.map(function(entry){
    let objClass = extractObjClass(entry['_source']['Class']['value']);
    if(objClass !=  null){
      return [entry['_source']['label']['value'], objClass];
    }
    return null;
  })
}

function extractObjClass(uri){
  let regExp = /([^/]+$)/;
  let ret = regExp.exec(uri)[1];
  if(!ret.startsWith("Q")) {
    return ret;
  }
  return null;
}

export { search }