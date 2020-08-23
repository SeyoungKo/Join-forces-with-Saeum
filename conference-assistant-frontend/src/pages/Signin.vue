<template>
    <v-layout column class="sign-in-page">
        <v-flex>
            <SigninForm @submit="onSubmit"/>
        </v-flex>
    </v-layout>
</template>
<script>
import SigninForm from '../components/SigninForm'
import http from '../config/http-common'

export default {
    name:'Signin',
    components:{
        SigninForm
    },
    methods:{
    }
}
</script>
<style scoped>
.sign-in-page{
    border : none;
}

</style>