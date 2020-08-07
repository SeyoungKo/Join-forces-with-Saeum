<template>
    <div class="chatroom-form">
        <v-container fluid class="v-container" grid-list-md style="height: 83vh;">
            <v-layout row>
                <v-flex>
                    <h3 v-if="roomname!=''">{{roomname}}</h3>
                </v-flex>
                    <v-btn class="goto-minutes-btn" type="button" @click="checkNullMessages()" v-if="roomname!=''"><router-link :to="{name:'CreateMinutesPage', params:{roomname : roomname}}">회의록 생성</router-link></v-btn>
                    <div class="p-alert" v-else>채팅 방을 선택하거나 생성해주세요.</div>

                <!-- <button type="button"><img src="../img/menu.png"></button> -->
            </v-layout>
            <br>
            <v-layout column>
                <div class="page-container">
                    <div class="textarea">
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
                        <div class="input_div">
                        <div class="file_input_div">
                            <!-- <img src="../img/fileupload.png" class="file_input_img_btn" alt="open" /> -->
                            <input type="file" name="file_1" class="file_input_hidden" onchange="javascript: document.getElementById('fileName').value = this.value"/>
                        </div>
                        <!-- <div class="chat_input_div">
                            <input type="text" v-model="message" @keyup.enter="sendMessage()" placeholder="채팅을 입력하세요."/>
                            <button @click="sendMessage()">전송</button>
                        </div> -->
                        <v-layout>
                            <v-text-field style="max-width:100%; margin-left:2%; position: absolute;" outlined placeholder="채팅을 입력하세요."></v-text-field>
                            <v-btn height="60" width="30">전송</v-btn>
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

export default {
    name: 'ChatroomForm',

    data(){
        return{
            message : '',
            messages : [],
            roomname : '',
            rtn_summary:''
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
    background-color:#e9e9e9;
    margin-bottom:20px;
    border-radius : 0.5rem;
}
.textarea{
  height: 65vh;
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
</style>