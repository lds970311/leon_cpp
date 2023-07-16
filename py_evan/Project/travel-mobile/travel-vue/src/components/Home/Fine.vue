<template>
  <div class="home-fine">
    <!--    精选景点-->
    <van-cell icon="/static/home/hot/fire.png" is-link title="热门推荐"
              title-style="text-align:left"
              value="全部榜单"
              value-class="right-style"
    />
    <div class="box-main">
      <a v-for="(item) in fineList" :key="item.id" class="hot-item" href="#">
        <div class="img">
          <span></span>
          <img :src="item.img" alt="">
        </div>
        <h5 class="van-ellipsis">{{ item.name }}</h5>
        <div class="price">
          <span>¥{{ item.price }}</span>起
        </div>
      </a>
    </div>
  </div>
</template>

<script>


export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Fine",
  data() {
    return {
      fineList: []
    }
  },
  methods: {
    initFineList() {
      this.fineList = [
        {id: 1, img: '/static/home/hot/h1.jpg', name: '景点名称', price: 65},
        {id: 2, img: '/static/home/hot/h2.jpg', name: '景点名称景点名称', price: 65},
        {id: 3, img: '/static/home/hot/h3.jpg', name: '景点名称', price: 65},
        {id: 4, img: '/static/home/hot/h4.jpg', name: '景点名称', price: 65},
        {id: 5, img: '/static/home/hot/h5.jpg', name: '景点名称景点名称', price: 65},
        {id: 6, img: '/static/home/hot/h6.jpg', name: '景点名称', price: 65},
        {id: 7, img: '/static/home/hot/h7.jpg', name: '景点名称景点名称景点名称', price: 65},
        {id: 8, img: '/static/home/hot/h8.jpg', name: '景点名称', price: 65},
        {id: 9, img: '/static/home/hot/h9.jpg', name: '景点名称', price: 65},
        {id: 10, img: '/static/home/hot/h10.jpg', name: '景点名称', price: 65}
      ]
    }
  },
  mounted() {
    this.initFineList()
  }
}
</script>

<style lang="less">
.home-fine {
  padding: 0 10px;

  .right-style {
    span {
      color: #a89999;
    }
  }

  .van-cell {
    padding: 10px 0;
    line-height: 24px;
  }

  .box-main {
    width: 100%;
    display: flex;
    padding-top: 10px;
    overflow-x: scroll;
  }


  .hot-item {


    display: flex;
    flex-direction: column;
    width: 100px;
    margin-right: 10px;
    padding-bottom: 10px;

    &:nth-child(1) .img span {
      background: url('~@/assets/images/top1.png');
      background-size: 100% auto;
    }

    &:nth-child(2) .img span {
      background: url('~@/assets/images/top2.png');
      background-size: 100% auto;
    }

    &:nth-child(3) .img span {
      background: url('~@/assets/images/top3.png');
      background-size: 100% auto;
    }

    h5 {
      color: #212121;
      padding: 2px 0;
      font-size: 12px;
      margin: 0;
    }

    .img {
      position: relative;

      span {
        position: absolute;
        left: 0;
        top: 0;
        display: inline-block;
        width: 42px;
        height: 20px;
        z-index: 10;
      }

      img {
        width: 100px;
        height: 100px;
      }
    }

    .price {
      color: #212121;
      font-size: 12px;

      span {
        color: #f50;
        font-size: 13px;

      }
    }


  }
}


</style>