<template>
  <v-card
    color="green lighten-2"
    dark
  >
    <v-card-title class="headline green lighten-3">
      Search for Artworks
    </v-card-title>
    <v-card-text>
      <v-autocomplete
        v-model="model"
        :items="items"
        :loading="isLoading"
        :search-input.sync="search"
        v-on:keyup="submitQuery"
        color="white"
        filled
        label="Artworks"
        placeholder="Search for an Artwork"
        prepend-icon="mdi-database-search"
        return-object
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>
              Search for an
              <strong>Artwork</strong>
            </v-list-item-title>
          </v-list-item>
        </template>
        <template v-slot:item="{item}">
          <v-list-item-content>
            <v-list-item-title v-text="item[0]"></v-list-item-title>
            <v-list-item-subtitle v-text="item[1]"></v-list-item-subtitle>
          </v-list-item-content>
        </template>
      </v-autocomplete>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="!model"
        color="grey darken-3"
        @click="model = null"
      >
        Clear
        <v-icon right>mdi-close-circle</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  import { search } from './elasticsearch.js';
  export default {
    data: () => ({
      isLoading: false,
      model: null,
      search: null,
      autocompleteResults: []
    }),
    computed: {
      items () {
        return this.autocompleteResults.filter(entry => entry)
      },
    },
    methods: {
      submitQuery(e){
        if(e.keyCode === 13) {
          this.$emit("postQuery", this.search);
        }
      }
    },
    watch: {
      search () {
        if (this.isLoading) return

        this.isLoading = true

        search(this.search)
          .then(res => this.autocompleteResults = res)
          .catch(err => console.log(err))
          .finally(() => this.isLoading=false)
      },
    }
}
</script>