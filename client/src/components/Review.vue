<template>
  <div>
    <div class="mb-2 flex items-center">
      <picture
        :to="{ name: 'Account'}"
        class="h-6 w-6 rounded-full overflow-hidden border bg-cover"
        :style="review.customer.account.image? { backgroundImage: 'url(' + serverURL + review.customer.account.image + ')' } : {}"
        :title="review.customer.account.name"
      >
        <svg v-if="!review.customer.account.image" class="pt-0.5" viewBox="0 0 20 20">
          <path
            fill="currentColor"
            d="M5 5a5 5 0 0 1 10 0v2A5 5 0 0 1 5 7V5zM0 16.68A19.9 19.9 0 0 1 10 14c3.64 0 7.06.97 10 2.68V20H0v-3.32z"
          />
        </svg>
      </picture>
      <h2 class="ml-1 text-xs" v-text="isCurrentCustomer?'You':review.customer.account.name"></h2>
    </div>
    <p
      v-if="review.message.length > 0"
      class="mt-1 text-sm whitespace-pre-wrap"
      v-text="review.message"
    ></p>
    <div class="mt-1 flex items-center">
      <Rating :rating="review.rating" />
      <span class="ml-1.5 text-xs" v-text="timeDifference"></span>
      <button
        v-if="isCurrentCustomer"
        class="ml-1 p-1 text-red-700 hover:text-red-600 focus:text-red-600 focus:outline-none"
        title="Delete Review"
        @click="deleteProductReview(review.id)"
      >
        <svg class="h-4 w-4" viewBox="0 0 20 20">
          <path
            fill="currentColor"
            d="M6 2l2-2h4l2 2h4v2H2V2h4zM3 6h14l-1 14H4L3 6zm5 2v10h1V8H8zm3 0v10h1V8h-1z"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import gql from "graphql-tag";
import moment from "moment";
import helper from "@/helper";
import Rating from "@/components/Rating.vue";
export default {
  name: "Review",
  mixins: [helper],
  components: { Rating },
  props: ["review"],
  computed: {
    isCurrentCustomer() {
      return (
        this.$store.getters.getUserData.userType === "CUST" &&
        this.$store.getters.getUserData.customer.id === this.review.customer.id
      );
    },
    timeDifference() {
      return moment(this.review.date).fromNow();
    },
  },
  methods: {
    deleteProductReview(reviewID) {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation DeleteProductReview($reviewID: ID) {
              deleteProductReview(reviewID: $reviewID)
            }
          `,
          variables: {
            reviewID: reviewID,
          },
        })
        .then((data) => {
          this.$emit("refresh-reviews", data.data.deleteProductReview);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>