<template>
  <div class="promotion">
    This is the promotion page, would be amazing if it worked
  </div>
</template>

<script>

import { mapGetters } from 'vuex'

export default {
  name: 'promotion',
  computed: mapGetters(['getSmartLabelTab']),
  data () {
    return {
    }
  },
  methods: {
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

@import "../../variables.scss";

</style>
