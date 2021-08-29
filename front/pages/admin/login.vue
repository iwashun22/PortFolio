<template>
  <div class="login-case">
    <v-card
      flat
      dark
    >
      <v-card-title>
        <v-icon
          size="32"
        >
          mdi-account-cog
        </v-icon>
        <h4 class="fill-width">
          管理画面にログイン
        </h4>
      </v-card-title>
      <v-row>
        <v-col
          cols="10"
        >
          <v-text-field
            v-model="form.username"
            outlined
            prepend-inner-icon="mdi-email"
            placeholder="example@example.com"
            autocomplete="off"
            autofocus
            required
          />
        </v-col>
        <v-col
          cols="10"
        >
          <v-text-field
            v-model="form.password"
            :append-icon="form.passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
            :type="form.passwordShow ? 'text' : 'password'"
            outlined
            prepend-inner-icon="mdi-lock"
            placeholder="パスワード"
            autofocus
            autocomplete="off"
            required
            @click:append="form.passwordShow = !form.passwordShow"
          />
        </v-col>
        <v-col
          cols="10"
          class="login-btn"
        >
          <v-btn
            tile
            block
            x-large
            color="primary"
          >
            ログイン
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script>
export default {
  middleware ({ store, redirect }) {
    if (store.state.auth.loggedIn) {
      return redirect('/admin')
    }
  },
  data () {
    return {
      form: {
        username: '',
        password: '',
        passwordShow: false
      }
    }
  },
  head: {
    title: 'ログイン'
  },
  methods: {
    async loginUser () {
      await this.$auth.loginWith('local', {
        data: {
          username: this.form.username,
          password: this.form.password
        }
      }).then(() => {
        location.reload()
      }).catch(() => {
        location.reload()
        this.$auth.logout()
      })
    }
  }
}
</script>

<style lang="scss">
#__layout {
  margin-top: 68px;
}

.login-case {
  max-width: 500px;
  width: 100%;
  height: initial !important;
  display: flex;
  margin: 120px auto;

  .v-card {
    width: 100%;
    display: flex;
    margin: 0 auto;
    padding: 30px 0 60px 0;
    max-width: 520px;
    flex-direction: column;

    .row {
      justify-content: center;
    }

    .col {
      padding: 0 12px;
    }

    .login-btn {
      .v-btn {
        background-color: #1976d2 !important;
      }
    }

    .v-card__title {
      justify-content: center;
      padding: 28px 0 60px 0;
      font-size: 24px;
      color: #eee;

      i {
        margin: 10px 10px;
      }
    }

    .v-input {
      .v-input__control {
        .v-input__slot {
          .primary--text {
            color: #1976d2 !important;
          }

          .v-input__prepend-inner {
            margin: auto 10px auto 0;
          }
        }
      }
    }
  }
}
</style>
