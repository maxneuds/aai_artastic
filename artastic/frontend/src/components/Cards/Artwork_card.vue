<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    >
      <v-card-title>Artworktitle</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Artwork</v-card-subtitle>

    <v-card-text class="text--primary" v-if="artwork">
      <div>Title: </div>

      <div>Artist: </div>
      
      <div>Movement: </div>

      <div>Material: </div>

      <div>Location: </div>

      <div>Description: </div>

      <div>Abstract: {{artwork.results}}</div>

    </v-card-text>
    
  </v-card>
</template>

<script>
export default {
  props: ["artwork"]
};
</script>