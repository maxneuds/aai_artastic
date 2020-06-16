<template v-if="artwork">
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="white--text align-end"
      :src="artwork.results.bindings[0].image.value"
    >
      <v-card-title>{{artwork.results.bindings[0].label.value}}</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Artwork</v-card-subtitle>

    <v-card-text class="text--primary" v-if="artwork">

      <div>Artist: {{artwork.results.bindings[0].artist.value}}</div>
      
      <div>Movement: {{artwork.results.bindings[0].movement.value}}</div>

      <div>Material: {{artwork.results.bindings[0].material.value}}</div>

      <div>Description: {{artwork.results.bindings[0].description.value}}</div>

      <div>Abstract: {{artwork.results.bindings[0].abstract.value}}</div>

    </v-card-text>
    
  </v-card>
</template>

<script>
export default {
  props: ["artwork"]
};
</script>