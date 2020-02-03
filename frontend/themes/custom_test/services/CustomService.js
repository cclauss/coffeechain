// ST Enpoint calls

import axios from 'axios'
import Api from '../api.js'

var Promise = require('promise-polyfill')

var cambioAxios = axios.create({
  baseURL: Api.cambio_config.API_BASE_URL
})

export default {
  loadPromotions: function (roastId) {
    return new Promise(function (resolve, reject) {
      setTimeout(() => {
        resolve('hello')
      }, 2000)
    })
  }
}
