<template>
    <div class="team-list">
        <v-layout column>
            <v-layout row>
                <v-flex>
                    <img src="../img/profile.png" >
                    <div class="div-info" >
                        <span>
                            <h3>{{name}}</h3>
                            <br>{{email}}
                        </span>
                    </div>
                    <v-btn class="v-btn" rounded x-large color="#4CAF50" href="/Signup">프로필 변경</v-btn>
                </v-flex>
            </v-layout>
            <br><br><br><br>
            <v-flex>
                <TeamForm v-bind:teamlist="teamlist"></TeamForm>
            </v-flex>
            <button type="button" @click="showModal">팀 추가하기</button>
            <AddTeamModal v-show="isModalVisible" @close="closeModal" @create="showSecondModal"/>
            <CreateTeamModal v-if="isStatusOn"  @submit="closeSecondModal" @close="closeSecondModal"/>
        </v-layout>
    </div>
</template>
<script>
import AddTeamModal from '../modal/AddTeamModal'
import CreateTeamModal from '../modal/CreateTeamModal'
import TeamForm from './TeamForm'
import jwtDecode from 'jwt-decode'
import axios from 'axios'

export default {
    name : 'TeamList',
    components:{
        AddTeamModal,
        CreateTeamModal,
        TeamForm
    },
    data(){
        const token = localStorage.usertoken
        const decoded = jwtDecode(token)

        return{
            isStatusOn : false, // 두번째 모달 v-show
            isModalVisible: false,
            isSecondModalVisible : false,
            teamlist : [],
            id : decoded.identity.id,
            name : decoded.identity.name,
            email : decoded.identity.email,
            teamname: ''
        };
    },
    methods:{
        showModal(){
            this.isModalVisible = true;
        },
        closeModal(){
            this.isModalVisible = false;
        },
        showSecondModal(){
            this.isModalVisible = false; // 첫번째 모달 false
            this.isStatusOn = true;
            this.isModalVisible = true;
        },
        closeSecondModal(teamname){

           if(teamname !='' && teamname != null){

            var regType = /^[A-Za-z0-9+]{2,10}$/;

               if(!regType.test(teamname)){
                   alert('팀 명은 영문 혹은 영문 숫자를 혼합한 2~10자 이내 팀 명만 사용 가능합니다.')
                   return;
               }
               axios.post("http://localhost:8000/teams/enroll",{
                   teamname : teamname,
                   id : this.id

               }).then((res)=>{
                   if(res.data.duplicate){
                       alert('이미 '+teamname+'팀이 존재합니다. 다른 팀명을 입력해주세요.')
                   }else {
                        this.isStatusOn= false;
                        this.isModalVisible = false;
                        this.isSecondModalVisible = false;

                        // ** 추후 수정
                        this.teamlist.push(teamname);
                        this.teamname = teamname;
                   }
               }).catch((err)=>{
                   alert('다시 입력해주세요.')
                   console.log(err)
               })
           }else{
                this.isStatusOn= false;
                this.isModalVisible = false;
                this.isSecondModalVisible = false;
           }
        }
    }
}
</script>
<style scoped>

.team-list .router-profile{
    display:inline-block;
    background-color: #ffff;
    height: 10%;
    width: 12%;
    margin-top: -50px;
    margin-left: 80%;
    padding: 1rem;
    font-size: 19px;
    font-weight: bold;
    text-align: center;
    color: #fff;
    border-radius: 2rem;
    background-color: #32a852;
    text-decoration: none;
    transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

.team-list button[type="button"]{
    margin-left: 6%;
    position: fixed;
    bottom: 10px;
    height: 10%;
    width: 85%;
    padding: 2rem;
    font-size: 19px;
    font-weight: 700;
    text-align: center;
    color: #ffff;
    border-radius: 1rem;
    background-color: #cacaca;
}

.team-list button[type="button"]:hover{
    background-color:rgb(141, 141, 141);
    color:#fff;
}
img{
    margin-top: 112px;
    margin-left: 5%;
    max-width:100%;
}
span{
    font-size: 17px;
}
p{
    margin-left: 10%;
    margin-bottom:-15%;
    color:rgb(48, 42, 42);
    font-size: medium;
}
.div-info{
    margin-top: -5%;
    margin-left: 15%;
}

.v-btn{
    color: #fff;
    font-weight: 600;
    font-size: 17px;
    position:absolute;
    height: auto;
    max-width:120px;
    right: 10%;
}

</style>