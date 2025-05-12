import { defineStore } from "pinia";
import { router } from "@router/index";

import { loginForAccessTokenApiV1UserAuthLoginPost } from "@client/index";

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    user: JSON.parse(localStorage.getItem("user")),
    returnUrl: null,
  }),
  actions: {
    async login(username, password) {
      const user = await loginForAccessTokenApiV1UserAuthLoginPost({
        username: username,
        password: password,
      });
      this.user = user;
      localStorage.setItem("user", JSON.stringify(user));
      router.push(this.returnUrl || "/");
    },
    async register(username, password, email) {
      const user = await loginForAccessTokenApiV1UserAuthLoginPost({
        username: username,
        password: password,
        email: email,
      });
      this.user = user;
      router.push("/login");
    },
    logout() {
      this.user = null;
      localStorage.removeItem("user");
      router.push("/login");
    },
  },
});
