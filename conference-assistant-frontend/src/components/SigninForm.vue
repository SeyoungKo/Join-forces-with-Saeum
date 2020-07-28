<template>
    <div class="sign-in-form">
        <form @submit.prevent="submit">
           <v-container class="v-container">
            <h3 class="h3-header">로그인</h3>
              <v-layout column>
                <v-flex xs12 sm6 md3>
                    <v-text-field solo type="text" class ="v-text-id" v-model="id"  placeholder="아이디를 입력하세요."></v-text-field>
                </v-flex>

                <v-flex>
                    <v-text-field solo type="password" v-model="password" placeholder="비밀번호를 입력하세요."/>
                </v-flex>
              </v-layout>

               <v-flex>
                <input type="checkbox"/><span> 로그인 상태 유지</span>
               </v-flex>

               <v-btn class="btn-txt" rounded x-large color="#4CAF50" type="submit" value="Login">Login</v-btn>

               <v-flex>
                <v-btn text small type="button" class="btn" @click="showModal">비밀번호가 생각나지 않으세요?</v-btn>
               </v-flex>

               <FindpasswordModal v-show="isModalVisible" @close="closeModal"/>

               <v-flex>
                <v-btn class="btn-txt" rounded x-large color="#4CAF50" ><router-link :to="{name:'Signup'}" class="join-btn">Join</router-link></v-btn>
               </v-flex>
           </v-container>
       </form>
    </div>
</template>
<script>
import FindpasswordModal from '../modal/FindpasswordModal'

export default {
name: 'SigninForm',
    components:{
        FindpasswordModal
    },
    data(){
        return{
            id:'',
            password:'',
            isModalVisible: false
        };
    },
    methods:{
        submit(){
            const {id,password} = this;
            this.$emit('submit',{id,password})
        },
        showModal(){
            this.isModalVisible = true;
        },
        closeModal(){
            this.isModalVisible = false;
        }
    }
}
</script>
<style scoped>
.v-container{
    padding : 5% 5% 5% 5%;
    margin-top:8%;
    width:50%;
    background: #ffffff;
}
.btn-txt{
    padding :0;
    padding : 10% 10%;
    margin-top:3%;
    margin-left:20%;
    font-weight: 800;
    font-size: 17px;
    color: #ffffff;
    width:50%;
    text-transform: none !important;

}
.btn{
    width:90%;
}
a{
    font-weight: 800;
    font-size: 17px;
    text-decoration:none;
    color:#ffffff;
}
.h3-header{
    position:flex;
    margin-bottom: 8%;
    text-align:center;
    font-size: 26px;
}
</style>