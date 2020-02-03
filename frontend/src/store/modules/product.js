import TradeshiftService from '@/services/TradeshiftService'
import * as types from '../mutations'

const state = {
  data: {},
  loaded: false
}

const getters = {
  product: state => state.data
}

const actions = {

  getProductData ({ commit }) {
    TradeshiftService.fetchTradeShiftInfos().then((product) => {
      commit(types.LOAD_PRODUCT_DATA, { product })
    })
  }
}

const mutations = {

  [types.LOAD_PRODUCT_DATA] (state, { product }) {
    state.data = { ...product }
    state = { ...state, loaded: true }
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
