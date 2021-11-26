<template>
  <main v-if="account" class="container mx-auto p-4 flex flex-col items-center">
    <picture>
      <img
        v-if="account.image"
        class="mx-auto h-48 w-48 rounded-full object-cover"
        :src="serverURL + account.image.substring(1)"
        :alt="account.name"
      />
      <svg v-else class="mx-auto pt-2 h-48 w-48 rounded-full border-2" viewBox="0 0 20 20">
        <path
          fill="currentColor"
          d="M5 5a5 5 0 0 1 10 0v2A5 5 0 0 1 5 7V5zM0 16.68A19.9 19.9 0 0 1 10 14c3.64 0 7.06.97 10 2.68V20H0v-3.32z"
        />
      </svg>
    </picture>
    <h1 class="mt-2 text-2xl">{{ account.name }}</h1>
    <a class="mt-2 p-2 bg-color3 rounded-lg" :href="'mailto:'+account.email">✉️ {{ account.email }}</a>
    <div class="mt-2 text-center">
      <h2 title="Phone Number">📞 {{ account.phone }}</h2>
      <h2 title="Date Of Birth">🎂 {{ accountDate }}</h2>
      <div v-if="getCustomer">
        <h2 title="Store Credit">💵 {{ getCustomer.credit }}</h2>
      </div>
      <div v-if="getSeller">
        <h2 title="Payment ID">🆔 {{ getSeller.paymentID }}</h2>
        <h2 title="Billing Address">🏢 {{ getSeller.billing }}</h2>
        <h2 title="Revenue">💰 ${{ getSeller.revenue.toLocaleString() }}</h2>
      </div>
    </div>
  </main>
</template>

<script>
import moment from "moment";
import helper from "@/helper";
import gql from "graphql-tag";
export default {
  name: "Account",
  mixins: [helper],
  computed: {
    userType() {
      return this.$store.getters.getUserData.userType;
    },
    account() {
      if (this.userType === "CUST" && this.getCustomer) {
        return this.getCustomer.account;
      } else if (this.userType === "SELL" && this.getSeller) {
        return this.getSeller.account;
      }
      return null;
    },
    accountDate() {
      if (this.account) {
        return moment(this.account.dateOfBirth).format("MMMM Do, YYYY");
      }
      return null;
    },
  },
  apollo: {
    getCustomer: {
      query: gql`
        query GetCustomer {
          getCustomer {
            id
            account {
              id
              email
              image
              name
              phone
              dateOfBirth
              created
            }
            credit
          }
        }
      `,
    },
    getSeller: {
      query: gql`
        query GetSeller {
          getSeller {
            id
            account {
              id
              email
              image
              name
              phone
              dateOfBirth
              created
            }
            paymentID
            billing
            revenue
          }
        }
      `,
    },
  },
  beforeCreate() {
    if (!this.$store.getters.getUserData.isLoggedIn) {
      this.$router.push({ name: "Login" });
    }
  },
};
</script>
