<template>
  <v-app>
    <v-app-bar color="indigo" class="flex-grow-0" app>
      <v-app-bar-title>
        <router-link class="link" to="/">
          <font-awesome-icon icon="house" />
        </router-link>
        Informações de Triangulos
      </v-app-bar-title>
    </v-app-bar>
    <v-container>
      <v-navigation-drawer>
        <v-list-item link title="Formula base altura" to="/bh"></v-list-item>
        <v-list-item link title="Formula de Heron" to="/abc"></v-list-item>
        <v-list-item link title="Formula do perimetro" to="/perimetro"></v-list-item>
      </v-navigation-drawer>
      <v-main>
        <router-view> </router-view>
      </v-main>
    </v-container>
  </v-app>
</template>

<style>
.link {
  text-decoration: none;
  color: rgb(255 255 255);
}

.link:hover {
  color: gray;
}
</style>
