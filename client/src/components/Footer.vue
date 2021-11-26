<template>
  <footer class="bg-color5 px-4 py-2 text-color1 flex justify-between flex-wrap">
    <router-link
      :to="{ name: 'Seller'}"
      class="flex items-center hover:underline focus:outline-none focus:underline"
    >
      <svg class="h-4" viewBox="0 0 20 20">
        <path
          fill="currentColor"
          d="M18 9.87V20H2V9.87a4.25 4.25 0 0 0 3-.38V14h10V9.5a4.26 4.26 0 0 0 3 .37zM3 0h4l-.67 6.03A3.43 3.43 0 0 1 3 9C1.34 9 .42 7.73.95 6.15L3 0zm5 0h4l.7 6.3c.17 1.5-.91 2.7-2.42 2.7h-.56A2.38 2.38 0 0 1 7.3 6.3L8 0zm5 0h4l2.05 6.15C19.58 7.73 18.65 9 17 9a3.42 3.42 0 0 1-3.33-2.97L13 0z"
        />
      </svg>
      <span class="ml-2 text-sm">Sell On TechToys</span>
    </router-link>
    <router-link
      :to="{ name: 'About'}"
      class="mx-1 flex items-center hover:underline focus:outline-none focus:underline"
    >
      <svg class="h-4 w-2" width="80" height="160" viewBox="0 0 21.166 42.333">
        <path
          fill="currentColor"
          transform="matrix(.26456 0 0 .26458 -39.682 -39.687)"
          d="m150 150v40h40v-40h-40zm40 40v40h40v-40h-40zm-40.002 39.996c-0.3934 33.546 22.039 67.213 54.781 76.667 8.1758 2.3884 16.72 3.3416 25.221 3.3366v-40c-13.269 0.975-26.91-5.6246-33.481-17.373-4.2253-6.7375-6.5523-14.672-6.5206-22.632-13.333 7e-5 -26.667 1.3e-4 -40 2e-4z"
        />
      </svg>
      <span class="ml-2 text-sm">About Us</span>
    </router-link>
    <router-link
      :to="{ name: 'Support'}"
      class="flex items-center hover:underline focus:outline-none focus:underline"
    >
      <svg class="h-4" viewBox="0 0 20 20">
        <path
          fill="currentColor"
          d="M10 20a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm2-13c0 .28-.21.8-.42 1L10 9.58c-.57.58-1 1.6-1 2.42v1h2v-1c0-.29.21-.8.42-1L13 9.42c.57-.58 1-1.6 1-2.42a4 4 0 1 0-8 0h2a2 2 0 1 1 4 0zm-3 8v2h2v-2H9z"
        />
      </svg>
      <span class="ml-2 text-sm">Help &amp; Support</span>
    </router-link>
  </footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>