<template>
  <v-layout row wrap class="my-5">
      <v-flex>
        <v-chip
          v-for="chip in chips"
          :key="chip"
          close
          @click="setSelectedChip(chip)"
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
    import {mapMutations, mapGetters} from "vuex";
    import {extractObjClassFromChip} from "./js/parse";
    export default {
        name: "chipsList",
        methods: {
            remove(item) {
                const index = this.chips.indexOf(item);
                if (index >= 0) this.chips.splice(index, 1);
            },
            setSelectedChip(text){
              const regExp = /^.*?(?=\()/;
              const label = regExp.exec(text)[0];
              const objClass = extractObjClassFromChip(text);
              this.setSearchParam({
                  label: label,
                  objClass: objClass
              });
            },
            clearChips() {
                this.setChips([]);
            },
            ...mapMutations({ setSearchParam: "setSearchParam", setChips: "setChips", addChip: "addChip"})
        },
        computed: {
            ...mapGetters({chips: "getChips"})
        },
    }
</script>

<style scoped>

</style>