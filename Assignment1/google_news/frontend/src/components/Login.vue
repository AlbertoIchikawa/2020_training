<template>
<v-container>
  <v-row >
    <v-col align="center">
<v-card width="1000px">
  <v-row justify="center">
    <v-col>
        <img height="400px" width="400px" :src='this.pic' alt="">
        <v-form>
          <v-text-field
            v-model="email"
            label="メールアドレス"
            :rules="[rules.required, rules.email]"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="パスワード"
            :rules="[rules.required, rules.password]"
            required
          ></v-text-field>
          <v-btn justify="center" @click="submit">ログイン</v-btn>
        </v-form>
    </v-col>
  </v-row>
  </v-card></v-col></v-row></v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: '',
      pic: 'https://publicdomainq.net/images/201712/21s/publicdomainq-0016994xwa.jpg',
      rules: {
        required: (value) => !!value || 'Required.',
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Invalid e-mail.'
        },
        password: (value) => value.length <= 20 || 'Max 20 characters'
      }
    }
  },
  methods: {
    submit () {
      axios.post('http://127.0.0.1:8000/login/', {
        email: this.email,
        password: this.password
      })
        .then((res) => {
          console.log(res.data)
          this.$router.push({name: 'HomePage', query: {obj: res.data}})
        })
        .catch(err => {
          console.log('axiosGetError', err)
          this.email = ''
          this.password = ''
          alert('記入された情報が正しくありません。\nもう一度入力してください。')
        })
        .finally(res => console.log('finaly'))
    }
  }
}
</script>
