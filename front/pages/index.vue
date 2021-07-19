<template>
  <div>
    <div id="background" class="background" />
    <div class="background-inner">
      <div class="myinfo-case">
        <div class="img" />
        <h1>広瀬 エイトル</h1>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style lang="scss">
#background {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100%;
  background: #393e46;
  z-index: 1;
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
      margin-top: 1px;
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
