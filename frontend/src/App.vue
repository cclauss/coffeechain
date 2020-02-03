<template>
  <div class="app-wrap" id="app">
    <loading v-if="!loaded"></loading>
    <img v-if="loaded" class="top-logo" src="./assets/smartlabel-logo.png" alt="">
    <product-infos v-if="loaded"></product-infos>
    <navigation v-if="loaded"></navigation>
    <router-view v-if="loaded"></router-view>
  </div>
</template>

<script>

import Loading from '@/components/ui/Loading'
import Navigation from '@/components/ui/Navigation'
import ProductInfos from '@/components/ProductInfos'
import ScantrustService from '@/services/ScantrustService'

import { mapGetters } from 'vuex'

export default {
  name: 'app',
  components: {
    'navigation': Navigation,
    'product-infos': ProductInfos,
    'loading': Loading
  },
  data () {
    return {
      campaign: {},
      scanId: ''
    }
  },

  methods: {
    positionSuccess: function (pos) {
      this.$store.dispatch('sendScanPosition', {position: pos, uid: this.$route.query.uid})
    },

    positionError: function () {
      console.log('error fetching position :( ')
    },

    getUserPosition: function () {
      navigator.geolocation.getCurrentPosition(this.positionSuccess, this.positionError, {enableHighAccuracy: false, timeout: 5000})
    }
  },

  computed: mapGetters({
    loaded: 'isLoaded',
    sections: 'getMainSections'
  }),

  created () {
    this.getUserPosition()

    if (this.$route.query.api_key) {
      ScantrustService.setAuthorizationHeader(this.$route.query.api_key)
    }

    this.$store.dispatch('saveUrlParameters', {qr: this.$route.query.qr, uid: this.$route.query.uid, apiKey: this.$route.query.api_key})
    this.$store.dispatch('getCombinedInfos', {uid: this.$route.query.uid}).then((code, theme) => {
      if (~this.sections.indexOf('blockchain-cambio')) {
        let roastId
        code.scm_data.forEach((scm) => {
          if (scm.key === 'roasting_id') {
            roastId = scm.value
          }
        })
        this.$store.dispatch('getBlockchainInfos', roastId || 'SH-20180507')
      }

      // Set Theme Colors
      if (theme) {
        const body = document.querySelector('body')

        if (theme.primary) {
          body.style.setProperty('--primary', theme.primary)
        }
        if (theme.accent) {
          body.style.setProperty('--accent', theme.accent)
        }
      }
    })
  },

  beforeMount () {
    if (!this.$route.query.uid) {
      alert('Incorrect URL')
    }
  }
}
</script>

<style lang="scss">

@import "./global.scss";

html {
  font-size: 62.5%;
  height: 100%;
  width: 100%;
}

body {
  height: 100%;
  width: 100%;
  max-width: 500px;
  margin: 0;
  margin-left: auto;
  margin-right: auto;
}

#app {
  height: 100%;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.top-logo{
  padding-top: 15px;
  width: 119px;
  margin-left: 1rem;
}

</style>
