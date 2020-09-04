<template>

<v-row justify="center" align-content="center">
  <v-col cols=12 sm=12 md=12 lg=12 xl=12 v-for="title in titles" :key="title">
  <v-card>
  <v-col>
    <v-card-title >
    {{ title }}
  </v-card-title></v-col>
   <!-- <v-col class="text-right"> -->
     <!-- <v-img tile height="100px" width="100px" src="https://2.bp.blogspot.com/-VJOwedxrDa4/WWXXWuTIarI/AAAAAAABFho/l09dY2mf-qs1atvIob4Fgiri45FB6MKCgCLcBGAs/s800/website_news.png"></v-img> -->
  <!-- </v-col> -->
</v-card>
</v-col>
</v-row>
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
    axios.get('http://127.0.0.1:8000/test/')
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
    }
  }
}
</script>
