<template>
  <div id="app" class="font-body flex flex-col min-h-screen text-color5 break-words">
    <Navigation />
    <router-view class="flex-grow" />
    <Footer />
  </div>
</template>
<script>
import gql from "graphql-tag";
import store from "@/store";
import Navigation from "@/components/Navigation.vue";
import Footer from "@/components/Footer.vue";
export default {
  name: "App",
  components: {
    Navigation,
    Footer,
  },
  methods: {
    refreshToken() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation RefreshToken {
              refreshToken
            }
          `,
        })
        .then((data) => {
          const response = data.data.refreshToken;
          if (response !== null) {
            console.log(response);
          } else {
            console.log("no response");
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    store.dispatch("loadData");
  },
};
</script>
<style>
:root,
.light {
  --color1: #ffffff;
  --color2: #1a202c;
  --color3: #edf2f7;
  --color4: #2c5282;
  --color5: #2a4365;
  --color6: #3182ce;
  --color7: #9499a5;
  --color8: #d8dfe7;
  --color9: #c8d0da;
}

@tailwind base;

@font-face {
  font-family: Quicksand;
  src: url(assets/fonts/Quicksand-Light.woff) format("woff");
}

@font-face {
  font-family: Livvic;
  src: url(assets/fonts/Livvic-Regular.woff) format("woff");
}

@tailwind components;

@tailwind utilities;

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  margin: 0;
}
input[type="number"] {
  -moz-appearance: textfield;
}
</style>
