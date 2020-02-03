import ScantrustService from '@/services/ScantrustService'
import BlockchainService from '@/services/BlockchainService'
import * as types from '../mutations'

const state = {
  code: {},
  scan: {},
  campaign: {},
  smartlabel: {
    data: []
  },
  loaded: false,
  apiKey: '',
  uid: '',
  qr: '',
  cambioBlockchainData: {},
  userPosition: {}
}

const getters = {
  scan: state => state.scan,
  code: state => state.code,
  uid: state => state.uid,
  qr: state => state.qr,
  smartlabel: state => state.smartlabel,
  isLoaded: state => state.loaded,
  cambioBlockchainData: state => state.cambioBlockchainData,
  userPosition: state => state.userPosition,
  updated_at: state => state.smartlabel.updated_at,

  scanResult: (state) => {
    if (state.code.qrcode.activation_status === 'inactive' || state.code.qrcode.is_blacklisted || (state.scan.reason === 'auth' && state.scan.result !== 'ok')) {
      return 'counterfeit'
    } else if (state.scan.reason === 'auth' && state.scan.result === 'ok') {
      return 'genuine'
    } else {
      return 'verified'
    }
  },

  getSmartlabelConfig: (state) => {
    if (state.smartlabel.config) {
      return state.smartlabel.config
    } else {
      return {}
    }
  },

  getUrlParameters: (state) => {
    return {uid: state.uid, qr: state.qr, apiKey: state.apiKey}
  },

  getSmartLabelTab: (state, getters) => (key) => {
    return JSON.parse(JSON.stringify(getters.smartlabel.data.find(obj => obj.key === key)))
  },

  getMainSections: (state, getters) => {
    let tabs = []
    getters.smartlabel.data.forEach(function (tab) {
      if (tab.is_enabled === true) {
        tabs.push(tab.key)
      }
    })

    let main = tabs.slice(0, 4)

    if (tabs.length > 5) {
      main.push('more')
    }

    return main
  },

  getMoreSection: (state, getters) => {
    let tabs = []

    getters.smartlabel.data.forEach((tab) => {
      if (tab.is_enabled === true) {
        tabs.push(tab.key)
      }
    })

    let more = tabs.slice(4)

    return more
  },

  getNutrient: (state, getters) => (key) => {
    let item = {}

    getters.getSmartLabelTab('nutrition').data.table.forEach((obj) => {
      if (obj.key === key) {
        item = obj
      } else if (obj.children) {
        obj.children.forEach((child) => {
          if (child.key === key) {
            item = child
          }
        })
      }
    })

    if (!item) {
      item = {serving: 'N/A', key: key, name: key}
    }

    return JSON.parse(JSON.stringify(item))
  }
}

const actions = {

  saveUrlParameters ({ commit }, { uid, qr, apiKey }) {
    commit(types.SAVE_URL_PARAMETERS, { uid, qr, apiKey })
  },

  getCombinedInfos ({ commit, getters }, { uid, hasBlockchain }) {
    return new Promise((resolve, reject) => {
      ScantrustService.getCombinedInfos(uid).then((combinedInfos) => {
        commit(types.LOAD_SCAN_DATA, { scan: combinedInfos.scan })
        commit(types.LOAD_CODE_DATA, { code: combinedInfos.code })
        commit(types.LOAD_CAMPAIGN_DATA, { campaign: combinedInfos.campaign })
        commit(types.LOAD_SMARTLABEL_DATA, { smartlabel: combinedInfos.smartlabel })
        if (!~getters.getMainSections.indexOf('blockchain-cambio')) {
          commit(types.DATA_LOADED)
        }

        resolve(combinedInfos.code, combinedInfos.smartlabel.theme)
      })
    }).catch((err) => {
      console.log('error fetching data' + err)
    })
  },

  getScanData ({ commit }, { uid }) {
    ScantrustService.getScanInfos(uid).then((scan) => {
      commit(types.LOAD_SCAN_DATA, { scan })
    })
  },

  getCodeData ({ commit }, { qr }) {
    ScantrustService.getCodeInfos(qr).then((code) => {
      commit(types.LOAD_CODE_DATA, { code })
    })
  },

  getCampaignData ({ commit }) {
    ScantrustService.getCampaignInfos().then((campaign) => {
      commit(types.LOAD_CAMPAIGN_DATA, { campaign })
    })
  },

  getBlockchainInfos ({ commit }, roastId) {
    commit(types.LOADING_DATA)
    BlockchainService.getBlockchainCambioInfos(roastId).then((data) => {
      commit(types.LOAD_BLOCKCHAIN_CAMBIO_DATA, {blockchainData: data})
    })
  },

  sendScanPosition ({ commit, getters }, { position, uid }) {
    ScantrustService.sendScanPosition({ position, uid })
    commit(types.SET_USER_POSITION, { lat: position.coords.latitude, lng: position.coords.longitude })
  }
}

const mutations = {

  [types.LOADING_DATA] (state) {
    state.loaded = false
  },

  [types.DATA_LOADED] (state) {
    state.loaded = true
  },

  [types.SET_USER_POSITION] (state, {lat, lng}) {
    state.userPosition.lat = lat
    state.userPosition.lng = lng
  },

  [types.LOAD_SCAN_DATA] (state, { scan }) {
    state.scan = { ...scan }
  },

  [types.LOAD_SMARTLABEL_DATA] (state, { smartlabel }) {
    state.smartlabel = { ...smartlabel }
  },

  [types.LOAD_CODE_DATA] (state, { code }) {
    state.code = { ...code }
  },

  [types.SAVE_URL_PARAMETERS] (state, { uid, qr, apiKey }) {
    state.uid = uid
    state.qr = qr
    state.apiKey = apiKey
  },

  [types.LOAD_CAMPAIGN_DATA] (state, { campaign }) {
    state.campaign = { ...campaign }
  },

  [types.LOAD_BLOCKCHAIN_CAMBIO_DATA] (state, { blockchainData }) {
    state.cambioBlockchainData = { ...blockchainData }
    state.loaded = true
  }

}

export default {
  state,
  getters,
  actions,
  mutations
}
