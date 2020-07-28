<template>
    <v-layout column class="sign-in-page">
        <v-flex>
            <SigninForm @submit="onSubmit"/>
        </v-flex>
    </v-layout>
</template>
<script>
import SigninForm from '../components/SigninForm'
// import {mapActions} from 'vuex'
export default {
    name:'Signin',
    components:{
        SigninForm
    },
    methods:{
        onSubmit(){
                alert('로그인이 완료되었습니다.');
                this.$router.push({name:'TeamListPage'})
        }
    }
}
</script>
<style scoped>
.sign-in-page{
    border : none;
}

</style>