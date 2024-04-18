<template>
  <!-- <v-app-bar flat>
    <v-app-bar-title>
      <RouterLink to="/">Graph</RouterLink> 
      <RouterLink to="/PeopleCards">Cards</RouterLink> 
      <RouterLink to="/Upload">Upload</RouterLink> 
    </v-app-bar-title>
  </v-app-bar> -->
  <v-navigation-drawer expand-on-hover rail>
    <v-list nav>
      <v-list-item prepend-icon="mdi-graph" title="Graph" value="graph" to="/Graph"></v-list-item>
      <v-list-item prepend-icon="mdi-account" title="Cards" value="card" to="/PeopleCards"></v-list-item> 
      <v-list-item prepend-icon="mdi-upload" title="Upload Data" value="upload" to="/Upload"></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
  //
</script>
