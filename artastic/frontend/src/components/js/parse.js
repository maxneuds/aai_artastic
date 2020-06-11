function parseAutocomplete(hits){
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

export {parseAutocomplete}