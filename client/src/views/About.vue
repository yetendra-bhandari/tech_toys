<template>
  <main class="container mx-auto p-4">
    <img
      class="mx-auto lg:ml-10 max-w-xs"
      src="@/assets/images/technology-banner.svg"
      alt="Welcome to Tech Toys"
    />
    <h1
      class="mt-6 font-title tracking-tighter leading-tight text-3xl text-center md:text-left"
    >What we do</h1>
    <div class="flex flex-wrap flex-col items-center md:items-start justify-between md:flex-row">
      <div class="mt-4 w-56">
        <svg class="mx-auto md:mx-0 h-10" viewBox="0 0 20 20">
          <path
            fill="currentColor"
            d="M10 20a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm7.75-8a8.01 8.01 0 0 0 0-4h-3.82a28.81 28.81 0 0 1 0 4h3.82zm-.82 2h-3.22a14.44 14.44 0 0 1-.95 3.51A8.03 8.03 0 0 0 16.93 14zm-8.85-2h3.84a24.61 24.61 0 0 0 0-4H8.08a24.61 24.61 0 0 0 0 4zm.25 2c.41 2.4 1.13 4 1.67 4s1.26-1.6 1.67-4H8.33zm-6.08-2h3.82a28.81 28.81 0 0 1 0-4H2.25a8.01 8.01 0 0 0 0 4zm.82 2a8.03 8.03 0 0 0 4.17 3.51c-.42-.96-.74-2.16-.95-3.51H3.07zm13.86-8a8.03 8.03 0 0 0-4.17-3.51c.42.96.74 2.16.95 3.51h3.22zm-8.6 0h3.34c-.41-2.4-1.13-4-1.67-4S8.74 3.6 8.33 6zM3.07 6h3.22c.2-1.35.53-2.55.95-3.51A8.03 8.03 0 0 0 3.07 6z"
          />
        </svg>
        <p
          class="mt-1 text-center md:text-left"
        >We work with our partners to make our products available in more than 3000 locations</p>
      </div>
      <div class="mt-4 w-56">
        <svg class="mx-auto md:mx-0 h-10" viewBox="0 0 20 20">
          <path
            fill="currentColor"
            d="M10 20a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm1-5h1a3 3 0 0 0 0-6H7.99a1 1 0 0 1 0-2H14V5h-3V3H9v2H8a3 3 0 1 0 0 6h4a1 1 0 1 1 0 2H6v2h3v2h2v-2z"
          />
        </svg>
        <p
          class="mt-1 text-center md:text-left"
        >Straightforward pricing that ensures you get our products at the cheapest price</p>
      </div>
      <div class="mt-4 w-56">
        <svg class="mx-auto md:mx-0 h-10" viewBox="0 0 20 20">
          <path
            fill="currentColor"
            d="M18 6V4H2v2h16zm0 4H2v6h16v-6zM0 4c0-1.1.9-2 2-2h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4zm4 8h4v2H4v-2z"
          />
        </svg>
        <p
          class="mt-1 text-center md:text-left"
        >Eliminating hassles and delays, TechToys makes payments easier than ever</p>
      </div>
      <div class="mt-4 w-56">
        <svg class="mx-auto md:mx-0 h-10" viewBox="0 0 20 20">
          <path
            fill="currentColor"
            d="M17 11v3l-3-3H8a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h10a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-1zm-3 2v2a2 2 0 0 1-2 2H6l-3 3v-3H2a2 2 0 0 1-2-2V8c0-1.1.9-2 2-2h2v3a4 4 0 0 0 4 4h6z"
          />
        </svg>
        <p
          class="mt-1 text-center md:text-left"
        >No matter when and where you need help, TechToys' support team is there for you</p>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "About",
};
</script>
