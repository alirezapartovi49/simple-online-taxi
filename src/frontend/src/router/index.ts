import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import RideTrackingView from "../views/RideTrackingView.vue";
import ProfileView from "../views/ProfileView.vue";
import RideHistoryView from "../views/RideHistoryView.vue";
import SupportView from "../views/SupportView.vue";
import NotFoundComponent from "@/components/NotFoundComponent.vue";
import { useAuthStore } from "@/stores";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: { requiresAuth: true },
  },
  {
    path: "/ride-tracking",
    name: "ride-tracking",
    component: RideTrackingView,
    meta: { requiresAuth: true },
  },
  {
    path: "/rides",
    name: "rides",
    component: RideHistoryView,
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: "/support",
    name: "support",
    component: SupportView,
    meta: { requiresAuth: true },
  },
  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/:catchAll(.*)*",
    component: NotFoundComponent,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const user = authStore.user;
  let isAuthenticated = false;
  if (user != null && user.status == 200) {
    isAuthenticated = true;
  }

  if (to.meta.requiresAuth && !isAuthenticated) {
    next("/login");
  } else {
    next();
  }
});

export default router;
