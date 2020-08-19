<template>
  <div>
    <v-form>
      <v-text-field
        v-model="username"
        label="ログインID"
        required></v-text-field>
      <v-text-field
        v-model="password"
        label="パスワード"
        required></v-text-field>
      <v-btn @click="submit">ログイン</v-btn>
      <img :src="img" alt="">
    </v-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      username: null,
      password: null,
      img: ''
    }
  },
  methods: {
    submit () {
      // alert('login!')
      axios.get('https://dog.ceo/api/breeds/image/random')
      .then((res) => {
          console.log(res.data.message)
          this.img = res.data.message
        // Vue.set(this, name, res.data);
        // this.$emit('GET_AJAX_COMPLETE');
      })
    }
  }
}
</script>
