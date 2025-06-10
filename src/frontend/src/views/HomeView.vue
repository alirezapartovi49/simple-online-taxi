<template>
  <div class="home-container">
    <div class="row g-3">
      <!-- Location Search -->
      <div class="col-12">
        <div class="card location-card shadow-sm">
          <div class="card-body">
            <div class="input-group mb-3">
              <span class="input-group-text">
                <i class="fas fa-map-marker-alt"></i>
              </span>
              <input
                type="text"
                class="form-control"
                placeholder="محل شروع سفر"
                v-model="rideData.startLocation"
              />
            </div>
            <div class="input-group">
              <span class="input-group-text">
                <i class="fas fa-flag"></i>
              </span>
              <input
                type="text"
                class="form-control"
                placeholder="مقصد سفر"
                v-model="rideData.endLocation"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- Map -->
      <div class="col-12">
        <div class="map-container position-relative">
          <div class="map-placeholder">
            <i class="fas fa-map fa-3x text-muted mb-3"></i>
            <p class="text-muted">نقشه در حال بارگذاری...</p>
          </div>
        </div>
      </div>

      <!-- Vehicle Types -->
      <div class="col-12">
        <h5 class="mb-3">نوع خودرو</h5>
        <div class="row g-3">
          <div
            v-for="vehicle in vehicleTypes"
            :key="vehicle.id"
            class="col-6 col-md-3"
          >
            <div
              class="card vehicle-card text-center p-3"
              :class="{ active: selectedVehicle === vehicle.id }"
              @click="selectVehicle(vehicle.id)"
            >
              <img
                :src="vehicle.image"
                class="vehicle-image mx-auto mb-2"
                :alt="vehicle.name"
              />
              <h6>{{ vehicle.name }}</h6>
              <p class="text-muted mb-0">{{ vehicle.price }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Ride Info -->
      <div class="col-12">
        <div class="card info-card">
          <div
            class="card-body d-flex flex-wrap justify-content-around text-center"
          >
            <div>
              <i class="fas fa-clock fa-lg text-primary mb-2"></i>
              <div>زمان انتظار: {{ rideInfo.waitTime }} دقیقه</div>
            </div>
            <div>
              <i class="fas fa-route fa-lg text-success mb-2"></i>
              <div>مسافت: {{ rideInfo.distance }} کیلومتر</div>
            </div>
            <div>
              <i class="fas fa-money-bill-wave fa-lg text-warning mb-2"></i>
              <div>هزینه: {{ rideInfo.cost }} تومان</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Request Button -->
      <div class="col-12">
        <button
          class="btn btn-primary btn-lg w-100"
          @click="requestRide"
          :disabled="!canRequestRide"
        >
          درخواست سفر
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { useTripStore, useDriversStore } from "@/stores";

export default {
  name: "HomeView",
  setup() {
    const tripStore = useTripStore();
    const driverStore = useDriversStore();
    const router = useRouter();
    const rideData = ref({
      startLocation: "",
      endLocation: "",
      vehicleType: null,
    });

    const vehicleTypes = [
      {
        id: 1,
        name: "اقتصادی",
        price: "۲۵,۰۰۰",
        image: "https://placehold.co/600x400?text= اقتصادی",
      },
      {
        id: 2,
        name: "لوکس",
        price: "۳۵,۰۰۰",
        image: "https://placehold.co/600x400?text= لوکس",
      },
      {
        id: 3,
        name: "باربری",
        price: "۴۵,۰۰۰",
        image: "https://placehold.co/600x400?text= باربری",
      },
      {
        id: 4,
        name: "موتور",
        price: "۱۵,۰۰۰",
        image: "https://placehold.co/600x400?text= موتور",
      },
    ];

    const selectedVehicle = ref(null);
    const rideInfo = ref({
      waitTime: 5,
      distance: 8.5,
      cost: 32000,
    });

    const selectVehicle = (vehicleId) => {
      selectedVehicle.value = vehicleId;
      rideData.value.vehicleType = vehicleId;
    };

    const canRequestRide = computed(() => {
      return (
        rideData.value.startLocation &&
        rideData.value.endLocation &&
        rideData.value.vehicleType
      );
    });

    const requestRide = async () => {
      let random_driver = await driverStore.get_random_driver();
      let driver_id = random_driver.id;
      tripStore.create_trip(
        driver_id,
        selectedVehicle.value.price | rideInfo.value.cost,
        rideData.value.startLocation,
        rideData.value.endLocation
      );
      router.push("/ride-tracking");
    };

    return {
      rideData,
      vehicleTypes,
      selectedVehicle,
      rideInfo,
      selectVehicle,
      canRequestRide,
      requestRide,
    };
  },
};
</script>

<style scoped>
.home-container {
  padding: 1rem;
}

.location-card .form-control {
  border-radius: 1rem;
  padding: 0.75rem 1rem;
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

.vehicle-card {
  border-radius: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.vehicle-card:hover,
.vehicle-card.active {
  border-color: #4a90e2;
  transform: translateY(-5px);
}

.vehicle-image {
  width: 60px;
  height: 40px;
  object-fit: cover;
  border-radius: 0.5rem;
}

.info-card {
  border-radius: 1rem;
}

.btn-primary {
  background: linear-gradient(135deg, #4a90e2, #357abd);
  border: none;
  border-radius: 1rem;
  font-weight: 600;
}

.btn-primary:disabled {
  background: #bdc3c7;
}
</style>
