<template>
  <div>
    <Header/>
    <router-view></router-view>
    
  </div>
</template>

<script>
import Header from '@/components/Header/Header.vue'
export default {
  name: 'HomeView',
  components: {
    Header
  }

}
</script>

<style>

</style>
