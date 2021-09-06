<template>
  <div class="case">
    <div class="h-space" />
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
.h-space {
  height: 68px;
  width: 100%;
}
</style>
