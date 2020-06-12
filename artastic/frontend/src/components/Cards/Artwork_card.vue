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
      <div>Title: {{artwork[0]}}</div>

      <div>Artist: {{artwork[1]}}</div>
      
      <div>Movement: {{artwork[2]}}</div>

      <div>Material: {{artwork[3]}}</div>

      <div>Location: {{artwork[4]}}</div>

      <div>Description: {{artwork[5]}}</div>

      <div>Abstract: {{artwork[6]}}</div>

    </v-card-text>
    
  </v-card>
</template>

<script>
export default {
  props: ["artwork"]
};
</script>