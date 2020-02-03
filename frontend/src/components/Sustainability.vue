<template>
  <div class="sustainability flex flex-vertical flex-space-between">
    <div class="flex-1">
      <div class="disclaimer roboto">
        <span>
          We believe sustainability is very important to us all.
          <br><br>
          We work hard to ensure our products and packaging meet the standards of Sustainable Development.
        </span>
      </div>
      <list :items="this.getSmartLabelTab('sustainability').data.items"></list>
    </div>
    <app-footer v-if="!hideFooter"></app-footer>
  </div>
</template>

<script>

import Footer from '@/components/ui/Footer'
import List from '@/components/ui/List'
import { mapGetters } from 'vuex'

export default {
  name: 'sustainability',
  props: ['hideFooter'],
  computed: mapGetters(['getSmartLabelTab']),
  data () {
    return {}
  },
  components: {
    'app-footer': Footer,
    'list': List
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.sustainability{
  height: 100%;
}

.disclaimer{
  color: #999;
  font-size: calc(12px + 1vw);
  padding: 17px;
}

</style>
