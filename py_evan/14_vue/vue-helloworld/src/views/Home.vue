<template>
  <div class="home">
    <my-component></my-component>
    <div v-show="false" v-html="rawHtml"></div>
    <a :href="link">google</a>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue from "vue";

Vue.component('my-component', {
  template: '<h3>局部组件</h3>'
})

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Home',
  data() {
    return {
      rawHtml: '<h3>Hello</h3>',
      link: 'https://www.google.com'
    }
  }
}
</script>

<style lang="less">

</style>