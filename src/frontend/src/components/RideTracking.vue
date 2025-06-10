<template>
  <div class="ride-tracking-component">
    <div v-if="loading" class="card tracking-card mb-4 text-center p-4">
      <h5>در حال بارگذاری اطلاعات...</h5>
      <div class="spinner-border text-primary my-3"></div>
    </div>

    <div
      v-else-if="error"
      class="card tracking-card mb-4 text-center p-4 text-danger"
    >
      {{ error }}
    </div>

    <div v-else class="card tracking-card mb-4">
      <div class="card-body text-center">
        <h5 class="card-title">اطلاعات سفر</h5>
        <p><strong>مبدا:</strong> {{ trip_data.from_address }}</p>
        <p><strong>مقصد:</strong> {{ trip_data.to_address }}</p>
        <p><strong>هزینه:</strong> {{ trip_data.price }}</p>
      </div>
    </div>

    <div v-if="!driverFound && !error" class="card tracking-card mb-4">
      <div class="card-body text-center">
        <h5 class="card-title">در حال جستجوی راننده...</h5>
        <div class="spinner-border text-primary my-3" role="status"></div>
        <p class="mt-2">
          لطفاً منتظر بمانید. ما بهترین راننده را برای شما پیدا می‌کنیم.
        </p>
      </div>
    </div>

    <div v-if="driverFound && driver" class="card driver-card mb-4">
      <div class="card-body">
        <div class="row align-items-center">
          <div class="col-auto">
            <div class="driver-avatar rounded-circle overflow-hidden">
              <img :src="driver.avatar" alt="راننده" class="img-fluid" />
            </div>
          </div>
          <div class="col">
            <h6 class="mb-1">{{ driver.name }}</h6>
            <p class="mb-0 text-muted small">خودرو: {{ driver.carModel }}</p>
            <p class="mb-0 text-muted small">پلاک: {{ driver.licensePlate }}</p>
          </div>
          <div class="col-auto">
            <button class="btn btn-outline-primary btn-sm">
              <i class="fas fa-phone"></i>
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="map-container position-relative mt-3">
      <div class="map-placeholder text-center py-5">
        <i class="fas fa-map fa-3x text-muted mb-3"></i>
        <p class="text-muted">موقعیت راننده در حال بارگذاری...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useTripStore, useDriversStore } from "@/stores";

const loading = ref(true);
const error = ref(null);
const driverFound = ref(false);
const driver = ref(null);

const trip_data = ref({
  from_address: "نامشخص",
  to_address: "نامشخص",
});

onMounted(async () => {
  try {
    const tripStore = useTripStore();
    const driversStore = useDriversStore();

    let trip;

    if (tripStore.trip) {
      trip = tripStore.trip;
    } else {
      trip = await tripStore.get_last_trip();
      if (!trip || !trip.from_address) {
        throw new Error("هیچ سفری یافت نشد.");
      }
    }

    trip_data.value = {
      from_address: trip.data.from_address,
      to_address: trip.data.to_address,
      price: trip.data.fare,
    };

    let driverData;

    if (trip.driver_id) {
      driverData = await driversStore.get_driver_by_id(trip.driver_id);
    }

    if (!driverData) {
      driverData = driversStore.get_random_driver;
    }

    if (driverData) {
      driver.value = {
        id: driverData.id,
        name: driverData.name || "علی محمدی",
        carModel: driverData.carModel || "پراید ۱۴۱",
        licensePlate: driverData.licensePlate || "۱۲۳۴ ا ب ۵۶",
        avatar: driverData.avatar || "https://placehold.co/150x150 ",
      };

      setTimeout(() => {
        driverFound.value = true;
      }, 4000);
    }

    loading.value = false;
  } catch (err) {
    console.error(err);
    error.value = "خطا در بارگذاری اطلاعات.";
    loading.value = false;
  }
});
</script>

<style scoped>
.ride-tracking-component {
  padding: 1rem;
}

.tracking-card {
  border-radius: 1rem;
}

.driver-card {
  border-radius: 1rem;
}

.driver-avatar {
  width: 60px;
  height: 60px;
}

.map-container {
  height: 300px;
  border-radius: 1rem;
  overflow: hidden;
  background-color: #f8f9fa;
}

.map-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>
