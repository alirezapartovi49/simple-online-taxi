<template>
  <div class="app-container bg-light">
    <nav
      v-show="user_loggedin"
      class="navbar navbar-expand navbar-dark bg-dark"
    >
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">تاکسی آنلاین</router-link>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/">خانه</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/rides">سفرهای من</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/profile">پروفایل</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/support">پشتیبانی</router-link>
            </li>
          </ul>
          <form class="d-flex me-3">
            <input
              class="form-control me-2"
              type="search"
              placeholder="جستجو"
              aria-label="Search"
            />
          </form>
          <div class="d-flex align-items-center text-white me-3">
            <i class="fas fa-wallet me-2"></i>
            <span
              >موجودی: {{ authStore.user?.walletBalance || "0" }} تومان</span
            >
          </div>
          <button
            @click="authStore.logout()"
            class="btn btn-outline-light"
            type="button"
          >
            خروج
          </button>
        </div>
      </div>
    </nav>

    <div class="container mt-4">
      <router-view />
    </div>

    <nav
      v-show="authStore.user"
      class="mobile-nav d-md-none bg-white border-top"
    >
      <div class="row g-0">
        <div class="col text-center">
          <router-link to="/" class="nav-link py-2">
            <i class="fas fa-home"></i>
            <small>خانه</small>
          </router-link>
        </div>
        <div class="col text-center">
          <router-link to="/rides" class="nav-link py-2">
            <i class="fas fa-car"></i>
            <small>سفرها</small>
          </router-link>
        </div>
        <div class="col text-center">
          <router-link to="/new-ride" class="nav-link py-2">
            <i
              class="fas fa-plus-circle text-primary"
              style="font-size: 1.5rem"
            ></i>
            <small>سفرو جدید</small>
          </router-link>
        </div>
        <div class="col text-center">
          <router-link to="/profile" class="nav-link py-2">
            <i class="fas fa-user"></i>
            <small>پروفایل</small>
          </router-link>
        </div>
        <div class="col text-center">
          <router-link to="/support" class="nav-link py-2">
            <i class="fas fa-headphones"></i>
            <small>پشتیبانی</small>
          </router-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useAuthStore } from "@/stores";
import "@fortawesome/fontawesome-free/css/all.css";

export default defineComponent({
  name: "App",

  setup() {
    const authStore = useAuthStore();
    let user_loggedin = false;
    if (authStore.user) {
      user_loggedin = true;
    }
    return { authStore, user_loggedin };
  },
});
</script>

<style scoped>
@import "@/assets/base.css";
@import url("https://cdn.fontcdn.ir/Font/Persian/Vazir/Vazir.css ");

* {
  font-family: "Vazir", sans-serif;
  direction: rtl;
}

.nav-item {
  color: white;
}

.mobile-nav {
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: 1000;
}
</style>
