<template>
  <div class="login-case">
    <v-card
      tile
      dark
      width="100%"
      max-width="520"
    >
      <v-card-title>
        Login
      </v-card-title>
      <div class="login-inner">
        <v-container>
          <v-row>
            <v-col
              cols="12"
              sm="12"
              class="pm"
            >
              <v-text-field
                v-model="form.username"
                solo
                label="E-mail"
                click:clear
                prepend-icon="mdi-email"
              />
              <v-text-field
                v-model="form.password"
                :append-icon="form.show ? 'mdi-eye' : 'mdi-eye-off'"
                solo
                :type="form.show ? 'text' : 'password'"
                click:clear
                label="Password"
                prepend-icon="mdi-lock"
                @click:append="form.show = !form.show"
              />
            </v-col>
            <v-col
              cols="12"
              sm="12"
            >
              <v-btn
                elevation="5"
                large
                x-large
                color="success"
                class="btn"
                @click="loginUser"
              >
                ログイン
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </div>
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
        show: false
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
        this.$toast.success('Logged In!')
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
  display: flex;

  .v-card {
    margin: 60px auto calc((100vh - 450px) / 4) auto;
    display: flex;
    flex-direction: column;
    background-color: #000;

    .v-card__title {
      justify-content: center;
      text-align: center;
      width: fit-content;
      font-size: 38px;
      font-weight: bolder;
      margin: 25px auto;
      padding: 0;
    }

    .row {
      justify-content: center;

      .btn {
        margin: 5px 0;
      }
    }

    .pm {
      padding: 0 20px !important;
    }

    .login-inner {
      position: relative;
    }

    .v-input {
      .v-input__control {
        margin: 0 20px;
      }
    }
  }
}
</style>
