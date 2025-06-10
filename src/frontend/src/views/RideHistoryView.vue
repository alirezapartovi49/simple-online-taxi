<template>
  <div class="rides-container">
    <h4 class="mb-4">سفرهای اخیر</h4>

    <div v-if="rides.length === 0" class="text-center py-5">
      <i class="fas fa-car fa-3x text-muted mb-3"></i>
      <p class="text-muted">هیچ سفری یافت نشد</p>
    </div>

    <div v-else>
      <div
        v-for="ride in rides"
        :key="ride.id"
        class="card ride-card mb-3"
        @click="viewRideDetails(ride.id)"
      >
        <div class="card-body">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <div class="fw-bold">{{ ride.date }}</div>
              <div class="text-muted small">{{ ride.time }}</div>
            </div>
            <div class="badge bg-primary">{{ ride.status }}</div>
          </div>

          <div class="mt-3">
            <div class="d-flex align-items-start">
              <i class="fas fa-map-marker-alt text-success mt-1 me-2"></i>
              <div class="flex-grow-1">
                <div class="fw-bold">از: {{ ride.from }}</div>
                <div class="text-muted small">{{ ride.startAddress }}</div>
              </div>
            </div>

            <div class="d-flex align-items-start mt-2">
              <i class="fas fa-flag text-danger mt-1 me-2"></i>
              <div class="flex-grow-1">
                <div class="fw-bold">به: {{ ride.to }}</div>
                <div class="text-muted small">{{ ride.endAddress }}</div>
              </div>
            </div>
          </div>

          <div class="d-flex justify-content-between align-items-center mt-3">
            <div><i class="fas fa-car me-1"></i> {{ ride.vehicleType }}</div>
            <div class="fw-bold">{{ ride.cost }} تومان</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "RideHistoryView",
  setup() {
    const router = useRouter();
    const rides = ref([
      {
        id: 1,
        date: "۱۴۰۲/۰۴/۱۵",
        time: "۱۴:۳۰",
        status: "تکمیل شده",
        from: "دفتر کار",
        to: "فرودگاه",
        startAddress: "خیابان آزادی، تهران",
        endAddress: "فرودگاه امام خمینی",
        vehicleType: "اقتصادی",
        cost: "۳۵,۰۰۰",
      },
      {
        id: 2,
        date: "۱۴۰۲/۰۴/۱۲",
        time: "۰۹:۱۵",
        status: "لغو شده",
        from: "خانه",
        to: "بیمارستان",
        startAddress: "خیابان ولیعصر، تهران",
        endAddress: "بیمارستان میلاد",
        vehicleType: "موتور",
        cost: "۱۵,۰۰۰",
      },
      {
        id: 3,
        date: "۱۴۰۲/۰۴/۰۸",
        time: "۱۸:۴۵",
        status: "تکمیل شده",
        from: "دانشگاه",
        to: "خانه",
        startAddress: "دانشگاه شریف",
        endAddress: "خیابان فرشته، تهران",
        vehicleType: "اقتصادی",
        cost: "۲۵,۰۰۰",
      },
    ]);

    const viewRideDetails = (rideId) => {
      router.push(`/ride/${rideId}`);
    };

    return {
      rides,
      viewRideDetails,
    };
  },
};
</script>

<style scoped>
.rides-container {
  padding: 1rem;
}

.ride-card {
  border-radius: 1rem;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.ride-card:hover {
  transform: translateX(5px);
}

.ride-card .card-body {
  padding: 1rem;
}
</style>
