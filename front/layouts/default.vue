<template>
  <div>
    <v-app-bar
      dense
      dark
    ></v-app-bar>
    <Nuxt />
  </div>
</template>

<style lang="scss">
::-webkit-scrollbar-thumb {
  background-color: #00adb5;
}

#background {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100%;
  background: #393e46;
}

header {
  z-index: 99;
  position: fixed;
  top: 0;
}

body {
  background-color: lighten(#00adb5, 2%);
}
</style>
