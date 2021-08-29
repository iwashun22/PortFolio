<template>
  <div class="card-case">
    <template v-if="loading">
      <v-progress-circular
        size="50"
        indeterminate
        class="loader"
      />
    </template>
    <h1
      v-else-if="err"
      style="color: white;"
    >
      Error
    </h1>
    <v-card
      v-else
      elevation="2"
      tile
      dark
    >
      <h1 class="career-title">
        {{ career.WorkSpace }}
      </h1>
      <div class="website-case">
        <v-icon>
          mdi-link-variant
        </v-icon>
        <a
          v-if="career.website !== null"
          :href="`${ career.website }`"
          class="website"
        >
          公式サイト
        </a>
        <p
          v-else
          class="website"
        >
          公式サイトはありません。
        </p>
      </div>
      <div
        class="tag-case"
      >
        <p
          v-for="tag in career.tags"
          :key="tag.id"
          class="tag"
        >
          {{ tag.name }}
        </p>
      </div>
      <p
        v-if="career.EndWork == null"
        class="date"
      >
        {{ career.StartWork }} ～ 現在
      </p>
      <p
        v-else
        class="date"
      >
        {{ career.StartWork }} ～ {{ career.EndWork }}
      </p>

      <div class="content-case">
        {{ career.content }}
      </div>
      <div class="link">
        <a @click="back()">
          戻る
        </a>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      career: [],
      check: null,
      loading: true,
      err: null
    }
  },
  head: {
    title: '詳しく'
  },
  async created () {
    this.career = await this.$axios.get(`api/career/${this.$route.params.id}`)
      .catch((err) => {
        this.loading = false
        this.check = true
        this.err = err
      }).finally(() => {
        this.loading = false
        this.check = false
      })

    if (this.career) {
      this.career = this.career.data
    }
  },
  methods: {
    back () {
      this.$router.go(-1)
    }
  }
}
</script>

<style lang="scss">
#__layout {
  margin-top: 68px;
}

.loader {
  margin: 30px auto;
  color: white;
}

.card-case {
  width: 100%;
  max-width: 1080px;
  display: flex;
  margin: 50px auto 0 auto;

  .v-card {
    width: 100%;
    margin: 50px 0;
    padding: 0 80px;

    .career-title {
      margin: 50px 0 15px 0;
    }

    .website-case {
      margin: 12px 0;
      display: flex;
      align-items: center;
      flex-direction: row;

      .website {
        color: #aad8d3;
        padding: 0 6px;

        &:hover {
          color: #00adb5;
        }
      }
    }

    .tag-case {
      display: flex;
      flex-wrap: wrap;
      padding: 0  auto 0 0;

      .tag {
        padding: 3px 6px;
        margin: 3px 3px;
        font-size: 80%;
        background-color: rgb(0, 0, 0);
        color: #aad8d3;
        font-weight: bold;

        &:hover {
          color: #00adb5;
        }
      }
    }

    .date {
      padding: 10px 0;
    }

    .content-case {
      padding: 25px 0;
    }
  }

  .link {
    text-align: right;
    padding: 20px 60px;

    a {
      padding: 0 10px;
      color: #aad8d3;

      &:hover {
        color: #00adb5;
      }
    }
  }
}

@media screen and (max-width: 1000px) {
  .v-card {
    padding: 0 40px !important;
  }
}

@media screen and (max-width: 580px) {
  .v-card {
    padding: 0 20px !important;

    .title {
      font-size: 32px !important;
    }

    .link {
      padding-right: 20px;
    }
  }
}
</style>
