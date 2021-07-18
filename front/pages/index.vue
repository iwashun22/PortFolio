<template>
  <div>
    <div id="background" class="background" />
    <div class="background-inner">
      <div class="myinfo-case">
        <img src="~/assets/icon.png" />
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
  z-index: -1;
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
  }
}
</style>
