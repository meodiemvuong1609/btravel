<template>
  <div class="flex items-center">
    <div class="flex gap-3 w-3/4 min-w-max ">
      <div v-for="(status, index) in statusOrder" :key="index" class="flex items-center bg-gray rounded-lg cursor-pointer p-3">
        {{status.title}}
      </div>
    </div>
  </div>
</template>

<script>
export default {

  props: {
    statusOrder: {
      type: Array,
      required: true
    },
  },
  data() {
    return {

    }
  },


}
</script>

<style>

</style>