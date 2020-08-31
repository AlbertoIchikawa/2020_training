<template>
<v-card color="grey lighten-4"
    flat
    >
  <v-toolbar dense>
    <v-btn icon @click="backToSearch">
        <v-icon>mdi-keyboard-backspace</v-icon>
      </v-btn>
    <v-text-field></v-text-field>
  </v-toolbar>
</v-card>
</template>

<script>
export default {
  name: 'News',
  data () {
    return {
    }
  },
  methods: {
    backToSearch () {
      this.$router.push('Search')
    }
  }
}
</script>
