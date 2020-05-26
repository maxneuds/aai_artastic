<template>
  <section id="home">
    <TheNavbar />
    <v-sheet id="scrolling-techniques-5" class="overflow-y-auto" max-height="800">
      <v-container fluid style="height: 1500px;">
        <v-row>
          <v-col cols="12">
            <v-row class="grey lighten-5 justify-center align-center pa-9" style="height: 800px;">
              <SearchField />
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
  </section>
</template>

<script>
import TheNavbar from "../components/TheNavbar.vue";
import SearchField from "../components/SearchField";
export default {
  components: {
    TheNavbar,
    SearchField
  }
};
</script>

<style>
#mainSearch {
  position: relative;
}
</style>