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
          <SearchField />
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import SearchField from "../components/SearchField";
export default {
  components: {
    SearchField
  }
};
</script>

<style>
#mainSearch {
  position: relative;
}
</style>