<template>
  <div>
    <h1>Hi {{ user?.firstName }}!</h1>
    <p>You're logged in with Vue 3 + Pinia & JWT!!</p>
    <h3>Users from secure api end point:</h3>
  </div>
</template>

<script lang="js">
import { Options, Vue } from "vue-class-component";
import { storeToRefs } from "pinia";
import { useAuthStore } from "@/stores";

@Options({})
export default class HomeView extends Vue {
  authUser = null;
  created() {
    const authStore = useAuthStore();
    this.authUser = storeToRefs(authStore).user;
  }
}
</script>
