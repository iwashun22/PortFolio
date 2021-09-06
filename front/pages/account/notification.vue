<template>
  <h1>通知受け取り admin page</h1>
</template>

<script>
export default {
  layout: 'admin',
  middleware ({ store, redirect }) {
    if (!store.state.auth.loggedIn) {
      return redirect('/admin/login')
    }
  },
  data () {
    return {
    }
  }
}
</script>
