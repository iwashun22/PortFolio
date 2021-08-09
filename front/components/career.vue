<template>
  <div class="case career">
    <h1 class="title">
      Career
    </h1>
    <div class="inner-case">
      <v-card
        elevation="2"
        tile
        height="300"
        width="90%"
        dark
      ></v-card>
      <v-card
        elevation="2"
        tile
        height="300"
        width="90%"
        dark
      ></v-card>
      <v-card
        elevation="2"
        tile
        height="300"
        width="90%"
        dark
      ></v-card>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
  })
}
</script>

<style lang="scss" scoped>
.text-right {
  text-align: right;
}

.title {
  border-bottom: solid 3px white;
  width: fit-content;
  padding: 6px 20px;
  margin: 0 30px;
  color: white;
}

.case {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  max-width: 980px;
}

.inner-case {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 30px 0;

  .v-card {
    margin: 14px 0;
  }
}

@media screen and (max-width: 580px) {
  .title {
    font-size: 1.5rem;
    padding: 3px 10px;
    margin: 0 15px;
  }
}
</style>
