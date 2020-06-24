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
          <SearchField @postQuery="postQuery" :chipSearch="chipSearch"/>
        </v-flex>
      </v-layout>
      <ChipsList :chipLabel="chipLabel" @pasteToSearch="pasteToSearch"/>
      <v-layout row wrap class="my-5">
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
import CardList from "../components/CardList";
import axios from "axios";
import { parseObjClass } from "../components/js/parse";
import { search as searchElastic } from "../components/js/elasticsearch";
import ChipsList from "../components/ChipsList";
export default {
  props: ["chipLabel", "chipSearch"],
  components: {
    ChipsList,
    SearchField,
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
    generateChip: function(text) {
      this.chipLabel = text;
    },
    pasteToSearch(item){
      console.log(item);
      console.log("Test1");
      this.chipSearch = item;
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
        this.searchWords = await this.filterSearchWords(
          response.data.searchWords
        );
      });
    },
    filterSearchWords: async function(searchWords) {
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
        if (objClass) {
          ret.push([searchWords[i], objClass]);
        }
      }
      return ret;
    }
  }
};
</script>

<style>
#mainSearch {
  position: relative;
}
</style>
