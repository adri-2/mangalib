<template>
  <div class="bg-gray-900 text-white min-h-screen">
    <!-- Navigation Bar -->
    <!-- <header class="flex justify-between items-center px-6 py-4 bg-gray-800">
      <div class="flex items-center gap-4">
        <img
          src="https://img.icons8.com/ios-filled/50/orange/tachiyomi.png"
          alt="Crunchyroll Logo"
          class="h-6"
        />
        <nav class="flex gap-4 text-sm">
          <a href="#" class="hover:text-orange-400">Nouveau</a>
          <a href="#" class="hover:text-orange-400">Populaire</a>
          <a href="#" class="hover:text-orange-400">Simulcast</a>
          <a href="#" class="hover:text-orange-400">Catégories</a>
          <a href="#" class="hover:text-orange-400">Jeux</a>
        </nav>
      </div>
      <div class="flex gap-4 text-sm">
        <button
          class="text-orange-400 border border-orange-400 px-3 py-1 rounded hover:bg-orange-500 hover:text-white"
        >
          ESSAI GRATUIT PREMIUM
        </button>
        <button><i class="fas fa-search"></i></button>
        <button><i class="fas fa-bookmark"></i></button>
        <button><i class="fas fa-user"></i></button>
      </div>
    </header> -->

    <!-- Hero Carousel -->
    <section class="relative h-[600px] overflow-hidden">
      <div
        class="w-full h-full bg-cover bg-center transition-all duration-700"
        :style="{ backgroundImage: `url(${slides[currentSlide].image})` }"
      >
        <div
          class="absolute inset-0 bg-black bg-opacity-60 flex flex-col justify-center px-12 h-[600px]"
        >
          <img
            :src="slides[currentSlide].logo"
            alt="Anime Logo"
            class="w-64 mb-4"
          />
          <p class="max-w-xl mb-4 text-sm">
            {{ slides[currentSlide].description }}
          </p>
          <button
            class="bg-orange-500 px-4 py-2 rounded text-sm hover:bg-orange-600"
          >
            ▶ LECTURE S1 E1
          </button>
        </div>

        <!-- Navigation Buttons -->
        <button
          @click="prevSlide"
          class="absolute left-2 top-1/2 transform -translate-y-1/2 text-2xl bg-black bg-opacity-50 p-2 rounded-full"
        >
          ‹
        </button>
        <button
          @click="nextSlide"
          class="absolute right-2 top-1/2 transform -translate-y-1/2 text-2xl bg-black bg-opacity-50 p-2 rounded-full"
        >
          ›
        </button>
      </div>
    </section>

    <!-- Top Picks Section -->
    <section class="px-6 py-8">
      <h2 class="text-xl font-bold mb-4">Top Picks for You</h2>
      <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
        <div
          v-for="anime in animes"
          :key="anime.title"
          class="bg-gray-800 rounded overflow-hidden hover:scale-105 transform transition"
        >
          <img
            :src="anime.image"
            alt="anime.title"
            class="w-full h-48 object-cover"
          />
          <div class="p-2">
            <h3 class="text-sm font-semibold">{{ anime.title }}</h3>
            <p class="text-xs text-gray-400">Sous-titrage | Doublage</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentSlide: 0,
      slides: [
        {
          image: 'photo_2024-12-15_15-20-03.jpg',
          logo: 'https://static.crunchyroll.com/fms/logo/25769/myheroacademia_logo.png',
          description:
            "Izuku has dreamt of being a hero all his life... But that's not enough to stop him from enrolling in one of the world's most prestigious hero academies.",
        },
        {
          image: 'https://static.crunchyroll.com/fms/landscape_large/65e10d87e1c2fbb1b0a979ee77a1d135.jpg',
          logo: 'https://static.crunchyroll.com/fms/logo/28749/sololeveling_logo.png',
          description: "Solo Leveling – Une nouvelle ère commence pour les chasseurs.",
        },
        {
          image: 'https://static.crunchyroll.com/fms/landscape_large/65e11390cd07147e0c1449e4ad19ad55.jpg',
          logo: 'https://static.crunchyroll.com/fms/logo/25875/vinlandsaga_logo.png',
          description: "Vinland Saga – Le combat pour la liberté commence.",
        },
      ],
      animes: [
        {
          title: 'My Hero Academia',
          image: 'https://static.crunchyroll.com/fms/portrait_large/25769/myheroacademia_keyart.jpg',
        },
        {
          title: 'Solo Leveling',
          image: 'https://static.crunchyroll.com/fms/portrait_large/28749/sololeveling_keyart.jpg',
        },
        {
          title: "Les Carnets de l'apothicaire",
          image: 'https://static.crunchyroll.com/fms/portrait_large/30789/apothecarydiaries_keyart.jpg',
        },
        {
          title: 'Dr. STONE',
          image: 'https://static.crunchyroll.com/fms/portrait_large/29093/drstone_keyart.jpg',
        },
        {
          title: 'VINLAND SAGA',
          image: 'https://static.crunchyroll.com/fms/portrait_large/25875/vinlandsaga_keyart.jpg',
        },
        {
          title: 'MASHLE: MAGIC AND MUSCLES',
          image: 'https://static.crunchyroll.com/fms/portrait_large/28285/mashle_keyart.jpg',
        },
        {
          title: 'Classroom of the Elite',
          image: 'https://static.crunchyroll.com/fms/portrait_large/27593/classroomelite_keyart.jpg',
        },
      ],
    };
  },
  methods: {
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length;
    },
    prevSlide() {
      this.currentSlide =
        (this.currentSlide - 1 + this.slides.length) % this.slides.length;
    },
  },
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
</style>
