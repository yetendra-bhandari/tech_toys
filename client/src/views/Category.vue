<template>
  <main v-if="getProductsByCategory" class="container mx-auto p-4">
    <section class="p-4 bg-color3 rounded-lg">
      <h1 class="text-2xl leading-tight" v-text="categoryName"></h1>
      <div
        v-if="getProductsByCategory.length"
        class="mt-2 grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5"
      >
        <router-link
          v-for="product in getProductsByCategory"
          :key="product.id"
          :to="{ name: 'CustomerProduct', params: { productID: product.id }}"
          class="relative flex flex-col bg-color1 rounded-xl cursor-default hover:shadow-md focus:shadow-md focus:outline-none"
          title="View Product"
        >
          <h2
            class="absolute top-0 right-0 mt-1 mr-2 text-xs text-gray-600"
          >{{ product.discount }}% Off</h2>
          <picture>
            <img
              class="h-40 w-full object-contain"
              v-if="product.image"
              :src="serverURL + product.image.substring(1)"
              :alt="product.name"
            />
            <svg v-else class="mx-auto h-40 p-8" viewBox="0 0 20 20">
              <path
                fill="currentColor"
                d="M17 6V5h-2V2H3v14h5v4h3.25H11a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6zm-5.75 14H3a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h12a2 2 0 0 1 2 2v4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-5.75zM11 8v8h6V8h-6zm3 11a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"
              />
            </svg>
          </picture>
          <div class="flex flex-col items-center p-2 truncate">
            <h2 class="leading-tighter max-w-full truncate">{{ product.name }}</h2>
            <h2 class="mb-1">
              <span
                class="font-bold text-sm"
              >${{ Math.floor(product.mrp * (100 - product.discount) / 100 ).toLocaleString() }}</span>
              <span
                v-if="product.discount > 0"
                class="ml-1 text-xs line-through text-gray-600"
              >${{ product.mrp.toLocaleString() }}</span>
            </h2>
            <div class="w-full flex justify-between">
              <Rating :rating="product.rating" />
              <span
                class="text-xs p-1 rounded-md"
                :class="product.inStock?'bg-green-500 text-white':'bg-red-200 text-red-700'"
              >In Stock</span>
            </div>
          </div>
        </router-link>
      </div>
      <h2 v-else class="mt-2">There are no products available right now!</h2>
    </section>
  </main>
</template>

<script>
import Rating from "@/components/Rating.vue";
import helper from "@/helper";
import gql from "graphql-tag";
export default {
  name: "Category",
  components: { Rating },
  mixins: [helper],
  computed: {
    categoryName() {
      const category = {
        laptops: "Laptops",
        earphones: "Earphones",
        headphones: "Headphones",
        "vr-headsets": "VR Headsets",
      };
      return category[this.$route.params.categoryName];
    },
  },
  beforeCreate() {
    const category = {
      laptops: "LAPT",
      earphones: "EARP",
      headphones: "HEAD",
      "vr-headsets": "VIRT",
    };
    if (
      this.$store.getters.getUserData.userType === "SELL" ||
      !(this.$route.params.categoryName in category)
    ) {
      this.$router.push({ name: "Home" });
    }
  },
  apollo: {
    getProductsByCategory: {
      query: gql`
        query GetProductsByCategory($category: String!) {
          getProductsByCategory(category: $category) {
            id
            seller {
              id
              account {
                id
                name
              }
            }
            image
            name
            mrp
            discount
            inStock
            rating
          }
        }
      `,
      variables() {
        const category = {
          laptops: "LAPT",
          earphones: "EARP",
          headphones: "HEAD",
          "vr-headsets": "VIRT",
        };
        return {
          category: category[this.$route.params.categoryName],
        };
      },
    },
  },
};
</script>
