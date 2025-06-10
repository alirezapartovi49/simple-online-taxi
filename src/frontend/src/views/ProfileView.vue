<template>
  <div class="profile-container">
    <h4 class="mb-4">پروفایل کاربری</h4>

    <div class="card profile-card mb-4">
      <div class="card-body text-center">
        <div class="profile-avatar mx-auto mb-3">
          <img
            :src="user.avatar"
            alt="پروفایل"
            class="img-fluid rounded-circle"
          />
          <button class="btn btn-light btn-sm edit-avatar-btn">
            <i class="fas fa-camera"></i>
          </button>
        </div>

        <h5>{{ user.name }}</h5>
        <p class="text-muted">{{ user.email }}</p>
        <p>شماره تماس: {{ user.phone }}</p>
        <button class="btn btn-outline-primary btn-sm" @click="editProfile">
          ویرایش پروفایل
        </button>
      </div>
    </div>

    <div class="card mb-4">
      <div class="card-body">
        <h6 class="card-subtitle mb-3">اطلاعات حساب</h6>

        <div class="d-flex justify-content-between align-items-center mb-3">
          <span>نام کاربری:</span>
          <span class="fw-bold">{{ user.username }}</span>
        </div>

        <div class="d-flex justify-content-between align-items-center mb-3">
          <span>تاریخ ثبت‌نام:</span>
          <span>{{ user.registrationDate }}</span>
        </div>

        <div class="d-flex justify-content-between align-items-center">
          <span>آخرین فعالیت:</span>
          <span>{{ user.lastLogin }}</span>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-body">
        <h6 class="card-subtitle mb-3">کیف پول</h6>

        <div class="d-flex justify-content-between align-items-center mb-3">
          <span>موجودی:</span>
          <span class="fw-bold">{{ user.walletBalance }} تومان</span>
        </div>

        <button class="btn btn-outline-success btn-sm" @click="addFunds">
          افزایش موجودی
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "ProfileView",
  setup() {
    const router = useRouter();
    const user = ref({
      name: "علی محمدی",
      email: "ali@example.com",
      phone: "۰۹۱۲۳۴۵۶۷۸۹",
      username: "alimohammadi",
      registrationDate: "۱۴۰۲/۰۱/۱۵",
      lastLogin: "۱۴۰۲/۰۴/۱۵ ۱۴:۳۰",
      walletBalance: "۱۲۵,۰۰۰",
      avatar: "https://placehold.co/150x150 ",
    });

    const editProfile = () => {
      router.push("/profile/edit");
    };

    const addFunds = () => {
      router.push("/profile/add-funds");
    };

    return {
      user,
      editProfile,
      addFunds,
    };
  },
};
</script>

<style scoped>
.profile-container {
  padding: 1rem;
}

.profile-card {
  border-radius: 1rem;
}

.profile-avatar {
  position: relative;
  width: 100px;
  height: 100px;
}

.profile-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.edit-avatar-btn {
  position: absolute;
  bottom: 0;
  right: 0;
  border-radius: 50%;
  padding: 0.3rem;
  font-size: 0.75rem;
}
</style>
