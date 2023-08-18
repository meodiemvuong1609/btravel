<template>
  <div class="container mx-auto grid grid-flow-row">
      <div class="header w-full my-8">
        <div class="header__top w-full p-4 bg-white rounded-lg">
          <div class="top flex justify-between pb-5">
            <input type="text" class="w-1/3 flex p-3 rounded-lg bg-white border-2 border-#E2E2E2" placeholder="Tìm kiếm theo mã đơn hàng">
            <button class="w-1/6 rounded-lg bg-red-dark-1 p-3 md:p-4 font-medium text-white">Tạo đơn hàng</button>
          </div>
          <div class="bot flex justify-between">
            <status-order :statusOrder="statusOrder"></status-order>
  
            <div class="select w-1/6">
              <button class="rounded-lg bg-white p-3 md:p-4 font-medium text-black border-2 border-#E2E2E2 w-full">Chọn loại đối tác mua</button>
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
            <!-- Table rows -->
        <div class="table__rows">
          <div class="grid grid-cols-7 p-2 font-bold w-full justify-between gap-11 py-4 px-6 bg-white rounded-lg my-2">
          <div class="w-1/7 text-center">DH001</div>
          <div class="w-1/7 text-center">ABC Corp</div>
          <div class="w-1/7 text-center">XYZ Supplier</div>
          <div class="w-1/7 text-center">0123456789</div>
          <div class="w-1/7 text-center">123 Street</div>
          <div class="w-1/7 text-center">$100.00</div>
          <div class="w-1/7 text-center">In progress</div>
        </div>
        <div class="grid grid-cols-7 p-2 font-bold w-full justify-between gap-11 py-4 px-6 bg-white rounded-lg my-2">
          <div class="w-1/7 text-center">DH001</div>
          <div class="w-1/7 text-center">ABC Corp</div>
          <div class="w-1/7 text-center">XYZ Supplier</div>
          <div class="w-1/7 text-center">0123456789</div>
          <div class="w-1/7 text-center">123 Street</div>
          <div class="w-1/7 text-center">$100.00</div>
          <div class="w-1/7 text-center">In progress</div>
        </div>
        <div class="grid grid-cols-7 p-2 font-bold w-full justify-between gap-11 py-4 px-6 bg-white rounded-lg my-2">
          <div class="w-1/7 text-center">DH001</div>
          <div class="w-1/7 text-center">ABC Corp</div>
          <div class="w-1/7 text-center">XYZ Supplier</div>
          <div class="w-1/7 text-center">0123456789</div>
          <div class="w-1/7 text-center">123 Street</div>
          <div class="w-1/7 text-center">$100.00</div>
          <div class="w-1/7 text-center">In progress</div>
        </div>
        <div class="grid grid-cols-7 p-2 font-bold w-full justify-between gap-11 py-4 px-6 bg-white rounded-lg my-2">
          <div class="w-1/7 text-center">DH001</div>
          <div class="w-1/7 text-center">ABC Corp</div>
          <div class="w-1/7 text-center">XYZ Supplier</div>
          <div class="w-1/7 text-center">0123456789</div>
          <div class="w-1/7 text-center">123 Street</div>
          <div class="w-1/7 text-center">$100.00</div>
          <div class="w-1/7 text-center">In progress</div>
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
      statusOrder: []
    }
  },

  methods: {
    async getStatusOrder() {
      try {
        const response = await HTTP.get('account/api/gender/')
        if (response.status === 200) {
          this.statusOrder = response.data.data
        }
        } catch (error) {
          console.log(error)
      }
    }
  },
  mounted() {
    this.getStatusOrder()
  }
}

</script>

<style>

</style>