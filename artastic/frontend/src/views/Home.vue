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
          <CardList v-if="artworks" :cards="artworks" />
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import SearchField from "../components/SearchField";
import CardList from "../components/Cards/CardList";
import axios from "axios";
export default {
  components: {
    SearchField,
    CardList
  },
  data: function() {
    return {
      artworks: [],
      objClass: null
    };
  },
  methods: {
    postQuery: function(data, objClass) {
      this.objClass = objClass;
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios({
        method: "post",
        url: "http://localhost:8000/api/artworks/",
        data: {
          data: data
        }
      }).then(response => {
        this.artworks = response.data.results.bindings;
        console.log(response.data);
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