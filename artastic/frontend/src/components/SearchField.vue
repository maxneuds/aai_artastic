<template>
  <input type="text" placeholder="Search for artwork name" v-model="query" v-on:keyup="postQuery">
</template>
<script>
  export default {
    data() {
      return {
        query : ''
      }
    },
    methods: {
      postQuery: function (e) {
        if(e.keyCode === 13){
          this.$router.push({path : '/artworks', params: {q : this.query}})
        }
      }
    }
  }
</script>