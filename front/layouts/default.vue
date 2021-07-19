<template>
  <div>
    <v-app-bar
      fixed
      app
      dark
      height="68"
    >
      <v-toolbar-title>
        <a href="/">広瀬 エイトル</a>
      </v-toolbar-title>
      <v-spacer />
      <v-btn
        icon
        class="counter-btn"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <p class="counter">
        2302
      </p>
      <v-app-bar-nav-icon
        @click="drawer = true"
      />
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      right
      dark
      temporary
      width="60vw"
    >
      <v-list flat>
        <v-list-item-group
          v-model="selectedItem"
        >
          <template
            v-for="(item, i) in items"
          >
            <a
              v-if="i == 0"
              :key="i"
              href="/"
            >
              <v-list-item
                @click="selectedItem = i"
              >
                <v-list-item-icon>
                  <v-icon v-text="item.icon" />
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="item.text" />
                </v-list-item-content>
              </v-list-item>
            </a>
            <v-list-item
              v-else
              :key="i"
              :to="item.to"
              @click="selectedItem = i"
            >
              <v-list-item-icon>
                <v-icon v-text="item.icon" />
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title v-text="item.text" />
              </v-list-item-content>
            </v-list-item>
            <v-divider v-if="i !== items.length - 1" :key="i" />
          </template>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <Nuxt />
  </div>
</template>

<script>
export default {
  data: () => ({
    drawer: false,
    selectedItem: 0,
    items: [
      {
        icon: 'mdi-account-box',
        text: 'メインページ',
        to: '/'
      },
      {
        icon: 'mdi-star',
        text: 'Star',
        to: '/blog'
      },
      {
        icon: 'mdi-send',
        text: 'Send',
        to: '/blog'
      },
      {
        icon: 'mdi-email-open',
        text: 'Drafts',
        to: '/blog'
      }
    ]
  })
}
</script>

<style lang="scss">

// ::-webkit-scrollbar {
//   width: 13px;
//   background-color: #393e46;
// }

// ::-webkit-scrollbar-thumb {
//   background-color: #00adb5;
// }

body {
  background-color: #393e46;
}

a {
  &:visited {
    color: #eee;
    text-decoration: none;
  }

  &:link {
    color: #eee;
    text-decoration: none;
  }

  &:hover {
    color: #eee;
    text-decoration: none;
  }
}

header {
  z-index: 99;
}

#background {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100%;
  background: #393e46;
}

.v-toolbar__title {
  font-weight: bolder;
  user-select: none;
  padding: 0 30px;
}

.counter {
  margin-right: 30px;
}

.v-navigation-drawer {
  max-width: 300px;

  .v-list {
    padding: 0;

    .v-list-item {
      align-items: center;
      justify-content: space-between;
      text-align: center;
    }
  }
}

@media screen and (max-width: 580px) {
  header {
    .counter,
    .counter-btn {
      display: none;
    }
  }
}
</style>
