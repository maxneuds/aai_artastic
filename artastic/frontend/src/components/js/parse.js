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

function parseArtwork(jsonstr){
  let res = ["title", "artist", "movement", "material", "country", "description", "image", "abstract"];
  let resbool = [false, false, false, false, false, false, false, false];

  jsonstr.array.forEach(element => {
    if(element.property.value.localCompare("http://www.w3.org/2000/01/rdf-schema#label") && !resbool[0])
    {
      res[0] = element.value.value;
	  resbool[0] = true;
    }
    if(element.property.value.localCompare("http://h-da.de/fbi/artontology/artist") && !resbool[1])
    {
      res[1] = element.value.value;
	  resbool[1] = true;
    }
    if(element.property.value.localCompare("http://h-da.de/fbi/artontology/movement") && !resbool[2])
    {
      res[2] = element.value.value;
	  resbool[2] = true;
    }
    if(element.property.value.localCompare("http://h-da.de/fbi/artontology/material") && !resbool[3])
    {
      res[3] = element.value.value;
	  resbool[3] = true;
    }
    if(element.property.value.localCompare("http://h-da.de/fbi/artontology/country") && !resbool[4])
    {
      res[4] = element.value.value;
	  resbool[4] = true;
    }
    if(element.property.value.localCompare("http://h-da.de/fbi/artontology/description") && !resbool[5])
    {
      res[5] = element.value.value;
	  resbool[5] = true;
    }
    if(element.property.value.localCompare("http://h-da.de/fbi/artontology/image") && !resbool[6])
    {
      res[6] = element.value.value;
	  resbool[6] = true;
    }
    if(element.property.value.localCompare("http://h-da.de/fbi/artontology/abstract") && !resbool[7])
    {
      res[7] = element.value.value;
	  resbool[7] = true;
    }
  });

  return res

}

export {parseAutocomplete}
export {parseArtwork}