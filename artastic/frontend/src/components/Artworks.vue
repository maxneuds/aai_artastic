<template>
  <div class="pt-5">
    <div v-if="artworks && artworks.length">
      <div class="card mb-3" v-for="artwork of artworks" v-bind:key="artwork.id">
        <div class="row no-gutters">
          <div class="col-md-4">
            <svg
              class="bd-placeholder-img"
              width="200"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
              focusable="false"
              role="img"
              aria-label="Placeholder: Thumbnail"
            >
              <title>{{ artwork.name }}</title>
              <rect width="100%" height="100%" fill="#55595c" />
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ artwork.name.charAt(0) }}</text>
            </svg>
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{ artwork.name }}</h5>
              <p class="card-text">{{ artwork.artist }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p v-if="artworks.length == 0">No artworks</p>
  </div>
</template>

<script>
export default {
  props: ["artworks"]
};
</script>

<style scoped>
</style>