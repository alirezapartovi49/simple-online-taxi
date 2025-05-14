<template>
  <div class="login-wrapper">
    <div class="login-card">
      <!-- هدر -->
      <div class="login-header text-center">
        <div class="login-logo">🚕</div>
        <h1>تاکسی آنلاین</h1>
        <p class="login-demo-info">
          اطلاعات آزمایشی: <strong>نام کاربری</strong>: test /
          <strong>رمز</strong>: test
        </p>
      </div>

      <!-- فرم -->
      <Form
        @submit="onSubmit"
        :validation-schema="schema"
        v-slot="{ errors, isSubmitting }"
      >
        <div class="form-group">
          <label for="username">نام کاربری</label>
          <Field
            id="username"
            name="username"
            type="text"
            class="form-input"
            placeholder="نام کاربری خود را وارد کنید"
            :class="{ 'input-error': errors.username }"
            dir="auto"
          />
          <small v-if="errors.username" class="error-text">{{
            errors.username
          }}</small>
        </div>

        <div class="form-group">
          <label for="email">ایمیل</label>
          <Field
            id="email"
            name="email"
            type="email"
            class="form-input"
            placeholder="ایمیل خود را وارد کنید"
            :class="{ 'input-error': errors.email }"
            dir="auto"
          />
          <small v-if="errors.email" class="error-text">{{
            errors.email
          }}</small>
        </div>

        <div class="form-group">
          <label for="password">رمز عبور</label>
          <Field
            id="password"
            name="password"
            type="password"
            class="form-input"
            placeholder="رمز عبور خود را وارد کنید"
            :class="{ 'input-error': errors.password }"
            dir="auto"
          />
          <small v-if="errors.password" class="error-text">{{
            errors.password
          }}</small>
        </div>

        <button type="submit" class="btn-login" :disabled="isSubmitting">
          <span v-if="isSubmitting" class="spinner"></span>
          ثبت نام
        </button>

        <router-link to="/login" class="btn-login">ورود</router-link>

        <div v-if="errors.apiError" class="api-error">
          {{ errors.apiError }}
        </div>
      </Form>
    </div>
  </div>
</template>

<script setup>
import { Form, Field } from "vee-validate";
import * as Yup from "yup";
import { useAuthStore } from "@/stores";

const schema = Yup.object().shape({
  username: Yup.string().required("نام کاربری اجباری است"),
  password: Yup.string().required("رمز عبور اجباری است"),
  email: Yup.string()
    .email("فرمت ایمیل اشتباه است")
    .required("ایمیل الزامی است"),
});

const onSubmit = (values, { setErrors }) => {
  const authStore = useAuthStore();
  const { username, password, email } = values;

  return authStore
    .register(username, password, email)
    .catch((error) => setErrors({ apiError: error }));
};
</script>

<style scoped>
* {
  font-family: "Vazir", sans-serif;
  direction: rtl;
  box-sizing: border-box;
}

.login-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%);
  padding: 1rem;
}

.login-card {
  background: #ffffff;
  border-radius: 1rem;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  width: 100%;
  max-width: 400px;
  transition: transform 0.3s ease;
}
.login-card:hover {
  transform: translateY(-5px);
}

.login-header h1 {
  margin: 0.5rem 0;
  font-size: 2rem;
  color: #333;
  font-weight: 700;
}

.login-logo {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.login-demo-info {
  font-size: 0.85rem;
  color: #666;
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1.2rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #444;
}

.form-input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #ccc;
  border-radius: 0.75rem;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: #fafafa;
}

.form-input:focus {
  border-color: #4a90e2;
  background: #fff;
  box-shadow: 0 0 0 4px rgba(74, 144, 226, 0.1);
}

.input-error {
  border-color: #e74c3c !important;
}

.error-text {
  color: #e74c3c;
  font-size: 0.85rem;
  margin-top: 0.25rem;
}

.btn-register {
  width: 100%;
  padding: 0.9rem;
  background: linear-gradient(135deg, #4a90e2, #357abd);
  color: #fff;
  border: none;
  border-radius: 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.btn-register:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(74, 144, 226, 0.3);
}
.btn-register:disabled {
  background: #bdc3c7;
  cursor: not-allowed;
  box-shadow: none;
}

.btn-login {
  display: block;
  text-align: center;
  margin: 1rem auto 0;
  padding: 0.7rem;
  color: #4a90e2;
  border: 1px solid #4a90e2;
  border-radius: 0.75rem;
  text-decoration: none;
  font-weight: 600;
  transition: background 0.3s ease, color 0.3s ease;
}
.btn-login:hover {
  background: #4a90e2;
  color: #fff;
}

.api-error {
  margin-top: 1.5rem;
  padding: 1rem;
  background: #fdecea;
  color: #e74c3c;
  border: 1px solid #e74c3c;
  border-radius: 0.75rem;
  text-align: center;
}

@media (max-width: 480px) {
  .login-card {
    padding: 1.5rem;
  }
  .login-header h1 {
    font-size: 1.5rem;
  }
  .login-logo {
    font-size: 3rem;
  }
}
</style>
