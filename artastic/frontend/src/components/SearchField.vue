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
        v-on:keyup="submitQuery"
        filled
        clearable
        item-text="description"
        item-value="description"
        label="Search"
        placeholder="Start by typing..."
        prepend-icon="mdi-database-search"
        return-object
      >
        <template v-slot:item="{item}">
          <v-list-item-content>
            <v-list-item-title v-text="item.description"></v-list-item-title>
            <v-list-item-subtitle v-text="item.objClass"></v-list-item-subtitle>
          </v-list-item-content>
        </template>
      </v-autocomplete>
    </v-card-text>
  </v-card>
</template>

<script>
import { search as searchElastic } from "./js/elasticsearch.js";
import { parseAutocomplete } from "./js/parse.js";
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
      let entries = this.autocompleteResults.filter(entry => entry);

      return entries.map(entry => {
        const description =
          entry[0].length > this.descriptionLimit
            ? entry[0].slice(0, this.descriptionLimit) + "..."
            : entry[0];
        const objClass = entry[1];
        return Object.assign({},{ description }, { objClass });
      });
    }
  },
  methods: {
    submitQuery(e) {
      if (e.keyCode === 13) {
        this.$emit("postQuery", this.model);
      }
    }
  },
  watch: {
    search(val) {
      if(!val){
        this.autocompleteResults = [];
      }
      // Items have already been requested
      if (this.isLoading) return;
      this.isLoading = true;

      searchElastic(val)
        .then(res => this.autocompleteResults = parseAutocomplete(res))
        .catch(err => console.log(err))
        .finally(() => (this.isLoading = false));
    }
  }
};
</script>