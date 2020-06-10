<template>
  <v-card color="blue-grey lighten-5">
    <v-card-title class="headline blue-grey lighten-2 white--text">Search for Artworks</v-card-title>
    <v-spacer />
    <v-card-text>
      <v-autocomplete
        v-model="model"
        :items="items"
        :loading="isLoading"
        :search-input.sync="search"
        item-text="Description"
        filled
        label="Search"
        placeholder="Start by typing..."
        prepend-icon="mdi-database-search"
        return-object
      ></v-autocomplete>
    </v-card-text>
  </v-card>
</template>

<script>
import { search as searchElastic } from "./elasticsearch.js";
export default {
  data: () => ({
    isLoading: false,
    model: null,
    search: null,
    descriptionLimit: 60,
    autocompleteResults: []
  }),
  computed: {
    items() {
      var entries = this.autocompleteResults.filter(entry => entry);

      return entries.map(entry => {
        const Description =
          entry[0].length > this.descriptionLimit
            ? entry[0].slice(0, this.descriptionLimit) + "..."
            : entry[0];
        return Object.assign({}, entry, { Description });
      });
    }
  },
  methods: {
    submitQuery(e) {
      if (e.keyCode === 13) {
        this.$emit("postQuery", this.search);
      }
    }
  },
  watch: {
    search(val) {
      // Items have already been requested
      if (this.isLoading) return;
      this.isLoading = true;

      searchElastic(val)
        .then(res => (this.autocompleteResults = res))
        .catch(err => console.log(err))
        .finally(() => (this.isLoading = false));
    }
  }
};
</script>