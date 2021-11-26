import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    theme: 'light',
    userData: {
      isLoggedIn: false,
      userType: '',
      authToken: '',
      account: {
        id: 0,
        email: '',
        image: '',
        name: '',
        phone: '',
        dateOfBirth: '',
        created: ''
      },
      seller: {
        id: 0,
        paymentID: '',
        billing: '',
        revenue: 0
      },
      customer: {
        id: 0,
        credit: 0
      }
    }
  },
  getters: {
    getTheme: state => {
      return state.theme
    },
    getUserData: state => {
      return state.userData
    }
  },
  mutations: {
    LOAD_DATA(state) {
      const theme = localStorage.theme
      const userData = localStorage.userData
      if (theme != null) {
        state.theme = theme
      }
      if (userData != null) {
        state.userData = JSON.parse(userData)
      }
    },
    SET_USER_DATA(state, userData) {
      state.userData = userData
    },
    SET_USER_IMAGE(state, image) {
      state.userData.account.image = image
    },
    SAVE_USER_DATA(state) {
      localStorage.userData = JSON.stringify(state.userData)
    },
    SET_CUSTOMER_CREDIT(state, credit) {
      state.userData.customer.credit = credit
    },
    SET_THEME(state, theme) {
      state.theme = theme
    },
    SAVE_THEME(state) {
      localStorage.theme = state.theme
    },
    RESET_USER_DATA(state) {
      state.userData = {
        isLoggedIn: false,
        userType: '',
        authToken: '',
        account: {
          id: 0,
          email: '',
          image: '',
          name: '',
          phone: '',
          dateOfBirth: '',
          created: ''
        },
        seller: {
          id: 0,
          paymentID: '',
          billing: '',
          revenue: 0
        },
        customer: {
          id: 0,
          credit: 0
        }
      }
    }
  },
  actions: {
    loadData({
      commit
    }) {
      commit('LOAD_DATA')
    },
    setTheme({
      commit
    }, {
      theme
    }) {
      commit('SET_THEME', theme)
      commit('SAVE_THEME')
    },
    setUserData({
      commit
    }, {
      userData
    }) {
      commit('SET_USER_DATA', userData)
      commit('SAVE_USER_DATA')
    },
    setUserImage({
      commit
    }, {
      image
    }) {
      commit('SET_USER_IMAGE', image)
      commit('SAVE_USER_DATA')
    },
    setCustomerCredit({
      commit
    }, {
      credit
    }) {
      commit('SET_CUSTOMER_CREDIT', credit)
      commit('SAVE_USER_DATA')
    },
    resetUserData({
      commit
    }) {
      commit('RESET_USER_DATA')
      commit('SAVE_USER_DATA')
    }
  }
})