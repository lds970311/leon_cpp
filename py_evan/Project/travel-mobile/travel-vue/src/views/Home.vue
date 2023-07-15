<template>
  <div class="page-home">
    <Banner></Banner>
    <Fine></Fine>
  </div>
</template>

<script>
import Banner from "@/components/Home/Banner.vue";
import Fine from "@/components/Home/Fine.vue";

export default {

  // eslint-disable-next-line vue/multi-word-component-names
  name: "Home",
  components: {Fine, Banner},

  methods: {},
  mounted() {

  }
}
</script>

<style lang="less" scoped>
.page-home {

}
</style>