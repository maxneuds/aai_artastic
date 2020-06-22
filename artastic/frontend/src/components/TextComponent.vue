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
      >{{shortedAbstract}}</text-highlight>
      <text-highlight
        v-if="!shortAbstract"
        :queries="searchWordLabels"
        :highlightComponent="ClickableHighlightComponent"
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