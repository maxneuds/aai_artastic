<template>
  <nav>
    <v-app-bar color="#43a047" dark prominent src="https://picsum.photos/1920/1080?random">
      <v-app-bar-nav-icon @click="drawer=true"></v-app-bar-nav-icon>
      <v-spacer />
      <v-toolbar-title>
        <span class="font-weight-light">art</span>
        <span class="text-uppercase white--text">Tastic</span>
      </v-toolbar-title>
      <v-spacer />
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
          v-for="link in links"
          :key="link.text"
        >
          <v-list-item router :to="link.route">
            <v-list-item-icon>
              <v-icon>{{link.icon}}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{link.text}}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
  data: () => ({
    drawer: false,
    links: [
      { icon: "mdi-home", text: "Home", route: "/" },
      { icon: "mdi-chat", text: "Contact", route: "/contact" }
    ]
  })
};
</script>

<style>
</style>