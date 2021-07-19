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
      <v-text-field
        v-if="$route.name == 'blog'"
        v-model="search"
        append-icon="mdi-magnify"
        label="記事を検索"
        single-line
        hide-details
        width="30vw"
        class="blog-search"
      />
      <v-btn
        icon
        class="counter-btn"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <p class="counter">
        0
      </p>
      <v-app-bar-nav-icon
        @click="drawer = true"
      />
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      right
      temporary
      width="60vw"
      dark
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
              <v-list-item>
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
        text: '制作物',
        to: '/created'
      },
      {
        icon: 'mdi-fountain-pen',
        text: 'ブログ',
        to: '/blog'
      },
      {
        icon: 'mdi-bell-ring',
        text: 'お知らせ',
        to: '/notification'
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

.blog-search {
  max-width: 280px;
  margin-right: 20px;
}

.v-navigation-drawer {
  max-width: 300px;
  border: none;
  box-shadow: none;
  background: #222 !important;

  .v-list {
    padding: 0;

    .v-list-item {
      align-items: center;
      justify-content: space-between;
      text-align: center;
    }

    .v-list-item__content,
    .v-list-item__icon {
      font-weight: bolder;
    }
  }
}

@media screen and (max-width: 850px) {
  .blog-search {
    display: none;
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
