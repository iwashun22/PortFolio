<template>
  <div>
    <Nuxt />
  </div>
</template>

<style lang="scss">
::-webkit-scrollbar {
  width: 10px;
  background-color: #393e46;
}

::-webkit-scrollbar-track {
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background-color: #00adb5;
  border-radius: 10px;
  box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.3);
}

#background {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100%;
  background: #393e46;
}
</style>
