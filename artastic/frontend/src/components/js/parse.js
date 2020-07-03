function parseAutocomplete(hits) {
  let autocompleteResults = hits.map(function (entry) {
    let objClass = extractObjClass(entry['_source']['Class']['value']);
    if (objClass != null) {
      let resultId = hits.indexOf(entry);
      let label = entry['_source']['label']['value'];
      return {
        resultId: resultId,
        objClass: objClass,
        label: label
      };
    }
  }).filter(entry => entry != null);

  let ret = [];
  for (let index = 0; index < autocompleteResults.length; ++index) {
    if (!containsAutocompleteResult(ret, autocompleteResults[index])) {
      ret.push(autocompleteResults[index]);
    }
  }
  return ret;
}

function containsAutocompleteResult(output, entry) {
  for (let index = 0; index < output.length; ++index) {
    let currentEntry = output[index];
    if (currentEntry.objClass === entry.objClass && currentEntry.label === entry.label) {
      return true;
    }
  }
  return false;
}

function extractObjClass(uri) {
  let regExp = /([^/]+$)/;
  let ret = regExp.exec(uri)[1];
  if (!ret.startsWith("Q")) {
    return ret;
  }
  return null;
}

function parseObjClass(hits) {
  return extractObjClass(hits[0]._source.Class.value);
}

function extractLabelsFromSearchWords(searchWords) {
  let column = [];
  for (let i = 0; i < searchWords.length; i++) {
    column.push(searchWords[i][0]);
  }
  return column;
}

function extractObjClassFromChip(chipLabel) {
  let regExr = /\(([^]+)\)/;
  let ret = regExr.exec(chipLabel)[0];
  return ret.substring(1, ret.length - 1)
}

function parseSources(similarityobjects) {
  let values = similarityobjects.map(entry => {
    return entry._source
  })
  return values
}

function parseURL(url) {
  var parser = document.createElement('a'),
    searchObject = {},
    queries, split, i;
  // Let the browser do the work
  parser.href = url;
  // Convert query string to object
  queries = parser.search.replace(/^\?/, '').split('&');
  for (i = 0; i < queries.length; i++) {
    split = queries[i].split('=');
    searchObject[split[0]] = split[1];
  }
  return {
    protocol: parser.protocol,
    host: parser.host,
    hostname: parser.hostname,
    port: parser.port,
    pathname: parser.pathname,
    search: parser.search,
    searchObject: searchObject,
    hash: parser.hash
  };
}

export { parseAutocomplete, parseObjClass, extractLabelsFromSearchWords, extractObjClassFromChip, parseURL, parseSources }