<template>
  <div class="first-main case first-case">
    <h1 class="title">
      About Me
    </h1>
    <div class="aboutme-info-case">
      <div class="img" />
      <div class="msg">
        <p>
          中学生の時にプログラミングを趣味で初めて、<br>
          今は専門学校に通って勉強しています。<br>
          最近はインターン二行って精進しております。<br>
          専門はWeb系ですが、データサイエンティストを目指しています！
        </p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.title {
  width: fit-content;
  padding: 6px 20px;
  margin: 0 30px;
}

.first-main {
  width: 100%;
  border-radius: 0 !important;
  margin: calc(100vh + 30px) auto 20px auto;
  max-width: 980px;

  h1 {
    color: white;
  }
}

.case {
  display: flex;
  flex-direction: column;
}

.first-case {
  .aboutme-info-case {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    margin: 15px 0;

    .msg {
      max-width: 48vw;
      margin: auto 0;
      color: white;
      line-height: 2rem;
      background-color: #111;

      p {
        padding: 14px;
        overflow-wrap: break-word;
      }
    }

    .img {
      width: 12vw !important;
      height: 12vw !important;
      min-width: 150px !important;
      min-height: 150px !important;
      background-image: url(~static/icon.png);
      background-size: cover;
      background-position: center center;
      border-radius: 50%;
      margin: 30px 0;
    }
  }
}

@media screen and (max-width: 580px) {
  .aboutme-info-case {
    flex-direction: column !important;
    align-items: center;
    max-width: initial;

    .img {
      max-height: initial !important;
      max-width: initial !important;
      margin: 30px auto !important;
    }

    .msg {
      width: 100%;
      max-width: 90vw !important;

      p {
        width: 100%;
        max-width: 90vw !important;
      }
    }
  }

  .title {
    font-size: 1.5rem;
    padding: 3px 10px;
    margin: 0 15px;
  }
}
</style>
