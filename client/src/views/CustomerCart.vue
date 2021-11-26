<template>
  <main v-if="getCustomerCartItems" class="container mx-auto p-4">
    <section class="p-4 bg-color3 rounded-lg">
      <div class="flex justify-between items-center">
        <h1 class="text-2xl leading-tight">Your Cart</h1>
        <button
          v-if="canCheckout"
          class="p-1 w-32 bg-color5 rounded-sm flex items-center justify-center hover:bg-color4 focus:outline-none focus:bg-color4 text-white"
          title="Checkout"
          @click="performCheckout(getCustomerCartItems)"
        >
          <svg class="h-4 mr-1" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="M4 2h16l-3 9H4a1 1 0 1 0 0 2h13v2H4a3 3 0 0 1 0-6h.33L3 5 2 2H0V0h3a1 1 0 0 1 1 1v1zm1 18a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm10 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"
            />
          </svg>
          <span>Checkout</span>
        </button>
      </div>
      <div v-if="getCustomerCartItems.length > 0" class="mt-3 grid gap-4 lg:grid-cols-2">
        <div
          v-for="cartItem in getCustomerCartItems"
          :key="cartItem.id"
          class="flex bg-white rounded-lg"
        >
          <router-link
            :to="{ name: 'CustomerProduct', params: { productID: cartItem.product.id }}"
            class="w-1/3 max-w-4xs flex items-center"
          >
            <img
              class="h-40 w-40 object-contain"
              v-if="cartItem.product.image"
              :src="serverURL + cartItem.product.image.substring(1)"
              :alt="cartItem.product.name"
            />
            <svg v-else class="h-full w-40 p-8" viewBox="0 0 20 20">
              <path
                fill="currentColor"
                d="M17 6V5h-2V2H3v14h5v4h3.25H11a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6zm-5.75 14H3a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h12a2 2 0 0 1 2 2v4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-5.75zM11 8v8h6V8h-6zm3 11a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"
              />
            </svg>
          </router-link>
          <div class="p-2 flex flex-col w-2/3">
            <h1 class="truncate text-xl" v-text="cartItem.product.name"></h1>
            <h2 class="text-sm">
              Quantity : {{ cartItem.quantity }}
              <span v-if="cartItem.quantity == 1">Piece</span>
              <span v-else>Pieces</span>
            </h2>
            <div class="mt-1 font-title flex items-center">
              <h2
                v-if="cartItem.product.discount"
                class="line-through text-color7"
              >${{ (cartItem.product.mrp * cartItem.quantity).toLocaleString() }}</h2>
              <h2
                v-if="cartItem.product.discount"
                class="ml-1 font-bold text-green-600 text-sm"
              >{{ cartItem.product.discount }}% Off</h2>
            </div>
            <h1
              class="font-title text-2xl font-bold"
            >${{ (discountPrice(cartItem)).toLocaleString() }}</h1>
            <div class="mt-1 grid grid-cols-2 gap-1 max-w-2xs text-center">
              <button
                v-if="cartItem.product.inStock"
                class="p-1 bg-green-600 rounded-sm flex items-center justify-center hover:bg-green-500 focus:outline-none focus:bg-green-500 text-white"
                title="Buy Now"
                @click="performCheckout([cartItem])"
              >
                <svg class="h-4 mr-1" viewBox="0 0 20 20">
                  <path fill="currentColor" d="M13 8V0L8.11 5.87 3 12h4v8L17 8h-4z" />
                </svg>
                <span>Buy Now</span>
              </button>
              <div
                v-else
                class="flex items-center p-1 bg-red-600 justify-center rounded-sm text-white"
              >
                <span>Out Of Stock</span>
              </div>
              <button
                class="p-1 bg-color5 rounded-sm flex items-center justify-center hover:bg-color4 focus:outline-none focus:bg-color4 text-white"
                title="Remove From Cart"
                @click="deleteCustomerCartItem(cartItem.id)"
              >
                <svg class="h-4 mr-1" viewBox="0 0 20 20">
                  <path
                    fill="currentColor"
                    d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm1.41-1.41A8 8 0 1 0 15.66 4.34 8 8 0 0 0 4.34 15.66zm9.9-8.49L11.41 10l2.83 2.83-1.41 1.41L10 11.41l-2.83 2.83-1.41-1.41L8.59 10 5.76 7.17l1.41-1.41L10 8.59l2.83-2.83 1.41 1.41z"
                  />
                </svg>
                <span>Remove</span>
              </button>
            </div>
          </div>
        </div>
      </div>
      <h2 v-else class="mt-2">
        You do not have any items in your cart,
        <router-link :to="{ name: 'Home' }" class="underline" title="TechToys">continue shopping</router-link>
      </h2>
    </section>
    <div
      v-if="checkoutConfirm"
      class="fixed inset-0 z-10 bg-black bg-opacity-50 flex items-center justify-center"
    >
      <section
        class="mx-4 max-h-4/5 overflow-auto bg-color1 p-2 rounded-md flex flex-col w-full sm:w-96"
      >
        <div class="py-1 px-2 rounded-md bg-color3 leading-snug">
          <h1>You are about to purchase the following</h1>
          <h2 v-if="checkoutOutOfStock" class="text-xs">(Some items in your cart are out of stock)</h2>
        </div>
        <div
          v-for="cartItem in checkoutCartItems"
          class="mt-2 flex items-center"
          :key="cartItem.id"
        >
          <picture>
            <img
              class="h-32 w-32 object-contain"
              v-if="cartItem.product.image"
              :src="serverURL + cartItem.product.image.substring(1)"
              :alt="cartItem.product.name"
            />
            <svg v-else class="h-32 w-32 p-6" viewBox="0 0 20 20">
              <path
                fill="currentColor"
                d="M17 6V5h-2V2H3v14h5v4h3.25H11a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6zm-5.75 14H3a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h12a2 2 0 0 1 2 2v4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-5.75zM11 8v8h6V8h-6zm3 11a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"
              />
            </svg>
          </picture>
          <div class="text-sm">
            <h1 class="truncate text-lg" v-text="cartItem.product.name"></h1>
            <h2>
              Quantity : {{ cartItem.quantity }}
              <span v-if="cartItem.quantity == 1">Piece</span>
              <span v-else>Pieces</span>
            </h2>
            <h2
              v-if="cartItem.product.discount"
            >MRP : ${{ (cartItem.product.mrp * cartItem.quantity).toLocaleString() }}</h2>
            <h2>Discount Price : ${{ (discountPrice(cartItem)).toLocaleString() }}</h2>
          </div>
        </div>
        <div class="font-title font-bold text-right">
          <h1 class="mx-1 text-xl">Cart Total : ${{ checkoutDiscountTotal }}</h1>
          <h1 v-if="savingsPercentage" class="mx-1 text-green-600 font-title font-bold">
            You Save : ${{ checkoutTotal - checkoutDiscountTotal }}
            ({{ savingsPercentage }}% Savings)
          </h1>
          <h1
            v-if="checkoutDiscountTotal > customerCredit"
            class="text-center text-sm text-red-700"
          >You don't have enough credit to place this order</h1>
          <select
            ref="selectedAddress"
            class="mt-2 w-full p-1 font-body truncate border bg-color3 rounded-md focus:outline-none focus:shadow-md"
            v-model="addressID"
            required
          >
            <option disabled selected value>Select An Address</option>
            <option
              v-for="address in getCustomerAddresses"
              :key="address.id"
              :value="address.id"
              v-text="truncateAddress(address, 8)"
            ></option>
          </select>
        </div>
        <form class="mt-2" @submit.prevent="addCustomerAddress">
          <textarea
            class="w-full border-b-2 focus:outline-none focus:border-color5"
            rows="2"
            maxlength="256"
            placeholder="Locality"
            v-model="addressLocality"
            required
          ></textarea>
          <div class="mt-2 grid grid-cols-2 gap-2 items-baseline">
            <input
              class="border-b-2 focus:outline-none focus:border-color5"
              type="text"
              placeholder="City"
              maxlength="64"
              v-model="addressCity"
              required
            />
            <input
              class="border-b-2 focus:outline-none focus:border-color5"
              type="text"
              placeholder="State"
              maxlength="64"
              v-model="addressState"
              required
            />
            <input
              class="border-b-2 focus:outline-none focus:border-color5"
              type="number"
              min="100000"
              max="999999"
              placeholder="Pincode"
              v-model.number="addressPincode"
              required
            />
            <button
              class="mt-2 flex items-center justify-center p-1 bg-orange-600 text-white rounded-md hover:bg-orange-500 focus:bg-orange-500 focus:outline-none"
            >
              <svg class="h-4 mr-1" viewBox="0 0 20 20">
                <path
                  fill="currentColor"
                  d="M10 20S3 10.87 3 7a7 7 0 1 1 14 0c0 3.87-7 13-7 13zm0-11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"
                />
              </svg>
              <span>Add Address</span>
            </button>
          </div>
        </form>
        <div class="mt-2 grid grid-cols-2 gap-1 text-white">
          <button
            class="bg-color5 p-1 rounded-sm hover:bg-color4 focus:outline-none focus:bg-color4"
            title="Checkout Later"
            @click="checkoutConfirm=false"
          >Checkout Later</button>
          <button
            v-if="checkoutDiscountTotal <= customerCredit"
            class="bg-green-500 p-1 rounded-sm hover:bg-green-400 focus:outline-none focus:bg-green-400"
            title="Confirm Purchase"
            @click="confirmPurchase"
          >Confirm Purchase</button>
        </div>
      </section>
    </div>
  </main>
