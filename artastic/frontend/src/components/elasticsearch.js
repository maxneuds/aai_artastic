let es = require('elasticsearch');

let client = new es.Client({
  host: 'neuds.de:9200/objects/_search',
  log: 'trace'
});

function search (searchText){
  return client.search({
    "query": {
      "query_string": {
        "query": searchText
      }
    },
    "size": 5
  }).then(function (resp) {
      return resp.hits.hits;
  }, function (err) {
    console.trace(err.message);
})}

export { search }