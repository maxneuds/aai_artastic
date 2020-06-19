<template>
  <v-card class="mx-auto" max-width="400">
    <v-img class="white--text align-end" height="200px" :src="person.image.value">
      <v-card-title>{{person.label.value}}</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Artist</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Gender: {{person.gender.value}}</div>
      <div>Birthdate: {{person.dob.value}}</div>
      <div>Place of Birth: {{person.pob.value}}</div>
      <div>Date of Death: {{person.dod.value}}</div>
      <div>Place of Death: {{person.pod.value}}</div>
      <div>
        <text-highlight
          :queries="searchWordLabels"
          :highlightComponent="ClickableHighlightComponent"
          @generateChip="generateChip"
        >Abstract: {{person.abstract.value}}</text-highlight>
      </div>
      <div>Wiki Link: {{person.wikilink.value}}</div>
    </v-card-text>
  </v-card>
</template>

<script>
import TextHighlight from "vue-text-highlight";
import ClickableHighlightComponent from "../ClickableHighlightComponent";
import {extractLabelsFromSearchWords} from "../js/parse";
export default {
  components: { TextHighlight },
  data: () => ({
    ClickableHighlightComponent
  }),
  methods: {
    generateChip: async function(text) {
      let index = this.searchWordLabels.indexOf(text);
      let label = text + ' (' + this.searchWords[index][1] + ')';
      this.$emit("generateChip", label);
    }
  },
  computed: {
    searchWordLabels(){
      return extractLabelsFromSearchWords(this.searchWords);
    }
  },
  props: ["person", "search-words"]
};
</script>