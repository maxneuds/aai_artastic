<template>
  <div class="my-2">
    <v-btn color="blue-grey" fab small dark v-on:click="sayHi(text)">
      <v-icon>mdi-voice</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  props: ["text"],
  methods: {
    sayHi(text) {
      console.log("Hi " + text + "!");
    }
  }
};
</script>

<style>
</style>