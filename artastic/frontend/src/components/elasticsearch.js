let es = require('elasticsearch');

let client = new es.Client({
  host: 'neuds.de:9200/objects/_search',
  log: 'trace'
});

function search (searchText){
  return client.search({
    "query": {
      "multi_match": {
        "query": searchText,
        "fields": ["Class", "abstract", "description", "instance", "label"]
      }
    },
    "sort": ["_score"]
  }).then(function (resp) {
      return resp.hits.hits;
  }, function (err) {
    console.trace(err.message);
})}

export { search }