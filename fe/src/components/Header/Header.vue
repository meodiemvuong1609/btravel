<template>
    <div class="header" :class="{ 'open': showDropdown }">
        <div class="header__logo">
            <img src="https://f004.backblazeb2.com/file/warehousebinh/logokiot/kiot_logo.png" alt="">
        </div>
        <div class="header__menu">
            <router-link to="/orders" class="header__menu--item">Đơn hàng</router-link>
            <router-link to="/products" class="header__menu--item">Sản phẩm</router-link>
            <router-link to="/partners" class="header__menu--item">Đối tác</router-link>
            <router-link to="/employees" class="header__menu--item">Nhân viên</router-link>
        </div>
        <div class="header__account" @click="toggleDropdown">
            <div class="header__account--img">
                <img src="@/assets/account.png" alt="">
                <div v-if="showDropdown" class="dropdown">
                    <div class="dropdown__item">Thông tin cá nhân</div>
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
        };
    },
    methods: {
        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },
        logout() {
            console.log('User logged out.');
        },
    },

}
</script>

<style lang="scss" scoped>
@import "./Header.scss"
</style>