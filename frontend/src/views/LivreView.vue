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
    <Popup><LivreForm @vue:updated="fetchLivres()" /></Popup>
    <div
      class="max-w-2xl mx-auto px-4 py-6 lg:max-w-6xl grid grid-cols-1 gap-y-10 gap-x-8 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-4"
    >
      <div
        class="bg-white shadow-lg rounded-lg"
        v-for="livre in livreFilter"
        :key="livre.id"
      >
        <img
          :src="livre.cover_image || '/default-image.jpg'"
          alt="Image du livre"
          class="rounded-t-lg w-full h-60 object-cover"
        />
        <div class="p-4">
          <div class="flex mb-5">
            <h3 class="text-2xl text-gray-700 font-semibold">
              {{ livre.title }}
            </h3>
            <!-- <p class="mt-1 ml-auto text-lg font-medium text-gray-900">
              {{ livre.date }}
            </p> -->
          </div>
          <RouterLink
            :to="`manga/${livre.id}`"
            class="text-gray-100 text-lg font-center justify-between px-5 py-1 shadow-sm font-medium rounded-md bg-red-600 flex items-center"
          >
            <span class="text-gray-100">Voir</span>
          </RouterLink>
        </div>
      </div>
    </div>

    <!-- PAGINATION -->
    <div class="flex justify-center space-x-4 mt-6">
      <button
        v-if="prev_page"
        @click="fetchLivres(prev_page)"
        class="px-4 py-2 bg-blue-600 text-white rounded-md"
      >
        Précédent
      </button>
      <button
        v-if="next_page"
        @click="fetchLivres(next_page)"
        class="px-4 py-2 bg-blue-600 text-white rounded-md"
      >
        Suivant
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";
import LivreForm from "./LivreForm.vue";
import Popup from "../components/Popup.vue";

const livres = ref([]);
const searchquery = ref("");
const next_page = ref(null);
const prev_page = ref(null);

// Fonction pour récupérer les livres depuis l'API
const fetchLivres = (url = "http://localhost:8000/api/manga/") => {
  axios
    .get(url)
    .then((response) => {
      livres.value = response.data;
      next_page.value = response.data.next;
      prev_page.value = response.data.previous;
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
        item.title.toLowerCase().includes(searchquery.value.toLowerCase())
      )
    : [];
});

onMounted(fetchLivres);
</script>
