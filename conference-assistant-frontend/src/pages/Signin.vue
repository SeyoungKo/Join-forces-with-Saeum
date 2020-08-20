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
        sss(){
          var data = {
              test : "test"
          }
        },
        onSubmit(){
                // alert('로그인이 완료되었습니다.');
                // this.$router.push({name:'TeamListPage'})
        http
            .post("/login")
            .then(response => {
                console.log(response.data);
            })
            .catch(e => {
                console.log(e);
            });
        }
    }
}
</script>
<style scoped>
.sign-in-page{
    border : none;
}

</style>