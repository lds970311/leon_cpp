<template>
  <div class="list-sight">
    <a v-for="item in $props.dataList" :key="item.id" class="site-item" href="#">
      <img alt="" src="/static/home/hot/h1.jpg">
      <div class="right">
        <h5>{{ item.name }}</h5>
        <van-rate
            v-model="item.score"
            color="#ffd21e"
            readonly
            void-color="#eee"
            void-icon="star"
        />
        <div class="tips">4人点评 | 90%满意</div>
        <div class="tips light">广东 深圳</div>
        <div class="line-price">¥{{ item.price }} 起</div>
      </div>
    </a>


  </div>
</template>

<script>


export default {
  name: "ListSight",
  props: {
    dataList: Array,
    required: true
  }
}
</script>


<style lang="less" scoped>
.list-sight {
  .site-item {
    display: flex;
    margin-top: 10px;
    border-bottom: 1px solid #f6f6f6;

    img {
      width: 100px;
      height: 100px;
    }

    .right {
      text-align: left;
      flex-grow: 1;
      justify-content: center;
      padding-left: 5px;
      position: relative;
    }

    h5 {
      color: #212121;
      font-size: 14px;
      padding: 5px 0;
      margin: 0;
    }

    .line-price {
      position: absolute;
      right: 10px;
      top: 20px;
      display: inline-block;
      color: #f50;
      font-size: 16px;
      font-weight: bold;
    }

    .tips {
      font-size: 12px;
      color: #666;

      &.light {
        color: #999;
      }
    }
  }
}
</style>