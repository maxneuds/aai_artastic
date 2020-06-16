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
          <ArtworkCard :artwork="artwork"/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import SearchField from "../components/SearchField";
import ArtworkCard from "../components/Cards/Artwork_card"
import axios from "axios";
export default {
  components: {
    SearchField,
    ArtworkCard
  },
  data: function() {
    return {
      artwork: []
    };
  },
  methods: {
    postQuery: function(data) {
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios({
        method: "post",
        url: "http://localhost:8000/api/artworks/",
        data: {
          data: data
        }
      }).then(response => {
        this.artwork = response.data;
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