<template>
  <div class="my-2">
    <v-btn color="blue-grey" fab dark v-on:click="sayHi">
      <v-icon>mdi-play-circle-outline</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  methods: {
    sayHi() {
      console.log("Hi!");
    }
  }
};
</script>

<style>
</style>