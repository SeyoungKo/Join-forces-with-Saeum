<template>
    <div class="sign-up-page">
     <SignupForm @submit="onSubmit"/>
    </div>
</template>
<script>
import SignupForm from '../components/SignupForm'
import httpCommon from '../config/http-common'
export default {
    name:'Signup',
    components:{
        SignupForm
    }
}
</script>
<style scoped>

</style>