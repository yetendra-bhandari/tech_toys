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
        <div class="mt-2 grid gap-1 grid-cols-2 w-64 lg:w-80 xl:w-96">
          <button
            class="p-2 bg-orange-600 rounded-sm flex items-center justify-center hover:bg-orange-500 focus:outline-none focus:bg-orange-500 text-white"
            title="Add To Cart"
            @click="addCustomerCartItem"
          >
            <svg class="h-4 inline-block mr-1" viewBox="0 0 20 20">
              <path
                fill="currentColor"
                d="M4 2h16l-3 9H4a1 1 0 1 0 0 2h13v2H4a3 3 0 0 1 0-6h.33L3 5 2 2H0V0h3a1 1 0 0 1 1 1v1zm1 18a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm10 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"
              />
            </svg>
            <span>Add To Cart</span>
          </button>
          <select
            v-model.number="quantity"
            class="rounded-sm border px-1 bg-color3 focus:outline-none focus:shadow-md"
          >
            <option v-for="number in 10" :key="number" :value="number">
              {{ number }}
              <span v-if="number == 1">Piece</span>
              <span v-else>Pieces</span>
            </option>
          </select>
          <div
            v-if="cartConfirm"
            class="fixed inset-0 z-10 bg-black bg-opacity-50 flex items-center justify-center"
          >
            <section class="bg-color1 p-2 rounded-md flex flex-col">
              <h1 class="text-lg">{{ product.name }} × {{ quantity }}</h1>
              <h2 class="mt-1">Added To Cart</h2>
              <h2 class="mt-1">
                Total :
                <span class="font-title font-bold text-lg">${{ discountPrice }}</span>
              </h2>
              <button
                class="mt-2 px-2 py-1 rounded-sm bg-red-200 text-red-700 hover:text-red-600 focus:text-red-600 focus:outline-none"
                @click="deleteCustomerCartItem"
              >Remove From Cart</button>
              <button
                class="mt-1 px-2 py-1 rounded-sm bg-green-500 text-white hover:bg-green-400 focus:bg-green-400 focus:outline-none"
                @click="cartConfirm=false"
              >Continue Shopping</button>
            </section>
          </div>
        </div>
        <span
          class="mt-2 px-1.5 py-0.5 rounded-md flex items-center focus:outline-none"
          :class="product.inStock?'bg-green-500 text-white ':'bg-red-200 text-red-700'"
        >
          <span v-if="product.inStock">In Stock</span>
          <span v-else>Out Of Stock</span>
          <svg class="ml-1.5 h-4 w-4" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="M18 9.87V20H2V9.87a4.25 4.25 0 0 0 3-.38V14h10V9.5a4.26 4.26 0 0 0 3 .37zM3 0h4l-.67 6.03A3.43 3.43 0 0 1 3 9C1.34 9 .42 7.73.95 6.15L3 0zm5 0h4l.7 6.3c.17 1.5-.91 2.7-2.42 2.7h-.56A2.38 2.38 0 0 1 7.3 6.3L8 0zm5 0h4l2.05 6.15C19.58 7.73 18.65 9 17 9a3.42 3.42 0 0 1-3.33-2.97L13 0z"
            />
          </svg>
        </span>
      </div>
      <section class="mt-4 leading-snug md:mt-0 md:ml-6 md:max-w-1/2">
        <h1 class="text-1.5xl leading-tight">{{ product.name }}</h1>
        <router-link
          :to="{ name: 'Category', params: { categoryName: categoryLink }}"
          class="font-title font-bold text-sm text-color7 hover:underline focus:outline-none focus:underline"
        >{{ categoryName }}</router-link>
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
          <h1 class="text-3xl font-bold">${{ discountPrice }}</h1>
          <h2
            v-if="product.discount"
            class="ml-2 line-through text-color7"
          >${{ (product.mrp * quantity).toLocaleString() }}</h2>
          <h2
            v-if="product.discount"
            class="ml-2 font-bold text-green-600 text-sm"
          >{{ product.discount }}% Off</h2>
        </div>
        <h1 class="mt-6 text-xl font-bold font-title">Product Details</h1>
        <p class="mt-2 text-sm whitespace-pre-wrap">{{ product.description }}</p>
        <h1 class="mt-6 text-xl font-bold font-title">Specifications</h1>
        <p class="mt-2 text-sm whitespace-pre-wrap">{{ product.specifications }}</p>
      </section>
    </div>
    <h1 class="mt-4 text-xl font-bold font-title">Product Reviews</h1>
    <form class="mt-2" @submit.prevent="addProductReview">
      <textarea
        class="mt-2 block w-full h-32 py-1 border-b-2 text-sm focus:outline-none focus:border-color5"
        placeholder="Write A Review (Optional)"
        v-model="reviewMessage"
      ></textarea>
      <div class="mt-2 w-64 grid grid-cols-2 gap-2">
        <select
          class="border bg-color3 px-1 rounded-md focus:outline-none focus:shadow-md"
          v-model.number="reviewRating"
          required
        >
          <option selected disabled value>Rating</option>
          <option value="10">1★ (Terrible)</option>
          <option value="20">2★ (Poor)</option>
          <option value="30">3★ (Average)</option>
          <option value="40">4★ (Good)</option>
          <option value="50">5★ (Excellent)</option>
        </select>
        <input
          class="rounded-md px-2 py-1 cursor-pointer text-white bg-color5 hover:bg-color4 focus:outline-none focus:bg-color4"
          type="submit"
          value="Add Review"
        />
      </div>
    </form>
    <section v-if="getProductReviews.length" class="mt-4 grid gap-6">
      <Review
        v-on:refresh-reviews="refreshReviews"
        v-for="review in getProductReviews"
        :key="review.id"
        :review="review"
      />
    </section>
    <h2 v-else class="mt-4">No Reviews Yet</h2>
  </main>
