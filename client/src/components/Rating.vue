<template>
  <h2
    v-if="rating >= 10"
    class="inline-block p-1 text-xs font-bold rounded-md"
    :class="rating >= 35?'bg-green-200 text-green-900':rating >= 25?'bg-yellow-300 text-yellow-900':'bg-red-200 text-red-900'"
  >{{ ratingFraction }}&nbsp;★</h2>
  <h2 v-else class="inline-block p-1 text-xs rounded-md bg-gray-300 text-gray-700">No Ratings</h2>
</template>

<script>
export default {
  name: "Rating",
  props: ["rating"],
  computed: {
    ratingFraction() {
      return (this.rating / 10).toFixed(1);
    },
  },
};
</script>