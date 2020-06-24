<template>
  <v-layout row wrap class="my-5">
      <v-flex>
        <v-chip
          v-for="chip in chips"
          :key="chip"
          close
          @click="$emit('pasteToSearch', chip)"
          @click:close="remove(chip)"
          class="ma-2"
          color="green"
          text-color="white"
      >{{ chip }}</v-chip>
      <v-btn v-if="chips.length > 0" color="blue-grey" fab small dark v-on:click="clearChips">
        <v-icon>mdi-close-circle-outline</v-icon>
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
    export default {
        props: ["chipLabel"],
        name: "chipsList",
        data(){
            return {
                chips: []
            }
        },
        methods: {
            remove(item) {
                const index = this.chips.indexOf(item);
                if (index >= 0) this.chips.splice(index, 1);
            },
            generateChip: function (text) {
                // only generate Chip if this chip is new
                if (!this.chips.includes(text)) {
                    this.chips.push(text);
                }
            },
            clearChips() {
                this.chips = [];
            }
        },
        watch:{
            chipLabel(){
                this.generateChip(this.chipLabel);
            }
        }
    }
</script>

<style scoped>

</style>