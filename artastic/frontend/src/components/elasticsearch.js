let es = require('elasticsearch');

let client = new es.Client({
  host: 'neuds.de:9200',
  log: 'trace'
});

function search (searchText){
  return client.search({
    type: 'completion',
    body: {
      fields: {},
      query: {
        multi_match: {
          query: searchText,
          fields: ["rdfs:label", "rdfs:type"]
        }
      },
      sort: ["_score", {"createdDate": "desc"}]
    }
  }).then(function (resp) {
      return resp.hits.hits;
  }, function (err) {
    console.trace(err.message);
})}

export { search }