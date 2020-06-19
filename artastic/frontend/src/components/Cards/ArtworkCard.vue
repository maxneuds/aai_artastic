<template v-if="artwork">
  <v-card class="mx-auto" max-width="400">
    <v-img class="white--text align-end" height="200px" :src="artwork.image.value">
      <v-card-title>{{artwork.label.value}}</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Artwork</v-card-subtitle>

    <v-card-text class="text--primary" v-if="artwork">
      <div>Artist: {{artwork.artist.value}}</div>

      <div>Movement: {{artwork.movement.value}}</div>

      <div>Material: {{artwork.material.value}}</div>

      <div>Description: {{artwork.description.value}}</div>

      <div>
        <text-highlight
          :queries="searchWordLabels"
          :highlightComponent="ClickableHighlightComponent"
          @generateChip="generateChip"
        >Abstract: {{artwork.abstract.value}}</text-highlight>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import TextHighlight from "vue-text-highlight";
import ClickableHighlightComponent from "../ClickableHighlightComponent";
import {extractLabelsFromSearchWords} from "../js/parse"
export default {
  components: { TextHighlight },
  data: () => ({
    ClickableHighlightComponent
  }),
  methods: {
    generateChip:async function(text) {
      let index = this.searchWordLabels.indexOf(text);
      console.log(index);
      let label = text + ' (' + this.searchWords[index][1] + ')';
      console.log(label);
      this.$emit("generateChip", label);
    }
  },
  computed: {
    searchWordLabels(){
      let test = extractLabelsFromSearchWords(this.searchWords);
      console.log("test");
      console.log(test);
      return test;
    }
  },
  props: ["artwork", "searchWords"]
};
</script>