<template>
  <h1>Dashboard</h1>
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
