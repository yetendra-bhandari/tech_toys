import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {
  ApolloClient
} from 'apollo-client'
import {
  createUploadLink
} from 'apollo-upload-client'
import {
  InMemoryCache
} from 'apollo-cache-inmemory'
import {
  setContext
} from "apollo-link-context";
import VueApollo from 'vue-apollo'

Vue.config.productionTip = false
const httpLink = createUploadLink({
  uri: process.env.VUE_APP_SERVER_URL + 'api/',
})

const cache = new InMemoryCache()

const authLink = setContext(() => {
  const token = store.getters.getUserData.authToken
  return {
    headers: {
      authorization: token ? `Bearer ${token}` : "",
    }
  }
});

const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache,
})

Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
})

new Vue({
  router,
  store,
  apolloProvider,
  render: h => h(App)
}).$mount('#app')