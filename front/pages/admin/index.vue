<template>
  <h1>The login Success</h1>
</template>

<script>
export default {
  middleware ({ store, redirect }) {
    if (!store.state.auth.loggedIn) {
      return redirect('/admin/login')
    }
  }
}
</script>
