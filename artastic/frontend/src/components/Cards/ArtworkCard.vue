<template v-if="artwork">
  <v-card class="mx-auto" max-width="400">
    <v-img class="white--text align-end" height="200px" :src="artwork.image.value">
      <v-card-title>{{artwork.label.value}}</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Artwork</v-card-subtitle>

    <v-card-text class="text--primary" v-if="artwork">
      <div>Artist: {{artwork.artist.value}}</div>

      <div>Movement: {{artwork.movement.value}}</div>

      <div>Material: {{artwork.material.value}}</div>

      <div>Description: {{artwork.description.value}}</div>

      <div>Abstract: {{artwork.abstract.value}}</div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: ["artwork"]
};
</script>