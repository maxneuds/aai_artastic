<template>
  <v-container fluid>
    <v-row dense>
      <v-col v-for="card in computedCards" :key="computedCards.indexOf(card)" cols="4">
        <v-card class="mx-auto" max-width="400">
          <v-img
            v-if="card.Image"
            class="white--text align-end"
            height="200px"
            :src="card.Image"
            lazy-src="https://picsum.photos/id/11/100/60"
          >
            <v-card-title v-if="card.Label">{{ card.Label }}</v-card-title>
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
              </v-row>
            </template>
          </v-img>

          <v-card-subtitle class="pb-0">{{ objClass }}</v-card-subtitle>

          <v-card-text class="text--primary">
            <div v-for="(value, key) in card" v-bind:key="value.Material">
              <TextComponent
                :keyValue="key"
                :value="value"
                :searchWords="searchWords"
                :shortAbstract="true"
                @generateChip="generateChip"
              />
            </div>
          </v-card-text>
          <v-card-actions>
            <router-link :to="{path: `/card/${card.Label}`}">
              <v-btn
                text
                color="deep-purple accent-4"
                v-on:click="addCardAndSearchWords(card, searchWords)"
              >Read more</v-btn>
            </router-link>
            <v-spacer></v-spacer>
            <SoundButton :text="card.Abstract" />
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import TextComponent from "./TextComponent";
import ClickableHighlightComponent from "./ClickableHighlightComponent";
import SoundButton from "../components/SoundButton";
import { extractLabelsFromSearchWords } from "./js/parse";
import { mapMutations } from "vuex";
export default {
  components: { SoundButton, TextComponent },
  data: () => ({
    ClickableHighlightComponent,
    shortAbstract: ""
  }),
  props: ["cards", "objClass", "searchWords"],
  methods: {
    addCardAndSearchWords(card, searchWordLabels) {
      this.addCard(card);
      this.addSearchWordLabels(searchWordLabels);
      console.log(searchWordLabels);
    },
    ...mapMutations({
      addCard: "addCard",
      addSearchWordLabels: "addSearchWordLabels"
    }),
    generateChip: async function(text) {
      this.$emit("generateChip", text);
    },
    computedOutput(data) {
      let obj = JSON.stringify(data);
      let obj2 = JSON.parse(obj);
      let finalObject = [];

      for (let card in obj2) {
        let testArray = {};
        for (let element in obj2[card]) {
          let cap_string = element.charAt(0).toUpperCase() + element.slice(1);
          if (cap_string === "Abstract") {
            let fullText = obj2[card][element].value;
            let shortText = fullText.slice(0, 350) + "...";
            this.shortAbstract = shortText;
            testArray[cap_string] = shortText;
          }
          testArray[cap_string] = obj2[card][element].value;
        }
        finalObject.push(testArray);
      }
      console.log(finalObject);
      return finalObject;
    }
  },
  computed: {
    searchWordLabels() {
      console.log(this.searchWords);
      let test = extractLabelsFromSearchWords(this.searchWords);
      return test;
    },
    computedCards() {
      return this.computedOutput(this.cards);
    }
  }
};
</script>

<style></style>
