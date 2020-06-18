<template>
  <v-container fluid>
    <v-row dense>
      <v-col v-for="card in cards" :key="card.title" cols="4">
        <ArtworkCard
          v-if="objClass === 'artwork'"
          :artwork="card"
          :searchWords="searchWords"
          @generateChip="generateChip"
        />
        <ArtistCard
          v-if="objClass === 'person'"
          :person="card"
          :searchWords="searchWords"
          @generateChip="generateChip"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ArtworkCard from "./ArtworkCard";
import ArtistCard from "./ArtistCard";
export default {
  components: {
    ArtworkCard,
    ArtistCard
  },
  props: ["cards", "objClass", "searchWords"],
  methods: {
    generateChip: function(text) {
      this.$emit("generateChip", text);
    }
  }
};
</script>

<style>
</style>