<template>
  <div class="bg-gray-200">
    <h1 class="text-center text-6xl py-7">
      La <span class="font-bold">Bibliothèque Mangalib</span>
    </h1>
    <input
      type="text"
      v-model="searchquery"
      placeholder="Rechercher un livre..."
      class="border border-gray-300 p-2 rounded w-full max-w-md mx-auto block"
    />
    <Popup><LivreForm @vue:updated="fetchLivres" /></Popup>
    <div
      class="max-w-2xl mx-auto px-4 py-6 lg:max-w-6xl grid grid-cols-1 gap-y-10 gap-x-8 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-4"
    >
      <div
        class="bg-white shadow-lg rounded-lg"
        v-for="livre in livreFilter"
        :key="livre.id"
      >
        <img
          src="../../public/photo_2024-12-15_15-19-55.jpg"
          alt="Image du livre"
          class="rounded-t-lg"
        />
        <div class="p-4">
          <div class="flex mb-5">
            <h3 class="text-2xl text-gray-700 font-semibold">
              {{ livre.titre }}
            </h3>
            <p class="mt-1 ml-auto text-lg font-medium text-gray-900">
              {{ livre.quantity }}
            </p>
          </div>
          <RouterLink
            :to="`/livre/${livre.id}`"
            class="text-gray-100 text-lg font-center justify-between px-5 py-1 shadow-sm font-medium rounded-md bg-red-600 flex items-center"
          >
            <span class="text-gray-100">Voir</span>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";
import LivreForm from "./LivreForm.vue";
import Popup from "../components/Popup.vue";

const apiUrl = import.meta.env.VITE_API_URL;
const livres = ref([]);
const searchquery = ref("");

// Fonction pour récupérer les livres depuis l'API
const fetchLivres = () => {
  axios
    .get(`${apiUrl}/livre/`)
    .then((response) => {
      livres.value = response.data;
    })
    .catch((error) => {
      console.error(
        "Erreur lors de la récupération des livres:",
        error.response?.data || error.message
      );
    });
};

// Filtrage des livres en fonction du terme recherché
const livreFilter = computed(() => {
  return livres.value?.length
    ? livres.value.filter((item) =>
        item.titre.toLowerCase().includes(searchquery.value.toLowerCase())
      )
    : [];
});

onMounted(fetchLivres);
</script>
