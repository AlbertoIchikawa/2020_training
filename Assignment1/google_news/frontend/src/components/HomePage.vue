<template>
<v-card color="grey lighten-4"
    flat
    >
  <v-toolbar flat>
    <v-btn icon @click="search" color="grey">
        <v-icon >mdi-magnify</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
    <v-toolbar-title align-center>ヘッドライン</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn @click.stop="dialog = true"><v-avatar></v-avatar></v-btn>
    <div>{{user.data}}</div>
    <!-- <v-dialog
    v-model="dialog"
    max-widht="200">
    </v-dialog> -->
  </v-toolbar>
</v-card>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomePage',
  data () {
    return {
      user: {}
    }
  },
  created () {
    this.user = this.$router.query.obj
    console.log(this.user)
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/test/')
      .then((res) => {
        console.log(res.data)
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
