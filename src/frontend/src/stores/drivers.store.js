import { defineStore } from "pinia";

import { driversAllApiV1UserAllPost } from "../client";
import { useAuthStore } from "./auth.store";

export const useDriversStore = defineStore("drivers", {
  state: () => ({
    drivers: JSON.parse(localStorage.getItem("active-drivers")),
    returnUrl: null,
  }),
  actions: {
    async get_all_drivers() {
      const authStore = useAuthStore();
      const token = await authStore.get_token();
      if (token == false) {
        const { default: router } = await import("../router");
        router.push(this.returnUrl || "/login");
        return;
      }
      const drivers = await driversAllApiV1UserAllPost({
        headers: {
          Authorization: "Bearer " + token,
        },
      });

      if (drivers.status == 422) {
        alert("sent data not valid");
        return;
      } else if (drivers.status == 401) {
        const { default: router } = await import("../router");
        router.push(this.returnUrl || "/login");
        return;
      } else if (drivers.status != 200) {
        alert("error in add trip " + drivers.message + " " + drivers.status);
        return;
      }
      this.drivers = drivers;

      localStorage.setItem("active-drivers", JSON.stringify(drivers));
    },
    async get_random_driver() {
      if (this.drivers == null) await this.get_all_drivers();

      let random_driver = null;
      let drivers = JSON.parse(localStorage.getItem("active-drivers"));
      if (drivers.length >= 1) {
        random_driver = drivers[Math.floor(Math.random() * drivers.length)];
      } else {
        random_driver = { id: Math.floor(Math.random() * 100) };
      }
      return random_driver;
    },
    async get_driver_by_id(id) {
      if (this.drivers == null) this.get_all_drivers();

      let drivers = JSON.parse(localStorage.getItem("active-drivers"));
      drivers.forEach((driver) => {
        if (driver.id == id) {
          return driver;
        }
      });
      return false;
    },
  },
});
