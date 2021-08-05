<template>
  <div>
    <div id="background" class="background" />
    <div class="background-inner">
      <div class="myinfo-case">
        <div class="img" />
        <h2>広瀬 エイトル</h2>
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
    <div class="first-main case first-case">
      <h1 class="title">
        About Me
      </h1>
      <div class="aboutme-info-case">
        <div class="img" />
        <div class="msg">
          <p>テストストストテストストストテストストストテストストストテストストストテストストストテストストストテストストストテストストストテストストストテストストスト</p>
        </div>
      </div>
    </div>
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
.first-case {
  .aboutme-info-case {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;

    .msg {
      max-width: 300px;

      p {
        padding: 14px;
      }
    }

    .img {
      width: 240px !important;
      height: 240px !important;
      background-image: url(~static/icon.png);
      background-size: cover;
      background-position: center center;
      border-radius: 50%;
      margin: 30px 0;
    }
  }
}

.title {
  border-bottom: solid 3px white;
  width: fit-content;
  padding: 6px 20px;
  margin: 0 30px;
}

.first-main {
  width: 100%;
  height: 600px;
  background-color: #1e1e1e;
  margin: calc(100vh + 30px) auto 20px auto;
  max-width: 980px;
  border-radius: 0 !important;

  h1 {
    color: white;
  }
}

.case {
  display: flex;
  flex-direction: column;
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

    h2 {
      text-align: center;
      font-weight: lighter;
      color: #eee;
      margin-top: 20px;
      font-size: 28px;
    }
  }
}

@media screen and (max-width: 580px) {
  .aboutme-info-case {
    flex-direction: column !important;
    align-items: center;
    max-width: initial;

    .img {
      max-width: initial !important;
      margin: 30px auto !important;
    }

    .msg {
      width: 100%;
      max-width: 90vw !important;

      p {
        width: 100%;
        max-width: initial !important;
      }
    }
  }

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

  .title {
    font-size: 1.5rem;
    padding: 3px 10px;
    margin: 0 15px;
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
