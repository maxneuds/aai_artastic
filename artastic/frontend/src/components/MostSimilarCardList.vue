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
            <div v-for="(value, key) in card" v-bind:key="value.label">
              <TextComponent :keyValue="key" :value="value" />
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import TextComponent from "./TextComponent";
export default {
  components: { TextComponent },
  props: ["cards", "objClass"],
  methods: {
    computedOutput(data) {
      let finalObject = [];
      let obj = JSON.stringify(data);
      let obj2 = JSON.parse(obj);
      obj2.map(entry => {
        let array = {};
        array["Label"] = entry[0].label.value;
        array["Image"] = entry[0].image.value;
        array["Score"] = entry[1].toString();
        finalObject.push(array);
      });

      finalObject.sort(function(a, b) {
        return parseFloat(b.Score) - parseFloat(a.Score);
      });
      return finalObject;
    }
  },
  computed: {
    computedCards() {
      return this.computedOutput(this.cards);
    }
  }
};
</script>

<style></style>
