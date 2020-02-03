<template>
  <div class="footer">
    <div class="updated-on roboto">
      Information updated on {{ formatDate(updated_at) }}
    </div>

    <div class="company-infos">
      by ScanTrust SA
    </div>

    <div class="Grid -between">
      <a class="" href="https://www.scantrust.com/privacy">Privacy Policy</a>
      <a href="#">Feedback for SmartLabel</a>
    </div>
  </div>
</template>

<script>

import { mapGetters } from 'vuex'

export default {
  name: 'appFooter',
  computed: mapGetters(['updated_at']),
  props: [],
  methods: {
    formatDate (string) {
      if (!string) {
        return
      }
      // 2019-03-21T08:37:29.730754Z

      let dateArray = string.split(/[^0-9]/)
      let date = new Date(dateArray[0], dateArray[1] - 1, dateArray[2], dateArray[3], dateArray[4], dateArray[5])
      let days = date.getDate() <= 9 ? '0' + date.getDate() : date.getDate()
      let months = date.getMonth() + 1 <= 9 ? '0' + (date.getMonth() + 1) : date.getMonth()
      return `${date.getFullYear()}-${months}-${days}`
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

@import "../../variables.scss";

.footer{
  margin-top: 25px;
  background: #fafafa;
  padding: 10px 30px;
  color: #333;
  border-bottom: 7px solid var(--accent);
  font-family: 'Roboto Light';
}

.updated-on{
  border-left: 10px solid #999;
  padding-left: 4px;
  font-size: calc(8px + 1vw);
}

.company-infos{
  padding: 10px 0px;
  font-size: calc(7px + 1vw);

}

a{
  font-size: calc(10px + 1vw);
  font-family: 'Roboto';
  color: var(--primary);
}

</style>