</template>

<script>
import helper from "@/helper";
import gql from "graphql-tag";
export default {
  name: "CustomerCart",
  mixins: [helper],
  data() {
    return {
      checkoutConfirm: false,
      checkoutCartItems: [],
      checkoutTotal: 0,
      checkoutDiscountTotal: 0,
      checkoutOutOfStock: false,
      addressID: "",
      addressLocality: "",
      addressCity: "",
      addressState: "",
      addressPincode: "",
    };
  },
  computed: {
    canCheckout() {
      for (let i in this.getCustomerCartItems) {
        if (this.getCustomerCartItems[i].product.inStock) {
          return true;
        }
      }
      return false;
    },
    savingsPercentage() {
      if (this.checkoutTotal > 0 && this.checkoutDiscountTotal > 0) {
        return Math.ceil(
          (100 * (this.checkoutTotal - this.checkoutDiscountTotal)) /
            this.checkoutTotal
        );
      } else {
        return 0;
      }
    },
    customerCredit() {
      return this.$store.getters.getUserData.customer.credit;
    },
  },
  methods: {
    discountPrice(cartItem) {
      return (
        Math.floor(
          (cartItem.product.mrp * (100 - cartItem.product.discount)) / 100
        ) * cartItem.quantity
      );
    },
    performCheckout(cartItems) {
      this.checkoutCartItems = [];
      this.checkoutTotal = this.checkoutDiscountTotal = 0;
      this.checkoutOutOfStock = false;
      for (let i in cartItems) {
        if (cartItems[i].product.inStock) {
          this.checkoutCartItems.push(cartItems[i]);
          this.checkoutTotal +=
            cartItems[i].product.mrp * cartItems[i].quantity;
          this.checkoutDiscountTotal += this.discountPrice(cartItems[i]);
        } else {
          this.checkoutOutOfStock = true;
        }
      }
      this.checkoutConfirm = true;
    },
    deleteCustomerCartItem(cartItemID) {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation DeleteCheckoutCartItem($cartItemID: ID) {
              deleteCustomerCartItem(cartItemID: $cartItemID)
            }
          `,
          variables: {
            cartItemID: cartItemID,
          },
        })
        .then((data) => {
          this.checkoutConfirm = false;
          this.$apollo.queries.getCustomerCartItems.refetch();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addCustomerAddress() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation AddCustomerAddress($addressInput: AddressInput) {
              addCustomerAddress(addressInput: $addressInput) {
                id
              }
            }
          `,
          variables: {
            addressInput: {
              locality: this.addressLocality,
              city: this.addressCity,
              state: this.addressState,
              pincode: this.addressPincode,
            },
          },
        })
        .then((data) => {
          if (data.data.addCustomerAddress !== null) {
            this.addressLocality = this.addressCity = this.addressState = this.addressPincode =
              "";
            this.$apollo.queries.getCustomerAddresses.refetch();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    confirmPurchase() {
      if (this.addressID === "") {
        this.$refs.selectedAddress.reportValidity();
      } else {
        let cartItemIDs = [];
        for (let i in this.checkoutCartItems) {
          cartItemIDs.push(this.checkoutCartItems[i].id);
        }
        this.$apollo
          .mutate({
            mutation: gql`
              mutation ConfirmPurchase($cartItemIDs: [ID], $addressID: ID) {
                addCustomerOrders(
                  cartItemIDs: $cartItemIDs
                  addressID: $addressID
                )
              }
            `,
            variables: {
              cartItemIDs: cartItemIDs,
              addressID: this.addressID,
            },
          })
          .then((data) => {
            if (data.data.addCustomerOrders === true) {
              this.$router.push({ name: "CustomerOrders" });
            }
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
  beforeCreate() {
    if (!this.$store.getters.getUserData.userType === "CUST") {
      this.$router.push({ name: "Login" });
    }
  },
  created() {
    this.$apollo.queries.getCustomerCartItems.refetch();
    this.$apollo.queries.getCustomerAddresses.refetch();
    this.$apollo
      .query({
        query: gql`
          query GetCustomerCredit {
            getCustomer {
              credit
            }
          }
        `,
      })
      .then((data) => {
        this.$store.dispatch("setCustomerCredit", {
          credit: data.data.getCustomer.credit,
        });
      })
      .catch((error) => {
        console.error(error);
      });
  },
  apollo: {
    getCustomerCartItems: {
      query: gql`
        query GetCustomerCartItems {
          getCustomerCartItems {
            id
            product {
              id
              image
              name
              mrp
              discount
              inStock
            }
            quantity
          }
        }
      `,
    },
    getCustomerAddresses: {
      query: gql`
        query GetCustomerAddresses {
          getCustomerAddresses {
            id
            locality
            city
            state
            pincode
          }
        }
      `,
    },
  },
};
</script>
