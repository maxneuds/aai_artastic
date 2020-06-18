<template>
  <v-container fluid>
    <v-row dense>
      <v-col v-for="artwork in cards" :key="artwork.title" cols="4">
        <ArtworkCard
          v-if="objClass === 'artwork'"
          :artwork="artwork"
          :searchWords="searchWords"
          @generateChip="generateChip"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ArtworkCard from "./ArtworkCard";
export default {
  components: {
    ArtworkCard
  },
  props: ["cards", "objClass", "searchWords"],
  methods: {
    generateChip: function(text) {
      console.log("Cardlist");
      this.$emit("generateChip", text);
    }
  }
};
</script>

<style>
</style>