<template>
  <div class="home">
    <v-container class="my-5">
      <v-layout row wrap justify-center>
        <v-flex>
          <h1 class="grey--text">Home</h1>
        </v-flex>
      </v-layout>

      <v-layout row wrap class="my-5">
        <v-flex>
          <SearchField @postQuery="postQuery" />
        </v-flex>
      </v-layout>
      <v-layout row wrap class="my-5">
        <v-flex>
          <v-chip
            v-for="chip in chips"
            :key="chip"
            close
            @click:close="remove(chip)"
            class="ma-2"
            color="green"
            text-color="white"
          >{{chip}}</v-chip>
        </v-flex>
      </v-layout>
      <v-layout row wrap class="my-5">
        <v-flex>
          <SoundButton :text="'Max'" />
          <CardList
            v-if="artworks"
            :cards="artworks"
            :searchWords="searchWords"
            :objClass="objClass"
            @generateChip="generateChip"
          />
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import SearchField from "../components/SearchField";
import SoundButton from "../components/SoundButton";
import CardList from "../components/Cards/CardList";
import axios from "axios";
export default {
  components: {
    SearchField,
    SoundButton,
    CardList
  },
  data: function() {
    return {
      artworks: [],
      searchWords: [],
      chips: [],
      objClass: null
    };
  },
  methods: {
    remove(item) {
      const index = this.chips.indexOf(item);
      if (index >= 0) this.chips.splice(index, 1);
    },
    generateChip: function(text) {
      // only generate Chip if this chip is new
      if (!this.chips.includes(text)) {
        this.chips.push(text);
      }
    },
    postQuery: function(data) {
      this.objClass = data.objClass;
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios({
        method: "post",
        url: "http://localhost:8000/api/artworks/",
        data: {
          label: data.label,
          objClass: data.objClass
        }
      }).then(response => {
        this.artworks = response.data.result.results.bindings;
        console.log(this.artworks);
        this.searchWords = response.data.searchWords;
      });
    }
  }
};
</script>

<style>
#mainSearch {
  position: relative;
}
</style>