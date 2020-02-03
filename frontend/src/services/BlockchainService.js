// ST Enpoint calls

import axios from 'axios'
import Api from '../api.js'

var Promise = require('promise-polyfill')

var cambioAxios = axios.create({
  baseURL: Api.cambio_config.API_BASE_URL
})

export default {
  getBlockchainCambioInfos: function (roastId) {
    return new Promise(function (resolve, reject) {
      cambioAxios.get(`roasts/${roastId}/`).then((res) => {
        resolve(res.data)
      }).catch((error) => {
        reject(error.response)
      })
    })
  }
}
