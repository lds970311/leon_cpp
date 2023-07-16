<template>
  <!--  底部导航-->
  <div class="footer">
    <van-tabbar v-model="active">
      <van-tabbar-item icon="wap-home-o">首页</van-tabbar-item>
      <van-tabbar-item icon="search">搜索</van-tabbar-item>
      <van-tabbar-item icon="user-o">我的</van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>


export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Footer",
  data() {
    return {
      active: 1
    }
  }
}
</script>


<style lang="less" scoped>
.footer {
  position: fixed;
  bottom: 0;
  background-color: #fff;
}
</style>