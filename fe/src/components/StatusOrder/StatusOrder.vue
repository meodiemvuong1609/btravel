<template>
  <div class="flex items-center">
    <div class="flex gap-3 w-3/4 h-3/4 ">
      <div v-for="(status, index) in statusOrder" :key="index" class="flex items-center bg-gray rounded-lg cursor-pointer px-4 py-2">
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