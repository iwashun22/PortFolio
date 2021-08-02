<template>
  <div>
    <div id="background" class="background" />
    <div class="background-inner">
      <div class="myinfo-case">
        <div class="img" />
        <h1>広瀬 エイトル</h1>
        <div class="icons">
          <a href="">
            <img src="~/static/sns/github.svg" alt="">
          </a>
          <a href="">
            <img src="~/static/sns/instagram.png" alt="">
          </a>
          <a href="">
            <img src="~/static/sns/mail.svg" alt="">
          </a>
          <a href="">
            <img src="~/static/sns/twitter.svg" alt="">
          </a>
          <a href="">
            <img src="~/static/sns/wantedly.svg" alt="">
          </a>
        </div>
      </div>
    </div>
    <div class="test" />
  </div>
</template>

<script>
import bubble from '~/assets/js/particles/bubble.js'

if (process.client) {
  require('particles.js')
}

export default {
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

.test {
  height: 1600px;
  width: 100%;
  margin-top: 100vh;
  background-color: #393e46;
}

#background {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100%;
  z-index: 1;
  background-color: #393e46;
}

.icons {
  width: 80%;
  height: 60px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;

  img {
    height: 48px;
    width: 48px;
    background-color: #eee;
    border-radius: 50%;
    object-fit: cover;
    display: block;
    margin: auto;
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

    h1 {
      text-align: center;
      font-weight: bolder;
      color: #eee;
      margin-top: 20px;
    }
  }
}

@media screen and (max-width: 580px) {
  .background-inner {
    .myinfo-case {
      width: 280px;
      height: 550px;

      .img {
        width: 240px !important;
        height: 240px !important;
      }
    }
  }

  .icons {
    width: 100%;
    height: 50px;
    display: flex;
    justify-content: space-between;
    align-self: center;

    img {
      height: 42px;
      width: 42px;
    }
  }
}
</style>
