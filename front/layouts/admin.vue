<template>
  <v-app dark>
    <v-app-bar
      fixed
      dark
      height="68"
      class="top-nav"
    >
      <v-toolbar-title>
        <NuxtLink to="/admin/">
          管理者ページ
        </NuxtLink>
      </v-toolbar-title>
      <v-spacer />
      <v-app-bar-nav-icon
        @click="drawer = true"
      />
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      right
      temporary
      width="80vw"
      dark
    >
      <v-list
        nav
      >
        <v-list-item-group
          v-for="(item, i) in links"
          :key="i"
        >
          <v-list-item
            :to="item.to"
          >
            <v-list-item-icon>
              <v-icon>
                {{ item.icon }}
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>
                {{ item.text }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-navigation-drawer
      class="left-nav"
      expand-on-hover
      permanent
      fixed
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group>
          <v-list-item
            class="px-2"
            to="/"
          >
            <v-icon
              size="42"
              mt="6"
            >
              mdi-account
            </v-icon>
          </v-list-item>

          <v-list-item
            to="/account/settings"
          >
            <v-list-item-content>
              <v-list-item-title class="text-h6">
                {{ $auth.user.username }}
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ $auth.user.email }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <v-list
        nav
        dense
      >
        <v-list-item-group
          no-action
        >
          <v-list-item
            v-for="(link, ilink) in links"
            :key="ilink"
            :to="link.to"
          >
            <v-list-item-icon>
              <v-icon>
                {{ link.icon }}
              </v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              {{ link.text }}
            </v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <div class="main">
      <Nuxt />
    </div>
  </v-app>
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
      drawer: false,
      links: [
        {
          icon: 'mdi-view-dashboard',
          text: 'ダッシュボード',
          to: '/admin'
        },
        {
          icon: 'mdi-fountain-pen',
          text: 'ブログを投稿',
          to: '/blog/admin'
        },
        {
          icon: 'mdi-account-box',
          text: 'キャリアを投稿',
          to: '/career/admin'
        },
        {
          icon: 'mdi-card-account-details',
          text: 'スキルを投稿',
          to: '/skills/admin'
        },
        {
          icon: 'mdi-star',
          text: '制作物を投稿',
          to: '/created/admin'
        },
        {
          icon: 'mdi-bell-ring',
          text: 'お知らせ作成',
          to: '/notification/admin'
        },
        {
          icon: 'mdi-alert-circle',
          text: 'お問い合わせ',
          to: '/contact/admin'
        },
        {
          icon: 'mdi-keyboard-backspace',
          text: '管理画面を出る',
          to: '/'
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
#__layout {
  margin: 0 !important;
}

.top-nav {
  display: none;
}

.main {
  margin: 0 0 0 56px;
  min-height: 100vh;
}

.v-navigation-drawer__content {
  .v-list {
    &-item {
      padding: 0 8px !important;
      margin: 5px 8px;
      justify-content: center !important;

      &--active {
        * {
          font-weight: bolder;
        }
      }

      &__icon {
        margin-right: 0 !important;
      }
    }
  }
}

@media screen and (max-width: 1080px) {
  .main {
    margin: 68px 0 0 0 !important;
    min-height: calc(100vh - 68px);
  }

  .top-nav {
    display: block !important;
  }

  .left-nav {
    display: none;
  }
}
</style>
