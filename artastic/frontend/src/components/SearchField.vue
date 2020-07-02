<template>
  <v-card color="blue-grey lighten-5">
    <v-card-title class="headline blue-grey lighten-2 white--text">Search for Artworks</v-card-title>
    <v-spacer />
    <v-card-text>
      <v-autocomplete
        ref="searchInputField"
        v-model="model"
        :items="items"
        :loading="isLoading"
        :search-input.sync="search"
        v-on:keyup="submitQuery"
        filled
        clearable
        item-text="label"
        item-value="resultId"
        label="Search"
        placeholder="Start by typing..."
        prepend-icon="mdi-database-search"
        return-object
      >
        <template v-slot:item="{parent, item}">
          <v-list-item-content>
            <v-list-item-title v-html="parent.genFilteredText(item.label)"></v-list-item-title>
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
import {mapGetters} from "vuex";
export default {
  data: () => ({
    isLoading: false,
    model: null,
    search: null,
    labelLimit: 60,
    autocompleteResults: []
  }),
  computed: {
    items() {
      return this.autocompleteResults.map(entry => {
        const label =
          entry.label.length > this.labelLimit
            ? entry.label.slice(0, this.labelLimit) + "..."
            : entry.label;
        const resultId = entry.resultId;
        const objClass = entry.objClass;
        return Object.assign({}, { resultId }, { label }, { objClass });
      });
    },
    ...mapGetters({ getSearchParam: "getSearchParam" })
  },
  methods: {
    submitQuery(e) {
      if (e.keyCode === 13) {
        let queryParam = this.getCorrectQueryParam();
        this.$emit("postQuery", queryParam);
      }
    },
    getCorrectQueryParam() {
      if (this.model) {
        if (Object.prototype.hasOwnProperty.call(this.model, "label")) {
          if (this.model.label.includes(this.search)) {
            return this.model;
          } else {
            return this.items[0];
          }
        } else {
          if (this.model.contains(this.search)) {
            return this.model;
          } else {
            return this.items[0];
          }
        }
      } else {
        return this.items[0];
      }
    }
  },
  watch: {
    search(val) {
      if (!val || val.length < 2) {
        this.autocompleteResults = [];
      } else {
        // Items have already been requested
        if (this.isLoading) return;
        this.isLoading = true;

        searchElastic(val)
          .then(res => (this.autocompleteResults = parseAutocomplete(res)))
          .catch(err => console.log(err))
          .finally(() => (this.isLoading = false));
      }
    },
    getSearchParam(val){
      this.model = {
        label : val.label,
        objClass : val.objClass
      };
      this.search = val.label;
    }
  }
};
</script>