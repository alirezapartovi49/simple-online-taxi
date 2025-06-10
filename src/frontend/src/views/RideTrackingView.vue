<template>
  <div class="ride-tracking-view">
    <div class="container mt-4">
      <div class="d-flex justify-content-between align-items-center mb-4">
        <h4>پیگیری سفر</h4>
        <button @click="cancelRide" class="btn btn-outline-secondary btn-sm">
          لغو سفر
        </button>
      </div>

      <RideTrackingComponent />

      <div class="mt-4">
        <button @click="cancelRide" class="btn btn-outline-danger w-100">
          لغو سفر
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import RideTrackingComponent from "@/components/RideTracking.vue";

const router = useRouter();
const cancelRide = () => {
  if (confirm("آیا از لغو سفر مطمئن هستید؟")) {
    router.push("/");
  }
};
</script>

<style scoped>
.ride-tracking-view {
  padding: 1rem;
}
</style>
