<template>
  <div>
    <h1>TEST</h1>
  </div>
</template>

<script>
export default {
  data () {
    return {
      career: [],
      check: null,
      loading: true,
      err: null
    }
  },
  head: {
    title: 'キャリア'
  },
  async created () {
    this.career = await this.$axios.get(this.$axios.defaults.baseURL + `api/career/${this.$route.params.id}`)
      .catch((err) => {
        this.loading = false
        this.check = true
        this.err = err
      }).finally(() => {
        this.loading = false
        this.check = false
      })
  }
}
</script>

<style lang="scss">
#__layout {
  margin-top: 58px;
}
</style>
