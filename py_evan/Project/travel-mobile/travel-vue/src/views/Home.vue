<template>
  <div class="page-home">
    <Banner></Banner>
    <Fine></Fine>
    <Hot></Hot>
    <Footer/>
  </div>
</template>

<script>
import Banner from "@/components/Home/Banner.vue";
import Fine from "@/components/Home/Fine.vue";
import Hot from '@/components/Home/Hot.vue'
import Footer from "@/components/Common/Footer.vue";

export default {

  // eslint-disable-next-line vue/multi-word-component-names
  name: "Home",
  components: {Footer, Hot, Fine, Banner},

  methods: {},
  mounted() {

  }
}
</script>

<style lang="less" scoped>
.page-home {

}
</style>