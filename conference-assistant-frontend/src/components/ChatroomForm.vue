<template>
    <div class="chatroom-form">
        <CreateChatroomForm v-if="isClicked" v-bind:team_key="team_key" @close="closeCreateChatroomForm" @exit="closeCreateChatroomForm"></CreateChatroomForm>
        <v-container fluid class="v-container" grid-list-md style="height: 83vh; position: relative;">
            <v-layout row>
                <v-flex>
                    <h3 v-show="roomname!=''">{{roomname}}</h3>
                </v-flex>
                    <v-btn class="goto-minutes-btn" type="button" @click="checkNullMessages()" v-if="roomname!=''"><router-link :to="{name:'CreateMinutesPage', params:{roomname : roomname}}">회의록 생성</router-link></v-btn>
                    <div class="p-alert" v-else>채팅 방을 선택하거나 생성해주세요.
                        <div><v-icon class="iconify">mdi-alert-circle-outline</v-icon></div>
                    </div>

                <!-- <button type="button"><img src="../img/menu.png"></button> -->
            </v-layout>
            <br>
            <v-layout column>
                <div class="page-container">
                    <div class="textarea" >
                        <div class="messages" v-for="(msg, index) in messages" :key="index">
                          <div>
                           <img class="profile-img" src="../img/default_profile.png">
                           <p class="user-name-p">user1</p>
                          </div>
                           <p class="message-text"><span class="font-weight-bold"></span>&nbsp;&nbsp;{{ msg.message }} </p>
                           <p class="date">{{moment().format('MM-DD HH:mm')}}</p>
                           <div></div>
                        </div>
                    </div>

                    <div class="input_div" v-if="roomname!=''">
                        <div class="file_input_div">
                            <v-file-input class="v-file" small-chips shaped label="첨부된 파일"></v-file-input>
                        </div>
                        <v-layout row class="row">
                            <v-text-field class="text-input" type="text" v-model="message" @keyup.enter="sendMessage()" outlined placeholder="채팅을 입력하세요."></v-text-field>
                            <v-flex>
                                <v-btn class="btn-send" height="55" large color="#e6e6e6" @click="sendMessage()">전송</v-btn>
                            </v-flex>
                        </v-layout>
                    </div>
                </div>
            </v-layout>
        </v-container>
    </div>
</template>
<script>
import moment from 'vue-moment';
import {EventBus} from '../EventBus'
import axios from 'axios';
import CreateChatroomForm from './CreateChatroomForm'

export default {
    name: 'ChatroomForm',
    components:{
      CreateChatroomForm
    },
    data(){
        return{
            isClicked : false,
            isClosedOn : false,
            message : '',
            messages : [],
            roomname : '',
            rtn_summary:'',
            team_key : ''
        }
    },
    methods: {
        sendMessage(){
            this.$socket.emit('SEND_MESSAGE',{
                message: this.message
            });
            this.message = ''
        },
        checkNullMessages(){
            if(this.messages.length<1){
                alert('회의를 먼저 진행해주세요.');
                return;
            }
            else{
                axios.get('http://127.0.0.1:5000/summary').then(res=>{

                    // return data
                    this.rtn_summary = res.data

                     EventBus.$emit('summary',{
                         summary : this.rtn_summary
                     });
                });

            }
        },
        closeCreateChatroomForm(){
            this.isClosedOn = !this.isClosedOn;
            this.isClicked = !this.isClicked;
        }
    },
    mounted(){
        this.$socket.on('MESSAGE', (data)=>{
            if(data.message.length !=0){
                this.messages = [...this.messages,data];

                EventBus.$emit('first',{
                     info : '회의를 시작합니다.'
                 });
            }
       });
    },
    beforeMount(){
        EventBus.$on('chatinfo', (obj)=>{
            this.roomname = obj.info.roomname;
        }),
        EventBus.$on('clickevent', (obj)=>{
            this.roomname = obj.roomname;
        }),
        EventBus.$on('clicked', (obj)=>{
            this.isClicked = obj.isClicked;
            this.team_key = obj.team_key;
        });
    }
}
</script>
<style scoped>
.chatroom-form{
    height:auto !important; /* cross-browser */
    margin-top: 60px;
}
.goto-minutes-btn{
    margin: 2% 2%;
    font-size: 14px;
    width:16%;
    text-transform: none !important;
}
a{
    text-decoration: none;
    color: #707070;
    font-weight: 600;
}
h4{
    display: inline;

}
.p-alert{
    position: absolute;
    top:40%;
    left: 30%;
    color:gray;
    transform:translate(0%, -50%);
    -webkit-transform:translate(0%, -50%);
}
.iconify{
    margin-top:3%;
    left: 45%;
    color: rgb(196, 196, 196);
}
.profile-img{
    max-width: 15%;
    max-height: 15%;
    margin-bottom: 6%;
}
.messages{
    width:60%;
    margin-left:15%;
    font-size:14px;
    color:rgb(39, 39, 39);
    font-weight: 500;
    background-color:rgb(208, 222, 230);
    margin-bottom:20px;
    border-radius : 0.5rem;
}
.textarea{
  height: 55vh;
  overflow-y:scroll;
}
.user-name-p{
    z-index: 2;
    display: inline-block;
    max-width: fit-content;
    margin-left: -13%;
    margin-bottom: 20px;

}
.profile-img{
    z-index: 2;
    margin-left: -20%;
    width:18%;
    height:18%;
}
.date{
    font-size:12px;
    color:gray;
    margin-left: 68%;
}
.message-text{
    margin-top:-16%;
}

.text-input{
    position: absolute;
    bottom : -3%;
    margin-left: 5%;
    border-radius: 0.7rem;
    border:0.3rem;
    width: 80%;
    color: #4CAF50;

}
.btn-send{
    position: absolute;
    left: 83%;
    bottom : 2.2%;
}
.v-file{
    position: absolute;
    margin-left: 2%;
    width: 0;
    bottom: 8%;
}
</style>
