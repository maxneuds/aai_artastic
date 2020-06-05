<template>
  <v-text-field
    type="text"
    placeholder="Search for painters name"
    outlined
    v-model="query"
    v-on:change="postQuery"
  />
</template>

<script>
export default {
  data() {
    return {
      query: ""
    };
  },
  methods: {
    postQuery: function() {
      this.$emit("postQuery", this.query);
    }
  }
};
</script>