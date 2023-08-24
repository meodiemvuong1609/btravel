<template>
  <div class="container mx-auto grid grid-flow-row">
      <div class="header w-full my-8">
        <div class="header__top w-full p-4 bg-white rounded-lg">
          <div class="top flex justify-between pb-5">
            <input type="text" class="w-1/4 h-8 items-center flex p-3 rounded-lg bg-white border-2 border-#E2E2E2" placeholder="Tìm kiếm theo mã đơn hàng">
            <button class="flex w-1/6 h-8 justify-center text-sm rounded-lg bg-red-dark-1 p-3 font-medium text-white">Tạo đơn hàng</button>
          </div>
          <div class="bot flex justify-between">
            <status-order :statusOrder="statusOrder"></status-order>
  
            <div class="select w-1/6">
              <button class="rounded-lg bg-white p-3 font-medium text-sm text-black border-2 border-#E2E2E2 w-full">Chọn loại đối tác mua</button>
            </div>
          </div>
        </div>
      </div>
      <div class="container grid grid-flow-row">
        <div class="grid grid-cols-7 p-2 font-bold w-full justify-between py-4 px-6 bg-red-dark-1 text-white rounded-lg">
          <div class="w-1/7 text-center">Mã đơn hàng</div>
          <div class="w-1/7 text-center">Đối tác mua</div>
          <div class="w-1/7 text-center">Đối tác cung cấp</div>
          <div class="w-1/7 text-center">Số điện thoại</div>
          <div class="w-1/7 text-center">Địa chỉ</div>
          <div class="w-1/7 text-center">Tổng tiền</div>
          <div class="w-1/7 text-center">Trạng thái</div>
        </div>
        <div class="table__rows">
          <div v-for="(item, index) in order" :key="index" class="grid grid-cols-7 p-2 font-bold w-full justify-between py-4 px-6 bg-white rounded-lg my-2">
            <div class="w-1/7 text-center">{{item.code}}</div>
            <div class="w-1/7 text-center">{{item.account_buy_data.key_account}}</div>
            <div class="w-1/7 text-center">{{item.account_sell_data.system_data.code}}</div>
            <div class="w-1/7 text-center">{{item.account_buy_data.phone}}</div>
            <div class="w-1/7 text-center">{{item.account_buy_data.address_data.title}}</div>
            <div class="w-1/7 text-center">{{item.total}}</div>
            <div class="w-1/7 text-center">{{item.status_data.title}}</div>

          </div>
        </div>
        </div>
        

      </div>
    

</template>

<script>
import StatusOrder from '../StatusOrder/StatusOrder.vue';
import HTTP from '@/HTTP/HTTP.js';
export default {
  components: { StatusOrder },
  name: 'Order',
  data() {
    return {
      statusOrder: [],
      order: []
    }
  },

  methods: {
    async getStatusOrder() {
      try {
        const response = await HTTP.get('order/api/statusordersystem/')
        if (response.status === 200) {
          this.statusOrder = response.data.data
        }
        } catch (error) {
          console.log(error)
      }
    },
    async getListOrder() {
      try {
        const response = await HTTP.get('order/api/ordersystem/')
        if (response.status === 200) {
          this.order = response.data.data
        }
        } catch (error) {
          console.log(error)
      }
    }
  },
  mounted() {
    this.getStatusOrder(),
    this.getListOrder()
  }
}

</script>

<style>

</style>