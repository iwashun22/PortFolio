<template>
  <div>
    <div id="background" class="background" />
    <div class="background-inner">
      <div class="myinfo-case">
        <div class="img" />
        <h2>広瀬 エイトル</h2>
        <div class="icons">
          <v-btn
            v-for="link in links"
            :key="link.icon"
            class="mx-4 white--text"
            icon
          >
            <a :href="link.to" target="_blank" rel="noopener noreferrer">
              <v-icon
                size="32px"
              >
                {{ link.icon }}
              </v-icon>
            </a>
          </v-btn>
        </div>
      </div>
    </div>
    <About />
    <Career />
    <Skills />
  </div>
</template>

<script>
import bubble from '~/assets/js/particles/bubble.js'
import About from '~/components/about-me.vue'
import Career from '~/components/career.vue'
import Skills from '~/components/skills.vue'

if (process.client) {
  require('particles.js')
}

export default {
  components: {
    About,
    Career,
    Skills
  },
  data () {
    return {
      links: [
        {
          icon: 'mdi-email',
          to: 'mailto:Heitorhirose@gmail.com'
        },
        {
          icon: 'mdi-twitter',
          to: 'https://twitter.com/Heitor_Hirose'
        },
        {
          icon: 'mdi-instagram',
          to: 'https://www.instagram.com/hirose_heitor/'
        },
        {
          icon: 'mdi-github',
          to: 'https://github.com/HEKUCHAN'
        }
      ]
    }
  },
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
    ]
  },
  mounted () {
    window.particlesJS('background', bubble.data)
  }
}
</script>

<style lang="scss">
#background {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100%;
  z-index: 1;
  background-color: #393e46;
}

.icons {
  width: 60%;
  height: 60px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;

  .v-btn {
    .v-btn__content {
      a {
        color: white;
      }
    }
  }
}

.background-inner {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  .myinfo-case {
    width: 340px;
    height: 550px;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;

    * {
      z-index: 2;
      user-select: none;
    }

    .img {
      width: 240px !important;
      height: 240px !important;
      background-image: url(~static/icon.png);
      background-size: cover;
      background-position: center center;
      border-radius: 50%;
    }

    h2 {
      text-align: center;
      font-weight: lighter;
      font-weight: bold;
      color: white;
      margin-top: 20px;
      font-size: 28px;
    }
  }
}

@media screen and (max-width: 580px) {
  .background-inner {
    .myinfo-case {
      width: 280px;
      height: 550px;

      .img {
        width: 180px !important;
        height: 180px !important;
      }
    }
  }

  .icons {
    width: 100%;
    height: 50px;
    display: flex;
    justify-content: space-evenly;
    align-self: center;

    img {
      height: 42px;
      width: 42px;
    }
  }
}
</style>
