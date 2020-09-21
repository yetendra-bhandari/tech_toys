<template>
  <main class="container mx-auto p-4">
    <h1 class="font-title text-3xl text-center">Great to see you there!</h1>
    <button
      class="mt-12 block mx-auto p-4 border rounded-md hover:bg-color3 focus:outline-none focus:text-color4"
      title="Switch Account Type"
      @click="isCustomer=!isCustomer; clearEmailValidation();"
    >
      <svg v-show="isCustomer" class="h-24" viewBox="0 0 20 20">
        <path
          fill="currentColor"
          d="M4 2h16l-3 9H4a1 1 0 1 0 0 2h13v2H4a3 3 0 0 1 0-6h.33L3 5 2 2H0V0h3a1 1 0 0 1 1 1v1zm1 18a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm10 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"
        />
      </svg>
      <svg v-show="!isCustomer" class="h-24" viewBox="0 0 20 20">
        <path
          fill="currentColor"
          d="M18 9.87V20H2V9.87a4.25 4.25 0 0 0 3-.38V14h10V9.5a4.26 4.26 0 0 0 3 .37zM3 0h4l-.67 6.03A3.43 3.43 0 0 1 3 9C1.34 9 .42 7.73.95 6.15L3 0zm5 0h4l.7 6.3c.17 1.5-.91 2.7-2.42 2.7h-.56A2.38 2.38 0 0 1 7.3 6.3L8 0zm5 0h4l2.05 6.15C19.58 7.73 18.65 9 17 9a3.42 3.42 0 0 1-3.33-2.97L13 0z"
        />
      </svg>
    </button>
    <div class="mt-2 text-center">
      <h4 v-show="isCustomer">Customer Account</h4>
      <h4 v-show="!isCustomer">Seller Account</h4>
    </div>
    <form
      ref="loginForm"
      class="mx-auto mt-8 w-full sm:w-72"
      v-show="isLogin"
      @submit.prevent="performLogin"
    >
      <input
        ref="loginEmailInput"
        type="email"
        class="block w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
        placeholder="Email"
        v-model.trim="account.email"
        @input="clearEmailValidation"
        required
        autofocus
      />
      <input
        ref="loginPasswordInput"
        type="password"
        class="mt-4 block w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
        placeholder="Password"
        v-model="account.password"
        @input="clearLoginPasswordValidation"
        required
      />
      <div class="flex items-start">
        <label class="mt-4 ml-2 flex items-center">
          <button
            type="button"
            class="h-6 w-6 rounded-md text-color5 focus:outline-none bg-color8 focus:bg-color9"
            @click="remember=!remember"
          >
            <span v-show="remember">✔</span>
          </button>
          <span class="ml-2 text-sm">Keep Me Signed In</span>
        </label>
      </div>
      <input
        type="submit"
        class="mt-6 bg-color5 block w-full p-2 focus:outline-none cursor-pointer text-color1 shadow-lg focus:bg-color4 rounded-full"
        value="Login"
      />
    </form>
    <form
      ref="signUpForm"
      class="mx-auto mt-8 w-full sm:w-72"
      v-show="!isLogin"
      @submit.prevent="performSignUp"
    >
      <h3 class="text-lg text-center">Tell Us About You</h3>
      <div class="mt-4 mx-auto h-32 w-32 relative">
        <label
          class="block h-32 w-32 rounded-full border-2 cursor-pointer overflow-hidden hover:bg-color3 hover:shadow-lg bg-cover bg-center"
          :style="{ backgroundImage: 'url(' + account.image + ')' }"
          :title="account.image?'Change Profile Picture':'Add Profile Picture'"
        >
          <input
            id="profilePicture"
            type="file"
            accept="image/*"
            class="hidden"
            ref="profilePicture"
            @change="showProfilePicture"
          />
          <svg class="pt-2" viewBox="0 0 20 20" v-show="!account.image">
            <path
              fill="currentColor"
              d="M5 5a5 5 0 0 1 10 0v2A5 5 0 0 1 5 7V5zM0 16.68A19.9 19.9 0 0 1 10 14c3.64 0 7.06.97 10 2.68V20H0v-3.32z"
            />
          </svg>
        </label>
        <label for="profilePicture" title="Add Profile Picture" v-show="!account.image">
          <svg
            class="h-8 absolute bottom-0 -right-6 cursor-pointer text-green-500 hover:text-green-400"
            viewBox="0 0 20 20"
          >
            <path
              fill="currentColor"
              d="M11 9V5H9v4H5v2h4v4h2v-4h4V9h-4zm-1 11a10 10 0 1 1 0-20 10 10 0 0 1 0 20z"
            />
          </svg>
        </label>
        <button
          type="button"
          title="Remove Profile Picture"
          @click="clearProfilePicture"
          v-show="account.image"
        >
          <svg
            class="h-8 absolute bottom-0 -right-6 text-red-600 hover:text-red-500"
            viewBox="0 0 20 20"
          >
            <path
              fill="currentColor"
              d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zM11.4 10l2.83-2.83-1.41-1.41L10 8.59 7.17 5.76 5.76 7.17 8.59 10l-2.83 2.83 1.41 1.41L10 11.41l2.83 2.83 1.41-1.41L11.41 10z"
            />
          </svg>
        </button>
      </div>
      <input
        type="text"
        pattern="[A-Za-z ]+"
        class="mt-4 block w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
        placeholder="Full Name"
        v-model.trim="account.name"
        required
      />
      <input
        ref="signUpEmailInput"
        type="email"
        class="mt-4 block w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
        placeholder="Email"
        v-model.trim="account.email"
        @input="clearEmailValidation"
        required
      />
      <input
        type="tel"
        maxlength="10"
        pattern="[0-9]{10}"
        class="mt-4 block w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
        placeholder="Phone Number"
        v-model="account.phone"
        required
      />
      <div class="mt-4 flex">
        <h3 class="pl-2 py-1">Date Of Birth</h3>
        <input
          type="date"
          class="ml-2 flex-grow pr-2 py-1 border-b-2 focus:outline-none text-right focus:border-color5"
          :max="validDate"
          v-model="account.dateOfBirth"
          required
        />
      </div>
      <input
        type="password"
        class="mt-4 block w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
        placeholder="Password"
        v-model="account.password"
        required
      />
      <input
        ref="confirmPassword"
        type="password"
        class="mt-4 block w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
        placeholder="Confirm Password"
        v-model="account.confirmPassword"
        @input="clearConfirmPasswordValidation"
        required
      />
      <div class="mt-10" v-show="!isCustomer">
        <h3 class="text-lg text-center">And Your Business</h3>
        <input
          type="text"
          class="mt-4 block w-full px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
          placeholder="Payment ID"
          v-model.trim="account.paymentID"
          :required="!isCustomer"
        />
        <textarea
          class="mt-4 block w-full h-24 px-2 py-1 border-b-2 focus:outline-none focus:border-color5"
          v-model.trim="seller.billing"
          placeholder="Billing Address"
          :required="!isCustomer"
        ></textarea>
      </div>
      <label class="mt-4 px-2 inline-flex items-center">
        <button
          type="button"
          class="h-6 w-6 rounded-md focus:outline-none bg-color8 focus:bg-color9"
          :class="remember?'text-color5':'text-transparent'"
          @click="remember=!remember"
        >✔</button>
        <span class="ml-2 text-sm">Keep Me Signed In</span>
      </label>
      <input
        type="submit"
        class="mt-6 bg-color5 block w-full p-2 focus:outline-none cursor-pointer text-color1 shadow-lg focus:bg-color4 rounded-full"
        value="Sign Up"
      />
    </form>
    <div class="mt-6 text-sm text-center">
      <h4 v-show="isLogin">
        Don't have an account?&nbsp;
        <button
          class="underline focus:outline-none focus:text-color4"
          @click="isLogin=false"
        >Sign Up</button>
      </h4>
      <h4 v-show="!isLogin">
        Already have an account?&nbsp;
        <button
          class="underline focus:outline-none focus:text-color4"
          @click="isLogin=true"
        >Login</button>
      </h4>
    </div>
  </main>
