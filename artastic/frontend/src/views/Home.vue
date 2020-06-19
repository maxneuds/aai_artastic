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
        <v-btn color="blue-grey" fab small dark v-on:click="clearChips">
          <v-icon>mdi-clear</v-icon>
        </v-btn>
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
        <SoundButton :text="'This is a test of the text engine. Yo.'" />
        <v-flex>
          <CardList
            v-if="data"
            :cards="data"
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
      data: [],
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
      var url = this.objClass + "/";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios({
        method: "post",
        url: "http://localhost:8000/api/" + url,
        data: {
          label: data.label,
          objClass: data.objClass
        }
      }).then(response => {
        this.data = response.data.result.results.bindings;
        this.searchWords = response.data.searchWords;
      });
    },
    clearChips() {
      this.chips = [];
    }
  }
};
</script>

<style>
#mainSearch {
  position: relative;
}
</style>