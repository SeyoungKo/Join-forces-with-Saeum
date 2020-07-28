<template>
    <div class="sign-up-page">
     <SignupForm @submit="onSubmit"/>
    </div>
</template>
<script>
import SignupForm from '../components/SignupForm'
export default {
    name:'Signup',
    components:{
        SignupForm
    },
    methods:{
        onSubmit(){
            // const {id, password, name, tel, email} = payload

            // api.post('/auth/signup',{id, password, name, tel, email}).then(res=>{
            //      this.$router.push({name:'Signin'})
            // }).catch(err=>{
            //     alert(err.response.data.msg) // 서버 오류
            // })
            this.$router.push({name:'Signin'})
        }
    }
}
</script>
<style scoped>

</style>