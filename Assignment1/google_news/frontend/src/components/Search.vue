<template>
<v-container>
  <v-toolbar flat>
    <v-btn icon @click="backToHP">
        <v-icon>mdi-keyboard-backspace</v-icon>
      </v-btn>
    <v-text-field></v-text-field>
    <v-btn icon @click="search">
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
  </v-toolbar>
</v-container>
</template>

<script>
export default {
  name: 'Search',
  data () {
    return {
    }
  },
  methods: {
    backToHP () {
      this.$router.push('HomePage')
    },
    search () {
      this.$router.push('HomePage')
    }
  }
}
</script>
