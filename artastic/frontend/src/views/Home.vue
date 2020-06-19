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
          <v-btn v-if="chips.length > 0" color="blue-grey" fab small dark v-on:click="clearChips">
            <v-icon>mdi-close-circle-outline</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>
      <v-layout row wrap class="my-5">
        <SoundButton :text="'Max'" />
        <v-flex>
          <CardList
            v-if="data && searchWords"
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
import {parseObjClass} from "../components/js/parse";
import {search as searchElastic} from "../components/js/elasticsearch";
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
      let url = this.objClass + "/";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios({
        method: "post",
        url: "http://localhost:8000/api/" + url,
        data: {
          label: data.label,
          objClass: data.objClass
        }
      }).then(async response => {
        this.data = response.data.result.results.bindings;
        this.searchWords = await this.filterSearchWords(response.data.searchWords);
      });
    },
    filterSearchWords: async function(searchWords){
      let ret = [];
      for (let i = 0; i < searchWords.length; i++) {
        let objClass;
        await searchElastic(searchWords[i])
              .then(res => {
                let foundObjClass = parseObjClass(res);
                if (foundObjClass) {
                  objClass = foundObjClass;
                }
              })
              .catch(err => console.log(err));
        if(objClass){
          ret.push([searchWords[i], objClass]);
        }
      }
      return ret;
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