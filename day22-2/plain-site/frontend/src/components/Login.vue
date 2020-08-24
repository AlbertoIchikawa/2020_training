<template>
  <!-- <div> -->
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
  <!-- </div> -->
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: '',
      img: '',
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
      // 値を受け取るためのURLを記述するのか
      axios.post('http://127.0.0.1:8000/login/', {
        email: this.email,
        password: this.password
        // データ形式が正しくないJSONで渡されている。
        // Jason→pythonでJSON形式を受け取る方法。
      })
        .then((res) => {
          console.log(res.data)
          // call back 関数
        })
        .catch(err => {
          console.log('axiosGetError', err)
        })
        .finally(res => console.log('finally'))
    }
  }
}
</script>
