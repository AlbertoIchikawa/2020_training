<template>
<v-card outlined>
  <v-row justify="center">
    <v-col>
        <img src="pic" alt="">
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
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: '',
      pic: '',
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
        })
        .catch(err => {
          console.log('axiosGetError', err)
        })
        .finally(res => console.log('finaly'))
    }
  },
  mounted () {
    axios.get('https://dog.ceo/api/breeds/image/random')
      .then((res) => {
        console.log(res.data.message)
        this.pic = res.data.message
      })
  }
}
</script>
