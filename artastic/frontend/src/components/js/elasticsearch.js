let es = require('elasticsearch');

function search(searchText) {
  let client = new es.Client({
    host: 'neuds.de:15660/objects'
  });
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

function searchSimilarObjects(entity) {
  let client = new es.Client({
    host: 'neuds.de:15660/artsim'
  });
  return client.search({
    "body": {
      "sort": [
        { "score": "desc" },
        "_score"
      ],
      "query": {
        "multi_match": {
          "query": entity,
          "fields": ["id1", "id2"]
        }
      },
      "_source": ["id1", "id2", "score"]
    }
  }).then(function (resp) {
    return resp.hits.hits;
  }, function (err) {
    console.trace(err.message);
  })
}

export { search, searchSimilarObjects }