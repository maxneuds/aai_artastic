<template>
  <v-container fluid>
    <v-row dense>
      <v-col v-for="artwork in cards" :key="artwork.title" cols="4">
        <ArtworkCard v-if="objClass === 'motif'" :artwork="artwork" />
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
  props: ["cards", "objClass"]
};
</script>

<style>
</style>