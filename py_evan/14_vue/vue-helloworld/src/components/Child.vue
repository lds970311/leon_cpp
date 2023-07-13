<template>
  <div class="child">
    <slot></slot>
    <span>{{ $props.username }}</span>
    <input type="text" v-model="name">
    <button @click="submit" value="提交">提交</button>
  </div>
</template>

<script>


export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Child",
  data() {
    return {
      name: ''
    }
  },
  methods: {
    submit() {
      this.$emit('getName', this.name)
    }
  },
  props: {
    username: {
      type: String,
      required: true,
      default: 'hehe'
    }
  }
}
</script>

<style scoped lang="less">

</style>