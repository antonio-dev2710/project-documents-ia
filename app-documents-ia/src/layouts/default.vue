<template>
  <v-layout>
    <v-app-bar
      color="primary"
      density="compact"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-app-bar-title>Documents IA</v-app-bar-title>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      :location="'left'"
      temporary
    >
      <v-list
        :items="items"
      />
    </v-navigation-drawer>
    <v-main>
      <router-view />
    </v-main>
  </v-layout>
</template>

<script>
  export default {
    data() {
      return {
        drawer: false,
        items: [
          {
            title: 'Home',
            value: 'home',
          },
          {
            title: 'About',
            value: 'about',
          },
        ],
      }
    }
  }
</script>