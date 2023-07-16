<template>
  <div class="home-hot">
    <!--    热门景点-->
    <van-cell icon="location-o" is-link title="精选景点"
              title-style="text-align:left"
              value="更多"
    />
    <ListSight :data-list="dataList"/>
  </div>
</template>

<script>
import ListSight from "@/components/Common/ListSight.vue";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Hot",
  components: {ListSight},

  data() {
    return {
      dataList: [
        {id: 1, name: '景点名称', score: 5, price: 98},
        {id: 2, name: '景点名称', score: 4.5, price: 98},
        {id: 3, name: '景点名称', score: 4, price: 98},
        {id: 4, name: '景点名称', score: 4.5, price: 98},
        {id: 5, name: '景点名称', score: 4.5, price: 98},
        {id: 6, name: '景点名称', score: 4.5, price: 98}
      ]
    }
  }
}
</script>
<style lang="less">
.home-hot {
  padding: 0 10px;

  .van-cell {
    padding: 10px 0;
  }
}
</style>