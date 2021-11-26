<template>
  <main v-if="product && getProductReviews" class="container mx-auto p-4">
    <div class="flex flex-col md:flex-row md:justify-center">
      <div class="flex flex-col items-center md:items-end">
        <picture>
          <img
            v-if="product.image"
            class="w-64 h-64 rounded-md object-contain shadow-md lg:w-80 lg:h-80 xl:w-96 xl:h-96"
            :src="serverURL + product.image.substring(1)"
            :alt="product.name"
          />
          <svg
            v-else
            class="w-64 h-64 p-12 rounded-md shadow-md lg:w-80 lg:h-80 xl:w-96 xl:h-96"
            viewBox="0 0 20 20"
          >
            <path
              fill="currentColor"
              d="M17 6V5h-2V2H3v14h5v4h3.25H11a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6zm-5.75 14H3a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h12a2 2 0 0 1 2 2v4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-5.75zM11 8v8h6V8h-6zm3 11a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"
            />
          </svg>
        </picture>
        <button
          class="mt-2 px-1.5 py-0.5 rounded-md flex items-center focus:outline-none"
          title="Change Product Stock"
          :class="product.inStock?'bg-green-500 text-white hover:bg-green-400 focus:bg-green-400':'bg-red-200 text-red-700 hover:text-red-600 focus:text-red-600'"
          @click="changeProductStock"
        >
          <span v-if="product.inStock">In Stock</span>
          <span v-else>Out Of Stock</span>
          <svg class="ml-1.5 h-4 w-4" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="M18 9.87V20H2V9.87a4.25 4.25 0 0 0 3-.38V14h10V9.5a4.26 4.26 0 0 0 3 .37zM3 0h4l-.67 6.03A3.43 3.43 0 0 1 3 9C1.34 9 .42 7.73.95 6.15L3 0zm5 0h4l.7 6.3c.17 1.5-.91 2.7-2.42 2.7h-.56A2.38 2.38 0 0 1 7.3 6.3L8 0zm5 0h4l2.05 6.15C19.58 7.73 18.65 9 17 9a3.42 3.42 0 0 1-3.33-2.97L13 0z"
            />
          </svg>
        </button>
      </div>
      <section class="mt-4 leading-snug md:mt-0 md:ml-6 md:max-w-1/2">
        <h1 class="text-1.5xl leading-tight">{{ product.name }}</h1>
        <h2 class="font-title font-bold text-sm text-color7">{{ categoryName }}</h2>
        <div class="mt-2 flex items-center">
          <Rating :rating="product.rating" />
          <h2 class="ml-1.5 text-xs text-color7">
            <span v-if="getProductReviews.length">
              {{ getProductReviews.length.toLocaleString() }}
              <span
                v-if="getProductReviews.length === 1"
              >Review</span>
              <span v-else>Reviews</span>
            </span>
            <span v-else>No Reviews Yet</span>
          </h2>
        </div>
        <div class="mt-4 flex items-center font-title">
          <h1
            class="text-3xl font-bold"
          >${{ Math.floor(product.mrp * (100 - product.discount) / 100 ).toLocaleString() }}</h1>
          <h2 v-if="product.discount" class="ml-2 line-through text-color7">${{ product.mrp }}</h2>
          <h2
            v-if="product.discount && !discountInput"
            class="ml-2 font-bold text-green-600 text-sm"
          >{{ product.discount }}% Off</h2>
          <button
            v-if="!discountInput"
            class="p-2 hover:text-color4 focus:outline-none focus:text-color4"
            title="Edit Discount"
            @click="discountInput=true"
          >
            <svg class="w-3 h-3" viewBox="0 0 20 20">
              <path
                fill="currentColor"
                d="M12.3 3.7l4 4L4 20H0v-4L12.3 3.7zm1.4-1.4L16 0l4 4-2.3 2.3-4-4z"
              />
            </svg>
          </button>
          <form
            ref="discountForm"
            v-if="discountInput"
            class="ml-2 text-sm"
            @submit.prevent="editProductDiscount"
          >
            <input
              class="border-b-2 focus:outline-none focus:border-color5 px-1 py-0.5 w-10 font-bold"
              type="number"
              v-model.number="newDiscount"
              min="0"
              max="99"
              required
            />%
            <button
              type="submit"
              class="ml-1 p-1 bg-green-500 rounded-full hover:shadow-md focus:outline-none"
              title="Confirm Discount"
            >
              <svg class="w-3 h-3 text-white" viewBox="0 0 20 20">
                <path fill="currentColor" d="M0 11l2-2 5 5L18 3l2 2L7 18z" />
              </svg>
            </button>
          </form>
        </div>
        <h1 class="mt-6 text-xl font-bold font-title">Product Details</h1>
        <p class="mt-2 text-sm whitespace-pre-wrap">{{ product.description }}</p>
        <h1 class="mt-6 text-xl font-bold font-title">Specifications</h1>
        <p class="mt-2 text-sm whitespace-pre-wrap">{{ product.specifications }}</p>
      </section>
    </div>
    <h1 class="mt-4 mb-2 text-xl font-bold font-title">Product Reviews</h1>
    <section v-if="getProductReviews.length" class="grid gap-6">
      <Review
        v-on:refresh-reviews="refreshReviews"
        v-for="review in getProductReviews"
        :key="review.id"
        :review="review"
      />
    </section>
    <h2 v-else>No Reviews Yet</h2>
  </main>
