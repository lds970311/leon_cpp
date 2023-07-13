<template>
  <div class="home">
    <my-component></my-component>
    <div v-show="false" v-html="rawHtml"></div>
    <a :href="link">google</a>
    <ul>
      <li v-for="item in areaList" :key="item">{{ item }}</li>
    </ul>
    <div>
      <button @click="count++">{{ count }}</button>
    </div>
    <p>{{ price | priceFormatter }}</p>
    <Child username="evan" @getName="handleName">
      <span>hahaha</span>
    </Child>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue from "vue";
import Child from "@/components/Child.vue";

Vue.component('my-component', {
  template: '<h3>局部组件</h3>'
})

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Home',
  components: {Child},
  methods: {
    handleName(data) {
      console.log(data)
    }
  },
  data() {
    return {
      rawHtml: '<h3>Hello</h3>',
      link: 'https://www.google.com',
      areaList: ['Bejjing', 'Shanghai', 'HongKong'],
      count: 0,
      price: 22.881
    }
  },
  filters: {
    priceFormatter(price) {
      if (price === undefined || price === null || isNaN(price)) {
        return price
      }
      return '¥' + price.toFixed(2)
    }
  }
}
</script>

<style lang="less">

</style>