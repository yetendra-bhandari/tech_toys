<template>
  <main class="container mx-auto p-4">
    <img
      class="mx-auto w-full max-w-xl py-8"
      src="@/assets/images/tech-toys-banner.svg"
      alt="Welcome to Tech Toys"
    />
    <h2 class="pb-2 font-title tracking-tight text-2xl md:text-3xl text-center border-b-2">Explore</h2>
    <div class="mt-4 mx-auto max-w-2xs md:max-w-lg grid grid-cols-1 md:grid-cols-2 gap-6">
      <router-link
        :to="{ name: 'Category', params: { categoryName: 'laptops' }}"
        class="border-2 border-solid rounded-md shadow-lg overflow-hidden hover:bg-color3"
      >
        <img src="@/assets/images/laptop.png" alt="Laptops" />
        <div class="mx-2 border-t-2 px-1 py-2">
          <h3 class="font-title font-bold text-xl">Laptops</h3>
          <h4 class="text-sm text-color7 truncate">For business, gaming and more</h4>
        </div>
      </router-link>
      <router-link
        :to="{ name: 'Category', params: { categoryName: 'earphones' }}"
        class="border-2 border-solid rounded-md shadow-lg overflow-hidden hover:bg-color3"
      >
        <img src="@/assets/images/earphones.png" alt="Earphones" />
        <div class="mx-2 border-t-2 px-1 py-2">
          <h3 class="font-title font-bold text-xl">Earphones</h3>
          <h4 class="text-sm text-color7 truncate">Wired or go wire-free</h4>
        </div>
      </router-link>
      <router-link
        :to="{ name: 'Category', params: { categoryName: 'headphones' }}"
        class="border-2 border-solid rounded-md shadow-lg overflow-hidden hover:bg-color3"
      >
        <img src="@/assets/images/headphones.png" alt="Headphones" />
        <div class="mx-2 border-t-2 px-1 py-2">
          <h3 class="font-title font-bold text-xl">Headphones</h3>
          <h4 class="text-sm text-color7 truncate">For professionals and audiophiles</h4>
        </div>
      </router-link>
      <router-link
        :to="{ name: 'Category', params: { categoryName: 'vr-headsets' }}"
        class="border-2 border-solid rounded-md shadow-lg overflow-hidden hover:bg-color3"
      >
        <img src="@/assets/images/vr-headset.png" alt="VR Headsets" />
        <div class="mx-2 border-t-2 px-1 py-2">
          <h3 class="font-title font-bold text-xl">VR Headsets</h3>
          <h4 class="text-sm text-color7 truncate">Turn the world into your arcade</h4>
        </div>
      </router-link>
    </div>
  </main>
</template>

<script>
export default {
  name: "Home",
  beforeCreate() {
    if (this.$store.getters.getUserData.userType === "SELL") {
      this.$router.push({ name: "Seller" }).catch(() => {});
    }
  },
};
</script>
