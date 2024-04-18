<template>
  <v-container :fluid="true" class="container">
  <template v-for="person in people">
    <PeopleCard :person=person></PeopleCard>
    <v-spacer></v-spacer>
  </template>
  </v-container>
</template>

<script setup>
import PeopleCard from '@/components/PeopleCard.vue';
import { usePeopleStore } from '@/stores/people';
import { onMounted } from 'vue';
import { ref } from 'vue';

const store = usePeopleStore()
const people = ref(null)

onMounted(() => {
  people.value = store.people;
})

</script>

<style>
.container {
  display: flex;
  flex-wrap: wrap;
}
</style>