import Vue from 'vue'
import Vuex from 'vuex'
import scantrust from './modules/scantrust'
import product from './modules/product'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    scantrust,
    product
  },
  strict: debug
})
