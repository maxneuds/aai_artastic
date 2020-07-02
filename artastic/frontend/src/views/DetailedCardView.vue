<template>
  <div class="home">
    <v-container class="my-5">
      <v-layout row wrap justify-center>
        <v-flex>
          <h1 class="grey--text">{{$route.params.label}}</h1>
        </v-flex>
      </v-layout>
      <ChipsList/>
      <v-layout row wrap class="my-5">
        <v-flex>
          <v-row align="center" justify="center" class="mb-6">
            <v-col>
              <v-img
                v-if="card.Image"
                :src="card.Image"
                lazy-src="https://picsum.photos/id/11/100/60"
                aspect-ratio="1"
                contain
                class="white"
                max-height="500"
              >
                <template v-slot:placeholder>
                  <v-row class="fill-height ma-0" align="center" justify="center">
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-row>
                </template>
              </v-img>
            </v-col>
            <v-col>
              <div v-for="(value, key) in card" :key="key">
                <TextComponent :keyValue="key" :value="value" :searchWords="searchWordLabels" @generateChip="prepareAndAddChip" />
              </div>
              <SoundButton :text="card.Abstract" />
            </v-col>
          </v-row>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
import TextComponent from "../components/TextComponent";
import SoundButton from "../components/SoundButton";
import ChipsList from "../components/ChipsList";
export default {
  components: {
    ChipsList,
    TextComponent,
    SoundButton
  },
  methods: {
    prepareAndAddChip: function(text) {
      this.addChip(text);
    },
    ...mapMutations({ addChip: "addChip"})
  },
  computed: {
    ...mapGetters({ card: "getCard", searchWordLabels: "getSearchWordLabels" })
  }
};
</script>

<style>
</style>