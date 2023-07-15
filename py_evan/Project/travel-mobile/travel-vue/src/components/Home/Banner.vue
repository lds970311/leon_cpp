<template>
  <div class="home-banner">
    <van-swipe :autoplay="3000" class="my-swipe" duration="1000"
               indicator-color="white">
      <van-swipe-item v-for="item in bannerList" :key="item.id">
        <img :src="item.url" alt="" style="width: 100%; ">
      </van-swipe-item>
    </van-swipe>
  </div>
</template>

<script>


export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Banner",
  data() {
    return {
      bannerList: []
    }
  },
  methods: {
    initBanner() {
      this.bannerList = [
        {id: 1, url: '/static/home/banner/banner1.jpg'},
        {id: 2, url: '/static/home/banner/banner2.jpg'},
        {id: 3, url: '/static/home/banner/banner3.jpg'}
      ]
    }
  },
  mounted() {
    this.initBanner()
  }
}
</script>
<style lang="less" scoped>

</style>