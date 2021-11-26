<template>
  <header>
    <nav class="relative z-10 bg-color1 px-3 py-2">
      <div class="px-2 flex flex-wrap items-center justify-between">
        <router-link
          :to="isSeller?{ name: 'Seller' } : { name: 'Home' }"
          title="TechToys"
          class="flex items-center focus:outline-none focus:text-color4"
        >
          <img class="h-8" src="@/assets/images/tech-toys-logo.svg" alt="Tech Toys" />
          <span class="ml-3 font-title font-bold text-lg">TechToys</span>
        </router-link>
        <div v-if="!isSeller" class="hidden lg:flex items-center">
          <router-link
            :to="{ name: 'Category', params: { categoryName: 'laptops' }}"
            class="px-2 py-1 rounded-md text-color5 text-sm hover:bg-color3 focus:outline-none focus:bg-color3"
          >Laptops</router-link>
          <router-link
            :to="{ name: 'Category', params: { categoryName: 'earphones' }}"
            class="px-2 py-1 ml-1 rounded-md text-color5 text-sm hover:bg-color3 focus:outline-none focus:bg-color3"
          >Earphones</router-link>
          <router-link
            :to="{ name: 'Category', params: { categoryName: 'headphones' }}"
            class="px-2 py-1 ml-1 rounded-md text-color5 text-sm hover:bg-color3 focus:outline-none focus:bg-color3"
          >Headphones</router-link>
          <router-link
            :to="{ name: 'Category', params: { categoryName: 'vr-headsets' }}"
            class="px-2 py-1 ml-1 rounded-md text-color5 text-sm hover:bg-color3 focus:outline-none focus:bg-color3"
          >VR Headsets</router-link>
        </div>
        <div class="flex items-center">
          <div v-if="isLoggedIn" class="flex">
            <router-link
              :to="{ name: 'CustomerCart'}"
              v-if="isCustomer"
              class="px-1 flex items-center hover:underline focus:outline-none focus:underline focus:text-color4"
              title="View Cart"
            >
              <svg class="h-5 w-5" viewBox="0 0 20 20">
                <path
                  fill="currentColor"
                  d="M4 2h16l-3 9H4a1 1 0 1 0 0 2h13v2H4a3 3 0 0 1 0-6h.33L3 5 2 2H0V0h3a1 1 0 0 1 1 1v1zm1 18a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm10 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"
                />
              </svg>
              <span class="hidden sm:block ml-1">Cart</span>
            </router-link>
            <router-link
              :to="{ name: 'CustomerOrders'}"
              v-if="isCustomer"
              class="mx-1 px-1 flex items-center hover:underline focus:outline-none focus:underline focus:text-color4"
              title="View Orders"
            >
              <svg class="h-5 w-5" viewBox="0 0 20 20">
                <path
                  fill="currentColor"
                  d="M16 6v2h2l2 12H0L2 8h2V6a6 6 0 1 1 12 0zm-2 0a4 4 0 1 0-8 0v2h8V6zM4 10v2h2v-2H4zm10 0v2h2v-2h-2z"
                />
              </svg>
              <span class="hidden sm:block ml-1">Orders</span>
            </router-link>
            <button
              class="px-1 flex items-center hover:underline focus:outline-none focus:underline focus:text-color4"
              title="Logout"
              @click="logoutUser"
            >
              <svg class="h-5 w-5" viewBox="0 0 471.2 471.2">
                <path
                  fill="currentColor"
                  d="M227.619,444.2h-122.9c-33.4,0-60.5-27.2-60.5-60.5V87.5c0-33.4,27.2-60.5,60.5-60.5h124.9c7.5,0,13.5-6,13.5-13.5
			s-6-13.5-13.5-13.5h-124.9c-48.3,0-87.5,39.3-87.5,87.5v296.2c0,48.3,39.3,87.5,87.5,87.5h122.9c7.5,0,13.5-6,13.5-13.5
			S235.019,444.2,227.619,444.2z M450.019,226.1l-85.8-85.8c-5.3-5.3-13.8-5.3-19.1,0c-5.3,5.3-5.3,13.8,0,19.1l62.8,62.8h-273.9c-7.5,0-13.5,6-13.5,13.5
			s6,13.5,13.5,13.5h273.9l-62.8,62.8c-5.3,5.3-5.3,13.8,0,19.1c2.6,2.6,6.1,4,9.5,4s6.9-1.3,9.5-4l85.8-85.8
			C455.319,239.9,455.319,231.3,450.019,226.1z"
                />
              </svg>
              <span class="hidden sm:block ml-1">Logout</span>
            </button>
            <router-link
              :to="{ name: 'Account'}"
              class="ml-2 h-8 w-8 rounded-full overflow-hidden border bg-cover hover:border-color5 focus:border-color5 focus:outline-none"
              :style="accountImageURL? { backgroundImage: 'url(' + accountImageURL + ')' } : {}"
              :title="accountName"
            >
              <svg v-if="!accountImageURL" class="pt-0.5" viewBox="0 0 20 20">
                <path
                  fill="currentColor"
                  d="M5 5a5 5 0 0 1 10 0v2A5 5 0 0 1 5 7V5zM0 16.68A19.9 19.9 0 0 1 10 14c3.64 0 7.06.97 10 2.68V20H0v-3.32z"
                />
              </svg>
            </router-link>
          </div>
          <router-link
            v-else
            :to="{ name: 'Login'}"
            class="px-1.5 py-0.5 border-2 border-color5 rounded-sm text-sm hover:bg-color5 hover:text-color1 focus:outline-none focus:bg-color4 focus:border-color4 focus:text-color1"
          >Log In Or Sign Up</router-link>
          <button
            v-if="!isSeller"
            class="lg:hidden ml-3 p-1 h-6 w-6 text-color5 focus:outline-none focus:text-color6"
            @click="menuOpen=!menuOpen"
          >
            <svg v-show="!menuOpen" viewBox="0 0 20 20">
              <path fill="currentColor" d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
            </svg>
            <svg v-show="menuOpen" viewBox="0 0 20 20">
              <path
                fill="currentColor"
                d="M10 8.586L2.929 1.515 1.515 2.929 8.586 10l-7.071 7.071 1.414 1.414L10 11.414l7.071 7.071 1.414-1.414L11.414 10l7.071-7.071-1.414-1.414L10 8.586z"
              />
            </svg>
          </button>
        </div>
      </div>
      <div
        v-if="!isSeller"
        v-show="menuOpen"
        class="mt-2 p-2 flex flex-col shadow-md rounded-lg lg:hidden"
      >
        <router-link
          :to="{ name: 'Category', params: { categoryName: 'laptops' }}"
          @click.native="menuOpen=false"
          class="p-2 rounded-md text-color5 hover:bg-color4 hover:text-color1 focus:outline-none focus:bg-color4 focus:text-color1"
        >Laptops</router-link>
        <router-link
          :to="{ name: 'Category', params: { categoryName: 'earphones' }}"
          @click.native="menuOpen=false"
          class="mt-1 p-2 rounded-md text-color5 hover:bg-color4 hover:text-color1 focus:outline-none focus:bg-color4 focus:text-color1"
        >Earphones</router-link>
        <router-link
          :to="{ name: 'Category', params: { categoryName: 'headphones' }}"
          @click.native="menuOpen=false"
          class="mt-1 p-2 rounded-md text-color5 hover:bg-color4 hover:text-color1 focus:outline-none focus:bg-color4 focus:text-color1"
        >Headphones</router-link>
        <router-link
          :to="{ name: 'Category', params: { categoryName: 'vr-headsets' }}"
          @click.native="menuOpen=false"
          class="mt-1 p-2 rounded-md text-color5 hover:bg-color4 hover:text-color1 focus:outline-none focus:bg-color4 focus:text-color1"
        >VR Headsets</router-link>
      </div>
    </nav>
    <button
      v-show="menuOpen"
      class="lg:hidden inset-0 fixed w-full h-full focus:outline-none cursor-default"
      @click="menuOpen=false"
    ></button>
  </header>
</template>

<script>
import helper from "@/helper";
export default {
  name: "Navigation",
  mixins: [helper],
  data() {
    return {
      menuOpen: false,
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.getUserData.isLoggedIn;
    },
    isCustomer() {
      return this.$store.getters.getUserData.userType === "CUST";
    },
    isSeller() {
      return this.$store.getters.getUserData.userType === "SELL";
    },
    accountName() {
      return this.$store.getters.getUserData.account.name;
    },
    accountImageURL() {
      return this.$store.getters.getUserData.account.image
        ? this.serverURL + this.$store.getters.getUserData.account.image.substring(1)
        : null;
    },
  },
  methods: {
    logoutUser() {
      this.$store.dispatch("resetUserData");
      this.$router.push({ name: "Home" }).catch(() => {});
    },
  },
};
</script>