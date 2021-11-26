<template>
  <main class="container mx-auto p-4">
    <h1
      class="font-title tracking-tighter leading-tight text-3xl text-center"
    >Technologies Used In This Project</h1>
    <section class="flex flex-col items-center">
      <a class="mt-2" href="https://tailwindcss.com/" title="Tailwind CSS">
        <img class="h-24" src="@/assets/images/tailwind-css-logo.svg" alt="Tailwind CSS" />
      </a>
      <a href="https://ariadnegraphql.org/" title="Ariadne GraphQL">
        <img class="h-20" src="@/assets/images/ariadne-logo.png" alt="Ariadne GraphQL" />
      </a>
      <a class="mt-4" href="https://www.djangoproject.com/" title="Django">
        <img class="h-24" src="@/assets/images/django-logo.svg" alt="Django" />
      </a>
      <a class="mt-6" href="https://vuejs.org/" title="Vue.js">
        <img class="h-24" src="@/assets/images/vuejs-logo.svg" alt="Vue.js" />
      </a>
    </section>
  </main>
</template>

<script>
export default {
  name: "Support",
};
</script>
