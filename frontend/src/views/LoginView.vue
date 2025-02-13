<script setup>
import { reactive, ref } from "vue";
import axios from "axios";

const apiUrl = import.meta.env.VITE_API_URL;
const user = reactive({
  username: "",
  password: "",
});
const isLoggedIn = ref(!!localStorage.getItem("token"));
const loginMessage = ref("");

/** 🔹 Fonction pour se connecter et obtenir un token JWT */
const login = async (event) => {
  event.preventDefault(); // Empêche la soumission du formulaire

  try {
    const response = await axios.post(`${apiUrl}/api/token/`, {
      username: user.username,
      password: user.password,
    });

    // Stocker le token
    localStorage.setItem("token", response.data.access);
    localStorage.setItem("refresh_token", response.data.refresh);
    isLoggedIn.value = true;
    loginMessage.value = "Connexion réussie !";
  } catch (error) {
    loginMessage.value =
      error.response?.data?.detail || "Identifiants incorrects.";
  }
};

/** 🔹 Fonction pour se déconnecter */
const logout = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("refresh_token");
  isLoggedIn.value = false;
  loginMessage.value = "Déconnecté.";
};
</script>

<template>
  <div
    v-if="!isLoggedIn"
    class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"
  >
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <!-- <img
        class="mx-auto h-10 w-auto"
        src="https://tailwindui.com/plus-assets/img/logos/mark.svg?color=green&shade=600"
        alt="Your Company"
      /> -->
      <h2 class="mt-10 text-center text-2xl font-bold text-gray-900">
        Se connecter
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit="login">
        <div>
          <label for="username" class="block text-sm font-medium text-gray-900"
            >Nom d'utilisateur</label
          >
          <div class="mt-2">
            <input
              v-model="user.username"
              type="text"
              id="username"
              required
              class="block w-full rounded-md border-gray-300 px-3 py-1.5 text-gray-900 focus:outline-green-600"
            />
          </div>
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-900"
            >Mot de passe</label
          >
          <div class="mt-2">
            <input
              v-model="user.password"
              type="password"
              id="password"
              required
              class="block w-full rounded-md border-gray-300 px-3 py-1.5 text-gray-900 focus:outline-green-600"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-green-600 px-3 py-1.5 text-sm font-semibold text-white hover:bg-green-500"
          >
            Se connecter
          </button>
        </div>
      </form>

      <p class="mt-4 text-center text-sm text-red-500" v-if="loginMessage">
        {{ loginMessage }}
      </p>
    </div>
  </div>

  <div v-else class="text-center mt-10">
    <p class="text-lg font-bold">Bienvenue !</p>
    <button
      @click="logout"
      class="mt-4 rounded-md bg-red-500 px-4 py-2 text-white hover:bg-red-400"
    >
      Se déconnecter
    </button>
  </div>
</template>