</template>

<script>
import helper from "@/helper";
import gql from "graphql-tag";
import Rating from "@/components/Rating.vue";
import Review from "@/components/Review.vue";
export default {
  name: "CustomerProduct",
  components: { Rating, Review },
  mixins: [helper],
  data() {
    return {
      product: null,
      quantity: 1,
      cartConfirm: false,
      cartItemID: null,
      reviewRating: "",
      reviewMessage: "",
    };
  },
  computed: {
    discountPrice() {
      return (
        Math.floor((this.product.mrp * (100 - this.product.discount)) / 100) *
        this.quantity
      ).toLocaleString();
    },
    categoryName() {
      const categories = {
        EARP: "Earphones",
        HEAD: "Headphones",
        LAPT: "Laptops",
        VIRT: "VR Headsets",
      };
      return categories[this.product.category];
    },
    categoryLink() {
      const categories = {
        EARP: "earphones",
        HEAD: "headphones",
        LAPT: "laptops",
        VIRT: "vr-headsets",
      };
      return categories[this.product.category];
    },
  },
  methods: {
    refreshReviews(reviewRating) {
      this.product.rating = reviewRating;
      this.$apollo.queries.getProductReviews.refetch();
    },
    addCustomerCartItem() {
      if (this.$store.getters.getUserData.userType === "CUST") {
        this.$apollo
          .mutate({
            mutation: gql`
              mutation AddCustomerCartItem($productID: ID, $quantity: Int) {
                addCustomerCartItem(
                  productID: $productID
                  quantity: $quantity
                ) {
                  id
                }
              }
            `,
            variables: {
              productID: this.product.id,
              quantity: this.quantity,
            },
          })
          .then((data) => {
            const response = data.data.addCustomerCartItem;
            if (response !== null) {
              this.cartItemID = response.id;
              this.cartConfirm = true;
            }
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        this.$router.push({ name: "Login" });
      }
    },
    deleteCustomerCartItem() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation DeleteCustomerCartItem($cartItemID: ID) {
              deleteCustomerCartItem(cartItemID: $cartItemID)
            }
          `,
          variables: {
            cartItemID: this.cartItemID,
          },
        })
        .then((data) => {
          this.cartConfirm = false;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addProductReview() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation AddProductReview(
              $productID: ID
              $reviewInput: ReviewInput
            ) {
              addProductReview(productID: $productID, reviewInput: $reviewInput)
            }
          `,
          variables: {
            productID: this.product.id,
            reviewInput: {
              rating: this.reviewRating,
              message: this.reviewMessage,
            },
          },
        })
        .then((data) => {
          const response = data.data.addProductReview;
          if (response !== null) {
            this.product.rating = response;
            this.reviewMessage = "";
            this.reviewRating = "";
            this.$apollo.queries.getProductReviews.refetch();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  beforeCreate() {
    if (this.$store.getters.getUserData.userType === "SELL") {
      this.$router.push({ name: "Home" });
    }
  },
  created() {
    this.$apollo
      .query({
        query: gql`
          query GetCustomerProductById($productID: ID) {
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
        if (response !== null) {
          this.product = response;
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
        query GetCustomerProductReviews($productID: ID!) {
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