<template>
  <div class="product-infos flex flex-vertical flex-space-between">
    <div class="product-image flex-1 img-ctn" v-bind:style="{ 'background-image' : 'url(' + code.product.image + ')' }">
      <!-- <img class="product-image" v-bind:src="product.images['1']" alt=""> -->
    </div>

    <div class="infos-ctn">
      <div v-if="!getSmartlabelConfig.enable_authentication" class="brand roboto-medium">
        {{code.brand.name}}
      </div>

      <div v-if="getSmartlabelConfig.enable_authentication" class="authentication-result roboto-medium" v-bind:class="scanResult">
        <span v-if="scanResult === 'genuine'">Genuine</span>
        <span v-if="scanResult === 'verified'">Active Code</span>
        <span v-if="scanResult === 'counterfeit'">Suspected Counterfeit</span>
      </div>

      <div class="Grid -middle">
        <div class="Cell -fill product-name roboto">
          {{code.product.name}}
        </div>
        <div v-if="typeof this.getSmartLabelTab('nutrition').data.serving.weight != 'undefined' " class="Cell weight-infos roboto-light">
          <div>net.</div>
          <div class="number">{{this.getSmartLabelTab('nutrition').data.serving.weight}}</div>
        </div>
      </div>

      <div class="serial roboto">
        SN - {{code.qrcode.serial_number}}
      </div>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Config from '@/config'

export default {
  name: 'product-infos',
  computed: {
    ...mapGetters(['getSmartLabelTab', 'code', 'scanResult', 'getSmartlabelConfig'])
  },
  data () {
    return {
      config: Config
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.product-infos{
  padding: 15px 0px;
  height: calc(100% - 128px);
}

.weight-infos{
  border-left: 1px solid #bbbbbb;
  padding: 3px 10px;
  color: #bbbbbb;
  font-size: 1.2rem;
}

.serial{
  color: #999;
  font-size: calc(9px + 1vw);
  margin-left: 10px;
}

.weight-infos .number{
  font-size: calc(12px + 1vw);
}

.product-image{
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center center;
  /*max-height: 70%;*/
}

.product-name{
  font-size: calc(16px + 1vw);
  color: black;
  margin-left: 10px;
}

.authentication-result{
  margin-left: 10px;
  margin-top: 10px;
  font-size: calc(20px + 1vw);
  border-left: 5px solid var(--primary);
  padding-left: 5px;
}

.brand{
  margin-left: 10px;
  margin-top: 10px;
  font-size: calc(14px + 1vw);
  border-left: 5px solid var(--primary);
  color: var(--primary);
  padding-left: 5px;
}

.genuine {
  color: #7bc24e;
  border-color: #7bc24e;
}
.verified {
  border-color: #00a8e2;
  color: #00a8e2;
}
.counterfeit {
  color: #f43838;
  border-color: #f43838;
}

</style>
