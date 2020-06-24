<template>
  <div>
    <div v-if="keyValue !='Image' && keyValue != 'Abstract'">
      <strong>{{keyValue}}:</strong>
      {{value}}
    </div>
    <div v-if="keyValue === 'Abstract'">
      <strong>{{keyValue}}:</strong>
      <text-highlight
        v-if="shortAbstract"
        :queries="searchWordLabels"
        :highlightComponent="ClickableHighlightComponent"
        @generateChip="generateChip"
      >{{shortedAbstract}}</text-highlight>
      <text-highlight
        v-if="!shortAbstract"
        :queries="searchWordLabels"
        :highlightComponent="ClickableHighlightComponent"
        @generateChip="generateChip"
      >{{value}}</text-highlight>
    </div>
  </div>
</template>

<script>
import TextHighlight from "vue-text-highlight";
import ClickableHighlightComponent from "./ClickableHighlightComponent";
import { extractLabelsFromSearchWords } from "./js/parse";
export default {
  components: { TextHighlight },
  props: {
    keyValue: String,
    value: String,
    searchWords: Array,
    shortAbstract: {
      type: Boolean,
      default: false
    }
  },
  data: () => ({
    ClickableHighlightComponent
  }),
  methods: {
    generateChip: async function (text) {
      let index = this.searchWordLabels.indexOf(text);
      let label = text + " (" + this.searchWords[index][1] + ")";
      this.$emit("generateChip", label);
    }
  },
  computed: {
    searchWordLabels() {
      return extractLabelsFromSearchWords(this.searchWords);
    },
    shortedAbstract() {
      return this.value.slice(0, 350) + "...";
    }
  }
};
</script>

<style>
</style>