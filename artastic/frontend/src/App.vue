<template>
  <v-app>
    <AppBar />
    <v-content class="mx-4 mb-4">
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
// import Home from "./pages/Home.vue";
import AppBar from "@/components/AppBar";
export default {
  name: "App",

  components: { AppBar },

  data: () => ({
    drawer: false
  })
};
</script>

<style scoped>
#title {
  font-family: unquote("Roboto");
}
</style>

