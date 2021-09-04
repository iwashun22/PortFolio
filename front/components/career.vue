<template>
  <div class="case career">
    <h1 class="title">
      Career
    </h1>
    <div class="inner-case">
      <template v-if="loading">
        <v-progress-circular
          size="50"
          indeterminate
          class="loader"
        />
      </template>
      <h1
        v-if="err"
        style="color: white;"
      >
        Error
      </h1>
      <v-card
        v-for="(item, i) in career.data"
        v-else
        :key="i"
        elevation="2"
        tile
        width="90%"
        dark
      >
        <v-card-title>
          {{ item.WorkSpace }}
        </v-card-title>
        <div
          class="tag-case"
        >
          <p
            v-for="tag in item.tags"
            :key="tag.id"
            class="tag"
          >
            {{ tag.name }}
          </p>
        </div>
        <p
          v-if="item.EndWork == null"
          class="date"
        >
          {{ item.StartWork }} ～ 現在
        </p>
        <p
          v-else
          class="date"
        >
          {{ item.StartWork }} ～ {{ item.EndWork }}
        </p>

        <p class="content-case">
          {{ item.content }}
        </p>
        <div class="link">
          <NuxtLink
            v-if="$route.path !== '/career'"
            :to="{ name: 'career' }"
          >
            すべて見る
          </NuxtLink>
          <NuxtLink :to="{ path: `/career/${ item.id }`}">
            詳しく見る
          </NuxtLink>
        </div>
      </v-card>
    </div>
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
  async created () {
    if (this.$route.path === '/career') {
      this.career = await this.$axios.get('api/career/')
        .catch((err) => {
          this.loading = false
          this.check = true
          this.err = err
        }).finally(() => {
          this.loading = false
          this.check = false
        })
    } else {
      this.career = await this.$axios.get('api/career/min_career')
        .catch((err) => {
          this.loading = false
          this.check = true
          this.err = err
        }).finally(() => {
          this.loading = false
          this.check = false
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.text-right {
  text-align: right;
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

.inner-case {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 30px 10px 0 10px;

  .v-card {
    margin: 14px 0 0 0;
    display: flex !important;
    flex-direction: column;
    max-height: 600px;
  }

  .v-card__title {
    font-size: 200%;
    padding: 40px 60px 0 60px;
    font-weight: bolder;
  }

  .tag-case {
    display: flex;
    flex-wrap: wrap;
    padding: 15px 60px;

    .tag {
      padding: 3px 6px;
      margin: 3px 3px;
      font-size: 80%;
      background-color: rgb(0, 0, 0);
      color: #aad8d3;

      &:hover {
        color: #00adb5;
      }
    }
  }

  .content-case {
    margin: 20px 60px;
    max-height: calc(24px * 10) !important;
    overflow: hidden;
    word-break: break-all;
    text-overflow: ellipsis;
    line-height: 24px;
    font-size: 16px;
    height: 100%;
  }

  .link {
    text-align: right;
    padding: 15px 60px;

    a {
      padding: 0 10px;
      color: #aad8d3;

      &:hover {
        color: #00adb5;
      }
    }
  }

  .date {
    padding-left: 60px;
  }
}

.loader {
  margin: 0 auto;
  color: white;
}

@media screen and (max-width: 1000px) {
  .inner-case {
    .v-card {
      margin: 14px 0;
    }

    .v-card__title {
      font-size: 170%;
      padding: 30px 10px 0 10px;
    }

    .tag-case {
      padding: 15px 10px;

      .tag {
        padding: 3px 6px;
        margin: 3px 3px;
        font-size: 80%;
        font-weight: bold;
      }
    }

    .content-case {
      margin: 20px 10px;
      font-size: 16px;
      height: 100%;
    }

    .link {
      text-align: right;
      margin: 15px 0;
      padding: 0;

      a {
        margin: 0 !important;
        padding: 0 6px !important;
      }
    }

    .date {
      padding: 0;
      font-size: 70%;
      margin: 0 15px;
    }
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
