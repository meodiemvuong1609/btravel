<template>
    <div class="container mx-auto">
        <div class="form flex ">
            <div class="form__logo">
                <img src="@/assets/mini_logo.png" alt="">
            </div>
            <div class="form__title">Đăng nhập</div>
            <div class="form__input">
                <p>Số điện thoại</p>
                <input type="text" v-model="phone" placeholder="Số điện thoại" />
            </div>
            <div class="form__input">
                <p>Mật khẩu</p>
                <input type="password" v-model="password" placeholder="Mật khẩu" />
            </div>
            <div class="form__button">
                <button @click="handleLogin">Đăng nhập</button>
            </div>
            <router-link to="/forgot" class="form__forgot">Quên mật khẩu?</router-link>
        </div>
    </div>
</template>

<script>
import HTTP from '@/HTTP/HTTP.js'
export default {
    name: 'LoginView',
    data () {
        return {
            phone: '',
            password: '',
            message: null,
            loading: false
        }
    },
    methods: {
        async handleLogin () {
            if (this.phone === '' || this.password === '') {
                this.message = 'Vui lòng nhập đầy đủ thông tin'
                this.loading = false
                return
            }
            this.loading = true
            let response = await HTTP.post('/account/api/login/', {
                phone: this.phone,
                password: this.password
            })
            if (response.status === 200) {
                this.message = 'Đăng nhập thành công'
                this.loading = false
                localStorage.setItem('token', response.data.data.token)
                localStorage.setItem('user', JSON.stringify(response.data.data.user))
                this.$router.push('/')
            } else {
                this.message = 'Đăng nhập thất bại'
                this.loading = false
            }
        }
    }
    

}
</script>

<style lang="scss" scoped>
@import "@/scss/LoginView.scss";
</style>