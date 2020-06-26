let es = require('elasticsearch');

let client = new es.Client({
  host: 'neuds.de:15660/objects'
});

function search(searchText) {
  return client.search({
    "body": {
      "query": {
        "query_string": {
          "query": "*" + searchText + "*",
          "fields": ["label.value"]
        }
      }
    }
  }).then(function (resp) {
    return resp.hits.hits;
  }, function (err) {
    console.trace(err.message);
  })
}

export { search }