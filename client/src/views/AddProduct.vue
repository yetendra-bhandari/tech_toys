<template>
  <main class="container mx-auto p-4">
    <form
      @submit.prevent="addSellerProduct"
      class="flex flex-col items-center mx-auto w-full md:w-128"
    >
      <div class="relative">
        <label
          class="block w-64 h-64 shadow-md rounded-md cursor-pointer bg-contain bg-center bg-no-repeat hover:bg-color3"
          :style="{ backgroundImage: 'url(' + image + ')' }"
          :title="image?'Change Product Image':'Add Product Image'"
        >
          <input
            type="file"
            accept="image/*"
            class="hidden"
            ref="productImage"
            @change="showProductImage"
          />
          <svg v-if="!image" class="w-64 h-64 p-12" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="M17 6V5h-2V2H3v14h5v4h3.25H11a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6zm-5.75 14H3a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h12a2 2 0 0 1 2 2v4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-5.75zM11 8v8h6V8h-6zm3 11a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"
            />
          </svg>
        </label>
        <button
          type="button"
          class="absolute top-0 right-0 focus:outline-none"
          title="Remove Product Image"
          @click="clearProductImage"
          v-show="image"
        >
          <svg
            class="h-6 p-1.5 text-white mt-2 mr-2 rounded-full bg-red-600 hover:bg-red-500"
            viewBox="0 0 20 20"
          >
            <path
              fill="currentColor"
              d="M10 8.586L2.929 1.515 1.515 2.929 8.586 10l-7.071 7.071 1.414 1.414L10 11.414l7.071 7.071 1.414-1.414L11.414 10l7.071-7.071-1.414-1.414L10 8.586z"
            />
          </svg>
        </button>
      </div>
      <input
        class="mt-8 w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
        type="text"
        placeholder="Product Name"
        v-model.trim="name"
        required
      />
      <textarea
        class="mt-4 block w-full h-32 px-2 py-1 border-b-2 text-sm focus:outline-none focus:border-color5"
        v-model.trim="description"
        placeholder="Description"
        required
      ></textarea>
      <textarea
        class="mt-4 block w-full h-32 px-2 py-1 border-b-2 text-sm focus:outline-none focus:border-color5"
        v-model.trim="specifications"
        placeholder="Specifications"
        required
      ></textarea>
      <div class="w-full flex flex-col items-start sm:flex-row sm:justify-between sm:items-center">
        <input
          class="mt-4 w-32 px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
          type="number"
          min="1"
          step="1"
          placeholder="MRP ($)"
          v-model.number="mrp"
          required
        />
        <input
          class="mt-4 w-32 px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
          type="number"
          step="1"
          min="0"
          max="99"
          placeholder="Discount (%)"
          v-model.number="discount"
          required
        />
        <div class="mt-4 px-2">Discounted Price : {{ discountPrice }}</div>
      </div>
      <div class="mt-4 w-full flex justify-evenly">
        <select
          class="p-1 border bg-color3 rounded-md focus:outline-none focus:shadow-md"
          v-model="category"
          required
        >
          <option selected disabled value>Category</option>
          <option value="LAPT">Laptops</option>
          <option value="EARP">Earphones</option>
          <option value="HEAD">Headphones</option>
          <option value="VIRT">VR Headsets</option>
        </select>
        <button
          type="button"
          class="px-2 py-1 rounded-md flex items-center focus:outline-none"
          title="Change Product Stock"
          :class="inStock?'bg-green-500 text-white hover:bg-green-400 focus:bg-green-400':'bg-red-200 text-red-700 hover:text-red-600 focus:text-red-600'"
          @click="inStock=!inStock"
        >
          <span v-if="inStock">In Stock</span>
          <span v-else>Out Of Stock</span>
          <svg class="ml-1.5 h-4 w-4" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="M18 9.87V20H2V9.87a4.25 4.25 0 0 0 3-.38V14h10V9.5a4.26 4.26 0 0 0 3 .37zM3 0h4l-.67 6.03A3.43 3.43 0 0 1 3 9C1.34 9 .42 7.73.95 6.15L3 0zm5 0h4l.7 6.3c.17 1.5-.91 2.7-2.42 2.7h-.56A2.38 2.38 0 0 1 7.3 6.3L8 0zm5 0h4l2.05 6.15C19.58 7.73 18.65 9 17 9a3.42 3.42 0 0 1-3.33-2.97L13 0z"
            />
          </svg>
        </button>
      </div>
      <input
        class="mt-4 px-2 py-1 rounded-lg bg-color5 text-color1 cursor-pointer hover:bg-color4 focus:outline-none"
        type="submit"
        value="Add This Product"
      />
    </form>
  </main>
</template>

<script>
import gql from "graphql-tag";
export default {
  name: "AddProduct",
  data() {
    return {
      image: null,
      name: "",
      description: "",
      specifications: "",
      mrp: null,
      discount: null,
      category: "",
      inStock: true,
    };
  },
  computed: {
    discountPrice() {
      if (
        this.mrp !== null &&
        this.discount !== null &&
        this.mrp > 0 &&
        this.discount >= 0 &&
        this.discount < 100
      ) {
        return (
          "$" +
          Math.floor((this.mrp * (100 - this.discount)) / 100).toLocaleString()
        );
      } else {
        return "N/A";
      }
    },
  },
  methods: {
    showProductImage() {
      const productImage = this.$refs.productImage;
      if (productImage.files.length) {
        if (productImage.files[0].size > 2500000) {
          alert("Image Size Cannot Be Greater Than 2.5MB");
          productImage.value = "";
        } else {
          const reader = new FileReader();
          reader.onload = (data) => {
            this.image = data.target.result;
          };
          reader.readAsDataURL(productImage.files[0]);
        }
      } else {
        this.image = null;
      }
    },
    clearProductImage() {
      this.$refs.productImage.value = "";
      this.image = null;
    },
    addSellerProduct() {
      const product = {
        name: this.name,
        description: this.description,
        specifications: this.specifications,
        mrp: this.mrp,
        discount: this.discount,
        category: this.category,
        inStock: this.inStock,
      };
      if (this.$refs.productImage.files.length) {
        product.image = this.$refs.productImage.files[0];
      }
      this.$apollo
        .mutate({
          mutation: gql`
            mutation AddSellerProduct($productInput: ProductInput) {
              addSellerProduct(productInput: $productInput) {
                id
              }
            }
          `,
          variables: {
            productInput: product,
          },
        })
        .then((data) => {
          this.$router.push({ name: "Home" });
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
