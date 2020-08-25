<template>
<v-container>
    <v-row justify="center">
        <v-col cols="12" align='center'>
            ようこそ、{{user.name}}さん！
        </v-col>
            <v-btn>ログアウト</v-btn>
    </v-row>
</v-container>

</template>

<script>
export default{
  data () {
    return {
    //   Login.vueから送られてきた値を受け取るための箱(変数)
      user: {}
    }
  },
//   情報を受け取るための関数
  created () {
    //   userの変数の中に情報を入れる。
    this.user = this.$route.query.obj
    console.log(this.user)
  }
}
</script>

<style>
</style>
