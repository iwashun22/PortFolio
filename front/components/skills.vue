<template>
  <div class="case skills">
    <h1 class="title">
      Skills
    </h1>
  </div>
</template>

<script>
</script>

<style lang="scss">
#__layout {
  margin-top: 68px;
}

.title {
  width: fit-content;
  padding: 6px 20px;
  margin: 30px 30px 0 30px !important;
  color: white;
  font-weight: bolder;
}

.case {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  width: 100%;
  max-width: 980px;
}

@media screen and (max-width: 580px) {
  .title {
    font-size: 1.5rem;
    padding: 3px 10px;
    margin: 0 15px;
  }
}
</style>
