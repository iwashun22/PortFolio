<template>
  <div class="case">
    <Career />
  </div>
</template>

<script>
import Career from '~/components/career.vue'

export default {
  components: {
    Career
  },
  head: {
    title: 'キャリア'
  }
}
</script>

<style lang="scss">
.case {
  margin-top: 68px;
}
</style>
