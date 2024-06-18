<template>
  <main class="container mx-auto p-4">
    <template v-if="isSeller">
      <section v-if="getSellerProducts" class="p-4 bg-color3 rounded-lg">
        <h1 class="text-2xl leading-tight">Your Products</h1>
        <div class="mt-2 grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5">
          <router-link
            v-for="product in getSellerProducts"
            :key="product.id"
            :to="{ name: 'SellerProduct', params: { productID: product.id }}"
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
                <button
                  class="text-xs p-1 rounded-md focus:outline-none"
                  :class="product.inStock?'bg-green-500 text-white hover:bg-green-400 focus:bg-green-400':'bg-red-200 text-red-700 hover:text-red-600 focus:text-red-600'"
                  title="Change Product Stock"
                  @click.prevent="editProductStock(product)"
                >In Stock</button>
              </div>
            </div>
          </router-link>
          <router-link
            :to="{ name: 'AddProduct' }"
            class="p-4 flex bg-color5 text-color1 rounded-xl min-h-60 hover:bg-color4"
            title="Add New Product"
          >
            <svg class="m-auto h-20" viewBox="0 0 20 20">
              <path
                fill="currentColor"
                d="M11 9V5H9v4H5v2h4v4h2v-4h4V9h-4zm-1 11a10 10 0 1 1 0-20 10 10 0 0 1 0 20z"
              />
            </svg>
          </router-link>
        </div>
      </section>
      <section v-if="getSellerPendingOrders" class="mt-4 p-4 bg-color3 rounded-lg">
        <h1 class="text-2xl leading-tight">Pending Orders</h1>
        <div v-if="getSellerPendingOrders.length > 0" class="mt-3 grid gap-4 lg:grid-cols-2">
          <div
            v-for="order in getSellerPendingOrders"
            :key="order.id"
            class="flex bg-white rounded-lg"
          >
            <router-link
              :to="{ name: 'SellerProduct', params: { productID: order.product.id }}"
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
                Amount Received : ${{ order.amount }} ({{ order.quantity }}
                <span
                  v-if="order.quantity == 1"
                >Piece</span>
                <span v-else>Pieces</span>)
              </h2>
              <h2
                :title="order.address.locality + ', ' + order.address.city + ', ' + order.address.state + ' - ' + order.address.pincode"
              >Address : {{ truncateAddress(order.address, 64) }}</h2>
            </div>
          </div>
        </div>
        <h2 v-else class="mt-2">
          You do not have any pending orders.
        </h2>
      </section>
    </template>
    <div v-else>
      <img
        class="mx-auto w-full max-w-2xl"
        src="@/assets/images/seller-banner.svg"
        alt="Welcome to Tech Toys"
      />
      <h1
        class="mt-6 font-title tracking-tighter leading-tight text-3xl text-center md:text-left"
      >Why Sell On TechToys?</h1>
      <div class="flex flex-wrap flex-col items-center justify-between md:flex-row">
        <div class="mt-4 w-56">
          <svg class="mx-auto md:mx-0 h-10" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="M4.13 12H4a2 2 0 1 0 1.8 1.11L7.86 10a2.03 2.03 0 0 0 .65-.07l1.55 1.55a2 2 0 1 0 3.72-.37L15.87 8H16a2 2 0 1 0-1.8-1.11L12.14 10a2.03 2.03 0 0 0-.65.07L9.93 8.52a2 2 0 1 0-3.72.37L4.13 12zM0 4c0-1.1.9-2 2-2h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4z"
            />
          </svg>
          <h3
            class="mt-1 text-center md:text-left"
          >Widen your customer base and grow your business further with our support</h3>
        </div>
        <div class="mt-4 w-56">
          <svg class="mx-auto md:mx-0 h-10" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="M1 10h3v10H1V10zM6 0h3v20H6V0zm5 8h3v12h-3V8zm5-4h3v16h-3V4z"
            />
          </svg>
          <h3
            class="mt-1 text-center md:text-left"
          >TechToys' online marketplace allows you to reap the benefits of sales without limitations</h3>
        </div>
        <div class="mt-4 w-56">
          <svg class="mx-auto md:mx-0 h-10" viewBox="0 0 640 512">
            <path
              fill="currentColor"
              d="M624 352h-16V243.9c0-12.7-5.1-24.9-14.1-33.9L494 110.1c-9-9-21.2-14.1-33.9-14.1H416V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48v320c0 26.5 21.5 48 48 48h16c0 53 43 96 96 96s96-43 96-96h128c0 53 43 96 96 96s96-43 96-96h48c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zM160 464c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm320 0c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm80-208H416V144h44.1l99.9 99.9V256z"
            />
          </svg>
          <h3
            class="mt-1 text-center md:text-left"
          >Enjoy easy pick-up and delivery with our logistics partner</h3>
        </div>
        <div class="mt-4 w-56">
          <svg class="mx-auto md:mx-0 h-10" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="m12.9 14.32c-3.336 2.5915-8.1122 2.1424-10.906-1.0244-2.7934-3.1667-2.6406-7.9585 0.34612-10.945 2.9868-2.9868 7.7786-3.1396 10.945-0.34612 3.1668 2.7935 3.6159 7.5697 1.0244 10.906l5.35 5.33-1.42 1.42-5.33-5.34zm-4.9-0.32c3.3137 0 6-2.6863 6-6 0-3.3137-2.6863-6-6-6-3.3137 0-6 2.6863-6 6 0 3.3137 2.6863 6 6 6z"
            />
          </svg>
          <h3
            class="mt-1 text-center md:text-left"
          >Transparency and equal opportunities among all the sellers to grow</h3>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import Rating from "@/components/Rating.vue";
import helper from "@/helper";
import gql from "graphql-tag";
export default {
  name: "Seller",
  components: { Rating },
  mixins: [helper],
  computed: {
    isSeller() {
      return this.$store.getters.getUserData.userType == "SELL";
    },
  },
  methods: {
    editProductStock(product) {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation EditProductStock($productID: ID, $inStock: Boolean) {
              editProductStock(productID: $productID, inStock: $inStock) {
                inStock
              }
            }
          `,
          variables: {
            productID: product.id,
            inStock: !product.inStock,
          },
        })
        .then((data) => {
          this.$apollo.queries.getSellerProducts.refetch();
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  apollo: {
    getSellerProducts: {
      query: gql`
        query GetSellerProducts {
          getSellerProducts {
            id
            image
            name
            mrp
            discount
            inStock
            rating
          }
        }
      `,
    },
    getSellerPendingOrders: {
      query: gql`
        query GetSellerPendingOrders {
          getSellerPendingOrders {
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
  created() {
    if (this.$store.getters.getUserData.userType === "SELL") {
      this.$apollo.queries.getSellerProducts.refetch();
      this.$apollo.queries.getSellerPendingOrders.refetch();
    }
  },
};
</script>
<style scoped>
.grid {
  grid-auto-rows: 1fr;
}
</style>