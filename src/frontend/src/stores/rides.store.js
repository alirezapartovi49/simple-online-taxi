import { defineStore } from "pinia";

import {
  createTripApiV1TripAddTripPost,
  userTripsApiV1TripAllPost,
} from "../client";
import { useAuthStore } from "./auth.store";

export const useTripStore = defineStore("trip", {
  state: () => ({
    trip: JSON.parse(localStorage.getItem("active-trip")),
    returnUrl: null,
  }),
  actions: {
    async create_trip(driver_id, price, from_address, to_address) {
      const authStore = useAuthStore();
      const token = await authStore.get_token();
      if (token == false) {
        const { default: router } = await import("../router");
        router.push(this.returnUrl || "/");
        return;
      }
      const trip = await createTripApiV1TripAddTripPost({
        body: {
          driver_id: driver_id,
          fare: price,
          from_address: from_address,
          to_address: to_address,
        },
        headers: {
          Authorization: "Bearer " + token,
        },
      });

      if (trip.status == 422) {
        alert("sent data not valid");
        return;
      } else if (trip.status == 401) {
        const { default: router } = await import("../router");
        router.push(this.returnUrl || "/login");
        return;
      } else if (trip.status != 200) {
        alert("error in add trip " + trip.message + " " + trip.status);
        return;
      }
      this.trip = trip;

      localStorage.setItem("active-trip", JSON.stringify(trip));
    },
    async get_trips() {
      const authStore = useAuthStore();
      const token = await authStore.get_token();
      if (token == false) {
        const { default: router } = await import("../router");
        router.push(this.returnUrl || "/login");
        return;
      }
      const trips = await userTripsApiV1TripAllPost({
        headers: {
          Authorization: "Bearer " + token,
        },
      });

      if (trips.status == 422) {
        alert("sent data not valid");
        return;
      } else if (trips.status == 401) {
        const { default: router } = await import("../router");
        router.push(this.returnUrl || "/login");
        return;
      } else if (trips.status != 200) {
        alert("error in add trip " + trips.message + " " + trips.status);
        return;
      }

      return trips;
    },
    async get_last_trip() {
      let trips = this.get_trips();
      let last_trip = trips.data[trips.data.length - 1];
      alert(last_trip);
      return last_trip;
    },
  },
});
