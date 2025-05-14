<template>
  <div class="app-container bg-light">
    <nav
      v-show="authStore.user"
      class="navbar navbar-expand navbar-dark bg-dark"
    >
      <div class="navbar-nav">
        <router-link to="/">Home</router-link> |
        <a @click="authStore.logout()" class="nav-item nav-link">Logout</a>
      </div>
    </nav>
  </div>
  <router-view />
</template>

<script>
import { defineComponent } from "vue";
import { useAuthStore } from "@/stores";
import "@fortawesome/fontawesome-free/css/all.css";
import "@/assets/tailwind.css";

export default defineComponent({
  name: "App",
  setup() {
    const authStore = useAuthStore(); // ← now runs after Pinia is installed
    return { authStore };
  },
});
</script>

<style>
@import "@/assets/base.css";
@import url("https://cdn.fontcdn.ir/Font/Persian/Vazir/Vazir.css");

* {
  font-family: "Vazir", sans-serif;
  direction: rtl;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
