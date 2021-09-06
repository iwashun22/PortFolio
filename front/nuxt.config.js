import colors from 'vuetify/es5/util/colors'

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '広瀬エイトル - %s',
    title: 'Main',
    htmlAttrs: {
      lang: 'ja'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@mdi/font/css/materialdesignicons.css',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~plugins/particles.js', ssr: false }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/toast',
    ['nuxt-log', {
      // optional : defaults to true if not specified
      isEnabled: true,
      // required ['debug', 'info', 'warn', 'error', 'fatal']
      logLevel: 'debug',
      // optional : defaults to false if not specified
      stringifyArguments: false,
      // optional : defaults to false if not specified
      showLogLevel: false,
      // optional : defaults to false if not specified
      showMethodName: false,
      // optional : defaults to '|' if not specified
      separator: '|',
      // optional : defaults to false if not specified
      showConsoleColors: false
    }]
  ],

  toast: {
    // 右上にtoastを表示
    position: 'top-right',
    // 特に指定しなくても5秒で消えるように設定
    duration: 5000
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: process.env.API_URL,
  },

  auth: {
    redirect: {
      login: '/admin/admin',
      logout: '/admin/login',
      callback: false,
      home: false
    },
    user: {
      property: 'username',
    },
    localStorage: false,
    refreshToken: {
      property: 'refresh_token',
      data: 'refresh_token',
      maxAge: 60 * 60 * 24 * 1
    },
    strategies: {
      local: {
        token: {
          required: true,
          type: " Token "
        },
        endpoints: {
          login: { url: 'api/login/', method: 'post', propertyName: 'token' },
          user: { url: '/api/me/', method: 'get', propertyName: 'user' },
          logout: false
        }
      }
    }
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
