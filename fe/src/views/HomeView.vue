<script setup>
  import { reactive, computed, onMounted } from 'vue';
  import Header from '@/components/Header/Header.vue';
  import axios from 'axios';
  const headers = {
    'Authorization': `Token e06f13b48b51f2b07df1ceee0af81ffdad19a158`
  };
  onMounted(async () => {
    const res = await axios.get('http://localhost:8000/account/api/system/', { headers });
    console.log(res);
  });
  
</script>

<template>
  <div>
    <div class="w-full">
    <Header/>
  </div>
  <div class="container mx-auto grid grid-flow-row">
    <div class="header w-full my-8">
      <div class="header__top w-full p-4 bg-white rounded-lg">
        <div class="top flex justify-between pb-5">
          <input type="text" class="w-1/3 flex p-3 rounded-lg bg-white border-2 border-#E2E2E2" placeholder="Tìm kiếm theo mã đơn hàng">
          <button class="w-1/6 rounded-lg bg-red-600 p-3 md:p-4 font-medium text-white">Tạo đơn hàng</button>
        </div>
        <div class="bot flex justify-between">
          <div class="status flex w-3/4 gap-2">
            <div class="flex items-center px-4 py-2 bg-slate-300 rounded-lg cursor-pointer">Tất cả</div>
            <div class="flex items-center px-4 py-2 bg-slate-300 rounded-lg cursor-pointer">Chờ xác nhận</div>
            <div class="flex items-center px-4 py-2 bg-slate-300 rounded-lg cursor-pointer">Chờ phản hồi</div>
            <div class="flex items-center px-4 py-2 bg-slate-300 rounded-lg cursor-pointer">Đã xác nhận</div>
            <div class="flex items-center px-4 py-2 bg-slate-300 rounded-lg cursor-pointer">Hoàn thành</div>
            <div class="flex items-center px-4 py-2 bg-slate-300 rounded-lg cursor-pointer">Từ chối</div>
          </div>
          <div class="select w-1/6">
            <button class="rounded-lg bg-white p-3 md:p-4 font-medium text-black border-2 border-#E2E2E2 w-full">Chọn loại đối tác mua</button>
          </div>
        </div>
      </div>
    </div>
    <div class="container grid grid-flow-row">
      <div class="grid grid-cols-7 p-2 font-bold w-full justify-between py-4 px-6 bg-red-600 text-white rounded-lg">
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
  </div>
</template>
