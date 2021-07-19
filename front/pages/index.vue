<template>
  <div>
    <div id="background" class="background" />
    <div class="background-inner">
      <div class="myinfo-case">
        <div class="img" />
        <h1>広瀬 エイトル</h1>
      </div>
    </div>
    <div class="test" />
  </div>
</template>

<script>
export default {
  data: () => ({
    model: 0
  })
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
  z-index: -1;
  background-color: lighten(#00adb5, 2%);
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
    width: 320px;
    height: 550px;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;

    * {
      z-index: 1;
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
}
</style>
