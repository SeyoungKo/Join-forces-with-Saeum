<template>
    <div class="sign-up-form">
        <!--HTML5에서 자체적인 유효성 검사를 하지 않도록 수동 설정 -->
        <v-container class="v-container" @submit.prevent="submit" novalidate>
            <v-layout column>
            <h3 style="text-align:center"><span style="color:#32a852">두레</span> 회원가입</h3>
               <v-flex class="v-flex">
                 <span>아이디 </span><br><v-text-field class="v-text-field" solo v-model="id" type="text" placeholder="아이디를 입력해주세요."/>
                 <v-btn class="v-text" small>&nbsp;&nbsp;중복확인</v-btn><br>
               </v-flex>
               <v-flex class="v-flex">
                 <span>비밀번호 </span><v-text-field class="id" solo v-model="password" type="password" placeholder="비밀번호를 입력해주세요."/><br>
                 <span>비밀번호 확인 </span><v-text-field solo v-model="passwordConfirm" type="password" class="confirm" placeholder="비밀번호를 한번 더 입력해주세요."/><br>
               </v-flex>

               <v-flex class="v-flex">
                 <span>이름 </span><v-text-field type="text" solo class="name" v-model="name" placeholder="이름을 입력해주세요."/><br>
               </v-flex>
               <v-flex class="v-flex">
                 <span>전화번호 </span><v-text-field solo type="text" class="tel" v-model="tel" placeholder="전화번호를 입력해주세요."/><br>
               </v-flex>
               <v-flex class="v-flex">
                 <span>이메일 </span><v-text-field solo type="email" v-model="email" placeholder="이메일을 입력해주세요."/>
               </v-flex>
                <v-btn class="v-btn" type="submit" large color="#4CAF50">회원가입</v-btn>
            </v-layout>
        </v-container>
    </div>
</template>
<script>
export default {
    name:'SignupForm',
    data(){
        return{
            id:'',
            password:'',
            passwordConfirm:'',
            name:'',
            tel:'',
            email:''
        }
    },
    methods:{
        submit(){
            const {id, password, passwordConfirm, name, tel, email} = this
            if(!id || !password || !passwordConfirm || !name || !tel || !email){
                alert('모든 항목을 입력해주세요.');
                return;
            }
            if(password != passwordConfirm){
                alert('비밀번호가 일치하지 않습니다.');
                return;
            }
            this.$emit('submit',{id, password, passwordConfirm, name, tel, email})
        }
    }
}
</script>
<style scoped>
.v-container{
    padding : 5% 5% 5% 5%;
    width:57%;
    height: 100%;
    background: #ffffff;
    overflow-y:hidden;
    min-height: 100vh
}
h3{
  padding-bottom: 8%;
  font-size: 150%;
}
span{
    font-weight: 600;
}
.v-flex{
    padding-bottom: 1%;
}
.v-text{
    margin-left: 85%;
}
.v-btn{
    color:#ffffff;
    font-weight: 700;
    font-size: 120%;
}
</style>