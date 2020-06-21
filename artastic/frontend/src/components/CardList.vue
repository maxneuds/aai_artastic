<template>
  <v-container fluid>
    <v-row dense>
      <v-col v-for="card in computedOutput(cards)" :key="card" cols="4">
        <v-card class="mx-auto" max-width="400">
          <v-img v-if="card.Image" class="white--text align-end" height="200px" :src="card.Image">
            <v-card-title v-if="card.Label">{{card.Label}}</v-card-title>
          </v-img>

          <v-card-subtitle class="pb-0">{{objClass}}</v-card-subtitle>

          <v-card-text class="text--primary">
            <div v-for="(value, key) in card" v-bind:key="value.Material">
              <div v-if="key !='Image' && key != 'Abstract'">
                <strong>{{key}}:</strong>
                {{value}}
              </div>
              <div v-if="key === 'Abstract'">
                <strong>{{key}}:</strong>
                <text-highlight
                  :queries="searchWordLabels"
                  :highlightComponent="ClickableHighlightComponent"
                  @generateChip="generateChip"
                >{{value}}</text-highlight>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import TextHighlight from "vue-text-highlight";
import ClickableHighlightComponent from "./ClickableHighlightComponent";
import { extractLabelsFromSearchWords } from "./js/parse";
export default {
  components: { TextHighlight },
  data: () => ({
    ClickableHighlightComponent,
    abstract: null
  }),
  props: ["cards", "objClass", "searchWords"],
  methods: {
    generateChip: async function(text) {
      let index = this.searchWordLabels.indexOf(text);
      let label = text + " (" + this.searchWords[index][1] + ")";
      this.$emit("generateChip", label);
    },
    computedOutput(data) {
      var obj = JSON.stringify(data);
      var obj2 = JSON.parse(obj);
      var finalObject = [];

      for (let card in obj2) {
        let testArray = {};
        for (let element in obj2[card]) {
          var cap_string = element.charAt(0).toUpperCase() + element.slice(1);
          testArray[cap_string] = obj2[card][element].value;
        }
        finalObject.push(testArray);
      }
      console.log(typeof finalObject[0]);
      return finalObject;
    }
  },
  computed: {
    searchWordLabels() {
      let test = extractLabelsFromSearchWords(this.searchWords);
      console.log(test);
      return test;
    }
  }
};
</script>

<style>
</style>