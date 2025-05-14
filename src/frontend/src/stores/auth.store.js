import { defineStore } from "pinia";

import {
  loginForAccessTokenApiV1UserAuthLoginPost,
  registerUserApiV1UserAuthRegisterPost,
} from "../client";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: JSON.parse(localStorage.getItem("user")),
    returnUrl: null,
  }),
  actions: {
    async login(username, password) {
      const user = await loginForAccessTokenApiV1UserAuthLoginPost({
        body: {
          username: username,
          password: password,
          grant_type: "password",
          scope: "",
        },
      });

      if (user.status == 401) {
        alert("نام کاربری و یا رمز عبور اشتباه است");
        return;
      } else if (user.status != 200) {
        alert("error in login" + user.message);
        return;
      }
      this.user = user;

      localStorage.setItem("user", JSON.stringify(user));

      const { default: router } = await import("../router");
      router.push(this.returnUrl || "/");
    },
    async register(username, password, email) {
      const user = await registerUserApiV1UserAuthRegisterPost({
        body: {
          username: username,
          password: password,
          email: email,
        },
      });

      if (user.status == 409) {
        alert("نام کاربری و یا ایمیل تکراری است");
        return;
      } else if (user.status != 201) {
        alert("error in login" + " " + user.message + " " + user.status);
        return;
      }

      alert("موفقیت امیز بود به صفحه لاگین هدایت میشوید");
      const { default: router } = await import("../router");
      router.push(this.returnUrl || "/login");
    },
    async logout() {
      this.user = null;
      localStorage.removeItem("user");
      const { default: router } = await import("../router");
      router.push("/login");
    },
  },
});
