```json
GET artsim/_search?size=100
{
  "sort" : [
      { "score" : "desc" },
      "_score"
  ],
  "query": {
      "multi_match" : {
          "query" : "Q6519358",
          "fields" : ["id1", "id2"]
      }
  },
  "_source": ["id1", "id2", "score"]
}
```
