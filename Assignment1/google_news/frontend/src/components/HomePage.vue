<template>
<v-container>
<v-row>
  <v-col cols="12">
  <v-btn  @click="abroad">国際</v-btn>
  <v-btn @click="japan">日本</v-btn>
  <v-btn @click="local">ローカルニュース</v-btn>
  <v-btn @click="business">ビジネス</v-btn>
  <v-btn @click="science">科学＆テクノロジー</v-btn>
  <v-btn @click="gossip">エンタメ</v-btn>
  <v-btn @click="sports">スポーツ</v-btn>
  </v-col>
  <v-col align="center"  v-for="title in titles" :key="title">
  <v-card width=1185>
  <v-col>
    <v-card-title>
    {{ title }}
  </v-card-title></v-col>
   <v-col class="text-right">
     <v-img tile height="100px" width="100px" src="https://2.bp.blogspot.com/-VJOwedxrDa4/WWXXWuTIarI/AAAAAAABFho/l09dY2mf-qs1atvIob4Fgiri45FB6MKCgCLcBGAs/s800/website_news.png"></v-img>
  </v-col>
</v-card>
</v-col>
</v-row>
</v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomePage',
  data () {
    return {
      user: {},
      titles: []
    }
  },
  created () {
    this.user = this.$router.query.obj
    console.log(this.user)
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/home/')
      .then((res) => {
        console.log(res)
        this.titles = res.data
      })
      .catch((e) => {
        alert(e)
      })
  },
  methods: {
    search () {
      this.$router.push('Search')
    },
    abroad () {
      axios.get('http://127.0.0.1:8000/abroad/')
        .then((res) => {
          console.log(res)
          this.titles = res.data
        })
        .catch((e) => {
          alert(e)
        })
    },
    japan () {
      axios.get('http://127.0.0.1:8000/japan/')
        .then((res) => {
          console.log(res)
          this.titles = res.data
        })
        .catch((e) => {
          alert(e)
        })
    },
    local () {
      axios.get('http://127.0.0.1:8000/local/')
        .then((res) => {
          console.log(res)
          this.titles = res.data
        })
        .catch((e) => {
          alert(e)
        })
    },
    business () {
      axios.get('http://127.0.0.1:8000/business/')
        .then((res) => {
          console.log(res)
          this.titles = res.data
        })
        .catch((e) => {
          alert(e)
        })
    },
    science () {
      axios.get('http://127.0.0.1:8000/science/')
        .then((res) => {
          console.log(res)
          this.titles = res.data
        })
        .catch((e) => {
          alert(e)
        })
    },
    gossip () {
      axios.get('http://127.0.0.1:8000/gossip/')
        .then((res) => {
          console.log(res)
          this.titles = res.data
        })
        .catch((e) => {
          alert(e)
        })
    },
    sports () {
      axios.get('http://127.0.0.1:8000/sports/')
        .then((res) => {
          console.log(res)
          this.titles = res.data
        })
        .catch((e) => {
          alert(e)
        })
    }
  }
}
</script>
