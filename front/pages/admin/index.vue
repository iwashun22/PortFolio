<template>
  <v-alert
    type="error"
    elevation="3"
  >
    管理者ページ
  </v-alert>
</template>

<script>
export default {
  layout: 'admin',
  middleware ({ store, redirect }) {
    if (!store.state.auth.loggedIn) {
      return redirect('/admin/login')
    }
  }
}
</script>
