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
    let x =  [entry['_source']['label']['value'], extractObjClass(entry['_source']['Class']['value'])];
    console.log(x)
    return x;
  })
}

function extractObjClass(uri){
  let regExp = /([^/]+$)/;
  return regExp.exec(uri)[1];
}

export { search }