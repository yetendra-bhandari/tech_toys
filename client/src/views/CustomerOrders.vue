<template>
  <main class="container mx-auto p-4">
    <section v-if="getCustomerOrders" class="p-4 bg-color3 rounded-lg">
      <h1 class="text-2xl leading-tight">Your Orders</h1>
      <div v-if="getCustomerOrders.length > 0" class="mt-3 grid gap-4 lg:grid-cols-2">
        <div v-for="order in getCustomerOrders" :key="order.id" class="flex bg-white rounded-lg">
          <router-link
            :to="{ name: 'CustomerProduct', params: { productID: order.product.id }}"
            class="w-1/3 max-w-4xs flex items-center"
          >
            <img
              class="h-40 w-40 object-contain"
              v-if="order.product.image"
              :src="serverURL + order.product.image.substring(1)"
              :alt="order.product.name"
            />
            <svg v-else class="h-full w-40 p-8" viewBox="0 0 20 20">
              <path
                fill="currentColor"
                d="M17 6V5h-2V2H3v14h5v4h3.25H11a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6zm-5.75 14H3a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h12a2 2 0 0 1 2 2v4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-5.75zM11 8v8h6V8h-6zm3 11a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"
              />
            </svg>
          </router-link>
          <div class="p-2 flex flex-col w-2/3 text-sm">
            <h1 class="truncate text-xl" v-text="order.product.name"></h1>
            <h2 class="text-xs leading-none" v-text="dateTimeFormat(order.time)"></h2>
            <h2 class="mt-auto">
              Amount Paid : ${{ order.amount }} ({{ order.quantity }}
              <span
                v-if="order.quantity == 1"
              >Piece</span>
              <span v-else>Pieces</span>)
            </h2>
            <h2
              :title="order.address.locality + ', ' + order.address.city + ', ' + order.address.state + ' - ' + order.address.pincode"
            >Address : {{ truncateAddress(order.address, 5) }}</h2>
            <h2>
              Status :
              <span v-if="order.status === 'PEN'">Undelivered</span>
              <span v-else-if="order.status === 'DEL'">Delivered</span>
              <span v-else-if="order.status === 'CNL'">Cancelled</span>
            </h2>
            <div
              v-if="order.status === 'PEN'"
              class="mt-1 grid grid-cols-2 gap-1 max-w-2xs text-center text-base"
            >
              <button
                class="p-1 bg-green-600 rounded-sm flex items-center justify-center hover:bg-green-500 focus:outline-none focus:bg-green-500 text-white"
                title="Confirm Delivery"
                @click="editCustomerOrderStatus(order.id, 'DEL')"
              >
                <svg class="h-4 mr-1" viewBox="0 0 640 512">
                  <path
                    fill="currentColor"
                    d="M624 352h-16V243.9c0-12.7-5.1-24.9-14.1-33.9L494 110.1c-9-9-21.2-14.1-33.9-14.1H416V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48v320c0 26.5 21.5 48 48 48h16c0 53 43 96 96 96s96-43 96-96h128c0 53 43 96 96 96s96-43 96-96h48c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zM160 464c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm320 0c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm80-208H416V144h44.1l99.9 99.9V256z"
                  />
                </svg>
                <span>Delivered</span>
              </button>
              <button
                class="p-1 bg-red-600 rounded-sm flex items-center justify-center hover:bg-red-500 focus:outline-none focus:bg-red-500 text-white"
                title="Cancel Order"
                @click="editCustomerOrderStatus(order.id, 'CNL')"
              >
                <svg class="h-4 mr-1" viewBox="0 0 20 20">
                  <path
                    fill="currentColor"
                    d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm1.41-1.41A8 8 0 1 0 15.66 4.34 8 8 0 0 0 4.34 15.66zm9.9-8.49L11.41 10l2.83 2.83-1.41 1.41L10 11.41l-2.83 2.83-1.41-1.41L8.59 10 5.76 7.17l1.41-1.41L10 8.59l2.83-2.83 1.41 1.41z"
                  />
                </svg>
                <span>Cancel</span>
              </button>
            </div>
          </div>
        </div>
      </div>
      <h2 v-else class="mt-2">
        You have not placed any orders yet,
        <router-link :to="{ name: 'Home' }" class="underline" title="TechToys">continue shopping</router-link>
      </h2>
    </section>
  </main>
</template>

<script>
import helper from "@/helper";
import gql from "graphql-tag";
export default {
  name: "CustomerOrders",
  mixins: [helper],
  methods: {
    editCustomerOrderStatus(orderID, status) {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation EditCustomerOrderStatus($orderID: ID, $status: String) {
              editCustomerOrderStatus(orderID: $orderID, status: $status)
            }
          `,
          variables: {
            orderID: orderID,
            status: status,
          },
        })
        .then((data) => {
          const response = data.data.editCustomerOrderStatus;
          if (response === true) {
            this.$apollo.queries.getCustomerOrders.refetch();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  beforeCreate() {
    if (!this.$store.getters.getUserData.userType === "CUST") {
      this.$router.push({ name: "Login" });
    }
  },
  created() {
    this.$apollo.queries.getCustomerOrders.refetch();
  },
  apollo: {
    getCustomerOrders: {
      query: gql`
        query GetCustomerOrders {
          getCustomerOrders {
            id
            product {
              id
              image
              name
            }
            amount
            quantity
            time
            address {
              id
              locality
              city
              state
              pincode
            }
            status
          }
        }
      `,
    },
  },
};
</script>
