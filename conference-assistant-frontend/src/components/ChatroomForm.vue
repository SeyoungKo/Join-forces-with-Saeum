<template>
    <div class="chatroom-form">
        <v-container fluid class="v-container">
            <v-row no-gutters>
                <h4 class="chat-title"><span v-if="roomname!=''">{{roomname}}</span></h4>
                <button class="goto-minutes-btn" type="button" @click="checkNullMessages()" v-if="roomname!=''"><router-link :to="{name:'CreateMinutesPage', params:{roomname : roomname}}">회의록 생성</router-link></button>
                <p class="p-alert" v-else>채팅 방을 선택하거나 생성해주세요.</p>
                <!-- <button type="button"><img src="../img/menu.png"></button> -->
                <div class="page-container">
                    <div class="textarea" >
                        <div class="messages" v-for="(msg, index) in messages" :key="index">
                            <div class="profile-div"><img class="profile-img" src="../img/profile.png">
                            <p class="user-name-p">user1</p></div>
                            <p><span class="font-weight-bold"></span>&nbsp;&nbsp;{{ msg.message }} </p>
                            <p class="date">{{moment().format('MM-DD HH:mm')}}</p>
                        </div>
                    </div>
                        <div class="input_div">
                        <div class="file_input_div">
                            <img src="../img/fileupload.png" class="file_input_img_btn" alt="open" />
                            <input type="file" name="file_1" class="file_input_hidden" onchange="javascript: document.getElementById('fileName').value = this.value"/>
                        </div>
                        <div class="chat_input_div">
                            <input type="text" v-model="message" @keyup.enter="sendMessage()" placeholder="채팅을 입력하세요."/>
                            <button @click="sendMessage()">전송</button>
                        </div>
                    </div>
                </div>
            </v-row>
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

</style>