</template>

<script>
import helper from "@/helper";
import gql from "graphql-tag";
import Rating from "@/components/Rating.vue";
import Review from "@/components/Review.vue";
export default {
  name: "SellerProduct",
  components: { Rating, Review },
  mixins: [helper],
  data() {
    return {
      product: null,
      discountInput: false,
      newDiscount: 0,
    };
  },
  computed: {
    categoryName() {
      const categories = {
        EARP: "Earphones",
        HEAD: "Headphones",
        LAPT: "Laptops",
        VIRT: "VR Headsets",
      };
      return categories[this.product.category];
    },
  },
  methods: {
    refreshReviews(reviewRating) {
      this.product.rating = reviewRating;
      this.$apollo.queries.getProductReviews.refetch();
    },
    changeProductStock() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation ChangeProductStock($productID: ID, $inStock: Boolean) {
              editProductStock(productID: $productID, inStock: $inStock) {
                inStock
              }
            }
          `,
          variables: {
            productID: this.product.id,
            inStock: !this.product.inStock,
          },
        })
        .then((data) => {
          const response = data.data.editProductStock;
          if (response !== null) {
            this.product.inStock = response.inStock;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    editProductDiscount() {
      if (this.newDiscount >= 0 && this.newDiscount < 100) {
        this.$apollo
          .mutate({
            mutation: gql`
              mutation EditProductDiscount($productID: ID, $discount: Int) {
                editProductDiscount(
                  productID: $productID
                  discount: $discount
                ) {
                  discount
                }
              }
            `,
            variables: {
              productID: this.product.id,
              discount: this.newDiscount,
            },
          })
          .then((data) => {
            const response = data.data.editProductDiscount;
            if (response !== null) {
              this.product.discount = response.discount;
              this.discountInput = false;
            }
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
  beforeCreate() {
    if (this.$store.getters.getUserData.userType !== "SELL") {
      this.$router.push({ name: "Home" });
    }
  },
  created() {
    this.$apollo
      .query({
        query: gql`
          query GetSellerProductById($productID: ID) {
            getProductById(productID: $productID) {
              id
              seller {
                id
              }
              image
              name
              description
              specifications
              mrp
              discount
              category
              inStock
              rating
            }
          }
        `,
        variables: {
          productID: this.$route.params.productID,
        },
      })
      .then((data) => {
        const response = data.data.getProductById;
        if (
          response !== null &&
          response.seller.id == this.$store.getters.getUserData.seller.id
        ) {
          this.product = response;
          this.newDiscount = response.discount;
        } else {
          this.$router.push({ name: "Home" });
        }
      })
      .catch((error) => {
        console.error(error);
      });
  },
  apollo: {
    getProductReviews: {
      query: gql`
        query GetSellerProductReviews($productID: ID!) {
          getProductReviews(productID: $productID) {
            id
            customer {
              id
              account {
                id
                image
                name
              }
            }
            rating
            message
            date
          }
        }
      `,
      variables() {
        return {
          productID: this.$route.params.productID,
        };
      },
    },
  },
};
</script>