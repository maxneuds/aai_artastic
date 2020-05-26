<template>
  <v-app-bar
    absolute
    color="#6A76AB"
    dark
    shrink-on-scroll
    prominent
    src="https://picsum.photos/1920/1080?random"
    scroll-target="#scrolling-techniques-5"
  >
    <template v-slot:img="{ props }">
      <v-img v-bind="props" gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"></v-img>
    </template>

    <v-app-bar-nav-icon></v-app-bar-nav-icon>
    <v-spacer />
    <v-toolbar-title id="title" class="title">Artastic!</v-toolbar-title>
    <v-spacer />
  </v-app-bar>
</template>

<style scoped>
#title {
  font-family: unquote("Roboto");
}
</style>