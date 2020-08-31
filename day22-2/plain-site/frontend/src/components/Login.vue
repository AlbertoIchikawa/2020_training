<template>
    <v-container>
      <v-row justify="center">
        <v-col cols=6>
  <v-card outlined max-width="1100" height="300">
    <v-form>
      <v-text-field
        v-model="email"
        label="メールアドレス"
        :rules="[rules.required, rules.email]"
        required></v-text-field>
      <v-text-field
        v-model="password"
        label="パスワード"
        :rules="[rules.required, rules.password]"
        required></v-text-field>
        <div class="text-center">
      <v-btn justify="center" @click="submit">ログイン</v-btn>
      </div>
    </v-form>
  </v-card>
  </v-col>
  </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: '',
      rules: {
        required: value => !!value || 'Required.',
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Invalid e-mail.'
        },
        password: value => value.length <= 20 || 'Max 20 characters'
      }
    }
  },
  methods: {
    submit () {
      // 値を受け取るためのURLを記述する→実行したいメソッドを呼び出すためにURLを記述する
      axios.post('http://127.0.0.1:8000/login/', {
        // emailとpasswordを渡してログイン判定を行う
        email: this.email,
        password: this.password
      })
        .then((res) => {
          console.log(res.data)
          // homepageへ画面遷移と情報を渡す。
          this.$router.push({name: 'HomePage', query: {obj: res.data}})
        })
        .catch(err => {
          console.log('axiosGetError', err)
          // 画面遷移せずにアラート表示、入力値を残す。
          this.email = ''
          this.password = ''
          alert('記入された情報が正しくありません。\nもう一度入力してください。')
        })
        .finally(res => console.log('finally'))
    }
  }
}
</script>
