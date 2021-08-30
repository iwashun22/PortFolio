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
          pb="3"
        >
          <v-alert
            dismissible
            type="error"
            elevation="3"
          >
            管理者ページ
          </v-alert>
        </v-col>
        <v-col
          cols="10"
        >
          <v-text-field
            v-model="form.username"
            :rules="[rules.required]"
            hint="メール"
            prepend-inner-icon="mdi-email"
            placeholder="example@example.com"
            autocomplete="off"
            autofocus
            required
            outlined
          />
        </v-col>
        <v-col
          cols="10"
        >
          <v-text-field
            v-model="form.password"
            :append-icon="form.passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
            :type="form.passwordShow ? 'text' : 'password'"
            :prepend-inner-icon=" form.focus ? 'mdi-lock-open' : 'mdi-lock'"
            :rules="[rules.required]"
            hint="パスワード"
            outlined
            placeholder="パスワード"
            autocomplete="off"
            required
            @focus="form.focus = true"
            @blur="form.focus = false"
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
            @click="loginUser"
          >
            ログイン
          </v-btn>
        </v-col>
        <v-col
          cols="10"
          class="divider"
        >
          <p
            @click="snackbar = true"
          >
            これはなんですか？
          </p>
        </v-col>
      </v-row>
    </v-card>
    <v-snackbar
      v-model="snackbar"
    >
      これは管理の画面にためのログイン画面です<br>
      <b>登録はできません</b><br>
      何かあれば
      <Nuxt-Link to="/contact/">
        お問い合わせ
      </Nuxt-Link>
      ください

      <template
        #action="{ attrs }"
      >
        <v-btn
          text
          v-bind="attrs"
          class="snackbar-btn"
          @click="snackbar = false"
        >
          閉じる
        </v-btn>
      </template>
    </v-snackbar>
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
        passwordShow: false,
        focus: false
      },
      rules: {
        required: value => !!value || '必須項目です'
      },
      snackbar: false
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
    padding: 30px 0 40px 0;
    max-width: 520px;
    flex-direction: column;

    .row {
      justify-content: center;
      width: 100% !important;
      margin: 0 auto;
      max-width: 500px;
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

    .v-alert {
      background-color: #dd2c00 !important;
      margin: 30px 0;

      .v-alert__wrapper {
        align-items: center;
        border-radius: inherit;
        display: flex;

        .mdi-alert {
          margin-right: 20px;
        }

        .v-alert__content {
          flex: 1 1 auto;
        }
      }
    }

    .v-input {
      .v-input__control {
        .v-input__slot {
          color: #1976d2;

          .primary--text.mdi-email,
          .primary--text.mdi-lock,
          .primary--text.mdi-lock-open {
            color: #1976d2 !important;
          }

          .v-input__prepend-inner {
            margin: auto 10px auto 0;
          }
        }
      }
    }

    .error--text.mdi-lock,
    .error--text.mdi-lock-open,
    .error--text.mdi-email {
      color: #dd2c00 !important;
    }

    .v-snack__wrapper {
      padding: 20px !important;

      .snackbar-btn {
        padding-right: 10px;
      }
    }

    .divider {
      margin-top: 15px;
      font-size: 80%;
      color: #ddd;
      cursor: pointer;

      &:hover {
        color: white;
      }
    }
  }

  .v-snack__action {
    padding-right: 10px;
  }
}

@media screen and (max-width: 580px) {
  .login-case {
    margin-top: 78px !important;
  }
}
</style>
