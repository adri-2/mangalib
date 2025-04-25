<template>
  <div v-if="livre">
    <h1 class="bg-green-600 text-center h-[100px] items-center">
      {{ livre.title }}
    </h1>
    <p class="viole">Auteur : {{ livre.author }}</p>
    <p class="viole">Quantité : {{ livre.description }}</p>
  </div>
  <div v-else>
    <p>Chargement des données...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
const apiUrl = import.meta.env.VITE_API_URL;

const route = useRoute();
const livre = ref(null);

onMounted(() => {
  const livreId = route.params.id;
  axios
    .get(`http://localhost:8000/api/manga/${livreId}/`)
    .then((response) => {
      livre.value = response.data;
    })
    .catch((error) => {
      console.error("Erreur lors du chargement du livre:", error);
    });
});
</script>