</template>
<script>
import gql from "graphql-tag";
export default {
  name: "Login",
  data() {
    return {
      isCustomer: true,
      isLogin: true,
      remember: true,
      account: {
        image: null,
        email: "",
        name: "",
        phone: "",
        password: "",
        confirmPassword: "",
        dateOfBirth: "",
      },
      seller: {
        paymentID: "",
        billing: "",
      },
    };
  },
  computed: {
    validDate() {
      const today = new Date();
      return (
        today.getFullYear() -
        18 +
        "-" +
        (today.getMonth() < 9 ? "0" : "") +
        (today.getMonth() + 1) +
        "-" +
        (today.getDate() < 10 ? "0" : "") +
        today.getDate()
      );
    },
  },
  methods: {
    isLoginValid() {
      return this.$refs.loginForm.checkValidity();
    },
    isSignUpValid() {
      return this.$refs.signUpForm.checkValidity();
    },
    clearEmailValidation() {
      this.$refs.loginEmailInput.setCustomValidity("");
      this.$refs.signUpEmailInput.setCustomValidity("");
      this.$refs.loginPasswordInput.setCustomValidity("");
    },
    loginPasswordValidation() {
      this.$refs.loginPasswordInput.setCustomValidity(
        "Your password is incorrect"
      );
      this.$refs.loginForm.reportValidity();
    },
    clearLoginPasswordValidation() {
      this.$refs.loginPasswordInput.setCustomValidity("");
    },
    clearConfirmPasswordValidation() {
      this.$refs.confirmPassword.setCustomValidity("");
    },
    async checkLogin() {
      const emailInput = this.$refs.loginEmailInput;
      const sellerExists = await this.sellerExists();
      const customerExists = await this.customerExists();
      if (
        (this.isCustomer && customerExists) ||
        (!this.isCustomer && sellerExists)
      ) {
        emailInput.setCustomValidity("");
      } else {
        emailInput.setCustomValidity(
          "An account with the given email address does not exist"
        );
      }
      this.$refs.loginForm.reportValidity();
    },
    async checkSignUp() {
      const emailInput = this.$refs.signUpEmailInput;
      const confirmPassword = this.$refs.confirmPassword;
      const sellerExists = await this.sellerExists();
      const customerExists = await this.customerExists();
      if (sellerExists || customerExists) {
        emailInput.setCustomValidity(
          "An account with the given email address already exists"
        );
      } else {
        emailInput.setCustomValidity("");
      }
      if (this.account.confirmPassword == this.account.password) {
        confirmPassword.setCustomValidity("");
      } else {
        confirmPassword.setCustomValidity("Passwords do not match");
      }
      this.$refs.signUpForm.reportValidity();
    },
    performLoginCustomer() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation LoginCustomer(
              $remember: Boolean
              $email: String
              $password: String
            ) {
              loginCustomer(
                remember: $remember
                accountInput: { email: $email, password: $password }
              ) {
                authToken
                customer {
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
            }
          `,
          variables: {
            remember: this.remember,
            email: this.account.email,
            password: this.account.password,
          },
        })
        .then((data) => {
          const response = data.data.loginCustomer;
          if (response !== null) {
            const userData = {
              isLoggedIn: true,
              userType: "CUST",
              authToken: response.authToken,
              account: {
                id: response.customer.account.id,
                email: response.customer.account.email,
                image: response.customer.account.image,
                name: response.customer.account.name,
                phone: response.customer.account.phone,
                dateOfBirth: response.customer.account.dateOfBirth,
                created: response.customer.account.created,
              },
              customer: {
                id: response.customer.id,
                credit: response.customer.credit,
              },
            };
            this.$store.dispatch("setUserData", { userData: userData });
            this.$router.push({ name: "Home" });
          } else {
            this.loginPasswordValidation();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    performLoginSeller() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation LoginSeller(
              $remember: Boolean
              $email: String
              $password: String
            ) {
              loginSeller(
                remember: $remember
                accountInput: { email: $email, password: $password }
              ) {
                authToken
                seller {
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
                }
              }
            }
          `,
          variables: {
            remember: this.remember,
            email: this.account.email,
            password: this.account.password,
          },
        })
        .then((data) => {
          const response = data.data.loginSeller;
          if (response !== null) {
            const userData = {
              isLoggedIn: true,
              userType: "SELL",
              authToken: response.authToken,
              account: {
                id: response.seller.account.id,
                email: response.seller.account.email,
                image: response.seller.account.image,
                name: response.seller.account.name,
                phone: response.seller.account.phone,
                dateOfBirth: response.seller.account.dateOfBirth,
                created: response.seller.account.created,
              },
              seller: {
                id: response.seller.id,
                paymentID: response.seller.paymentID,
                billing: response.seller.billing,
                revenue: response.seller.revenue,
              },
            };
            this.$store.dispatch("setUserData", { userData: userData });
            this.$router.push({ name: "Home" });
          } else {
            this.loginPasswordValidation();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    async performLogin() {
      await this.checkLogin();
      if (this.isLoginValid()) {
        if (this.isCustomer) {
          this.performLoginCustomer();
        } else {
          this.performLoginSeller();
        }
      }
    },
    showProfilePicture() {
      const profilePicture = this.$refs.profilePicture;
      if (profilePicture.files.length) {
        if (profilePicture.files[0].size > 2500000) {
          alert("Image Size Cannot Be Greater Than 2.5MB");
          profilePicture.value = "";
        } else {
          const reader = new FileReader();
          reader.onload = (data) => {
            this.account.image = data.target.result;
          };
          reader.readAsDataURL(profilePicture.files[0]);
        }
      } else {
        this.account.image = null;
      }
    },
    clearProfilePicture() {
      this.$refs.profilePicture.value = "";
      this.account.image = null;
    },
    performSignUpCustomer() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation SignUpCustomer(
              $remember: Boolean
              $customer: CustomerInput
            ) {
              addCustomer(remember: $remember, customerInput: $customer) {
                authToken
                customer {
                  id
                  account {
                    id
                    email
                    name
                    phone
                    dateOfBirth
                    created
                  }
                  credit
                }
              }
            }
          `,
          variables: {
            remember: this.remember,
            customer: {
              account: {
                email: this.account.email,
                name: this.account.name,
                phone: this.account.phone,
                dateOfBirth: this.account.dateOfBirth,
                password: this.account.password,
              },
            },
          },
        })
        .then((data) => {
          const response = data.data.addCustomer;
          if (response !== null) {
            const userData = {
              isLoggedIn: true,
              userType: "CUST",
              authToken: response.authToken,
              account: {
                id: response.customer.account.id,
                email: response.customer.account.email,
                image: response.customer.account.image,
                name: response.customer.account.name,
                phone: response.customer.account.phone,
                dateOfBirth: response.customer.account.dateOfBirth,
                created: response.customer.account.created,
              },
              customer: {
                id: response.customer.id,
                credit: response.customer.credit,
              },
            };
            this.$store
              .dispatch("setUserData", { userData: userData })
              .then(() => {
                this.uploadAccountImage();
              });
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    performSignUpSeller() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation SignUpSeller($remember: Boolean, $seller: SellerInput) {
              addSeller(remember: $remember, sellerInput: $seller) {
                authToken
                seller {
                  id
                  account {
                    id
                    email
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
            }
          `,
          variables: {
            remember: this.remember,
            seller: {
              account: {
                email: this.account.email,
                name: this.account.name,
                phone: this.account.phone,
                dateOfBirth: this.account.dateOfBirth,
                password: this.account.password,
              },
              paymentID: this.seller.paymentID,
              billing: this.seller.billing,
            },
          },
        })
        .then((data) => {
          const response = data.data.addSeller;
          if (response !== null) {
            const userData = {
              isLoggedIn: true,
              userType: "SELL",
              authToken: response.authToken,
              account: {
                id: response.seller.account.id,
                email: response.seller.account.email,
                image: response.seller.account.image,
                name: response.seller.account.name,
                phone: response.seller.account.phone,
                dateOfBirth: response.seller.account.dateOfBirth,
                created: response.seller.account.created,
              },
              seller: {
                id: response.seller.id,
                paymentID: response.seller.paymentID,
                billing: response.seller.billing,
                revenue: response.seller.revenue,
              },
            };
            this.$store
              .dispatch("setUserData", { userData: userData })
              .then(() => {
                this.uploadAccountImage();
              });
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    async performSignUp() {
      await this.checkSignUp();
      if (this.isSignUpValid()) {
        if (this.isCustomer) {
          this.performSignUpCustomer();
        } else if (!this.isCustomer) {
          this.performSignUpSeller();
        }
      }
    },
    uploadAccountImage() {
      if (this.$refs.profilePicture.files.length) {
        this.$apollo
          .mutate({
            mutation: gql`
              mutation UploadAccountImage($image: Upload) {
                editAccountImage(image: $image) {
                  image
                }
              }
            `,
            variables: {
              image: this.$refs.profilePicture.files[0],
            },
          })
          .then((data) => {
            const response = data.data.editAccountImage;
            if (response !== null) {
              this.$store.dispatch("setUserImage", { image: response.image });
            }
          })
          .catch((error) => {
            console.error(error);
          });
      }
      this.$router.push({ name: "Home" });
    },
    async sellerExists() {
      return await this.$apollo
        .query({
          query: gql`
            query SellerExists($email: String!) {
              sellerExists(email: $email)
            }
          `,
          variables: {
            email: this.account.email,
          },
        })
        .then((data) => {
          return data.data.sellerExists;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    async customerExists() {
      return await this.$apollo
        .query({
          query: gql`
            query CustomerExists($email: String!) {
              customerExists(email: $email)
            }
          `,
          variables: {
            email: this.account.email,
          },
        })
        .then((data) => {
          return data.data.customerExists;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  beforeCreate() {
    this.$store.dispatch("resetUserData");
  },
};
</script>