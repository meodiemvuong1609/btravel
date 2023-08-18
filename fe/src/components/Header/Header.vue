<template>
    <div class="header" :class="{ 'open': showDropdown }">
        <div class="flex justify-center items-center">
            <img src="https://f004.backblazeb2.com/file/warehousebinh/logokiot/kiot_logo.png" alt="">
        </div>
        <div class="header__menu">
            <router-link to="/orders" class="header__menu--item">Đơn hàng</router-link>
            <router-link to="/products" class="header__menu--item">Sản phẩm</router-link>
            <router-link to="/partners" class="header__menu--item">Đối tác</router-link>
            <router-link to="/employees" class="header__menu--item">Nhân viên</router-link>
        </div>
        <div class="header__account" @click="toggleDropdown">
            <div class="header__account--fullname pr-3 font-semibold">{{ user.full_name }}</div>
            <div class="header__account--img">
                <img src="@/assets/account.png" alt="">
                <div v-if="showDropdown" class="dropdown">
                    <router-link to="/profile" class="dropdown__item">Thông tin cá nhân</router-link>
                    <div class="dropdown__item" @click="logout">Đăng xuất</div>
                </div>
            </div>
        
        </div>
    </div>
  
</template>

<script>

export default {
    
    data() {
        return {
            showDropdown: false,
            user: Object,

        };
    },
    methods: {
        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },
        logout() {
            localStorage.removeItem('user');
            localStorage.removeItem('token');
            this.$router.push('/login');
        },
    },

    mounted() {
        this.user = JSON.parse(localStorage.getItem('user'))? JSON.parse(localStorage.getItem('user')) : {};
    },


}
</script>

<style lang="scss" scoped>
@import "./Header.scss"
</style>