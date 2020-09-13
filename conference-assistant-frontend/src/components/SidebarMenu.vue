<template>
    <div class="sidebar-menu">
        <v-container>
            <!-- <img src="../img/dure_default.png"><router-link :to="{name:'MainPage'}" style="position:absolute;font-size:23px;font-weight:900">&nbsp;&nbsp;{{teamname}}</router-link>
            <span><img class="drop-menu-icon" src="../img/drop_menu.png" v-on:click="showDropMenu">
            <div v-if="isStatusOn" class="drop-menu">
                Team2<hr>
                Team3<hr>
            </div></span>
            <p>http://{{teamname}}.dure.com</p>
            <div class="route-menu">
                <router-link :to="{name:'FileStoragePage'}">업무자료</router-link><p></p>
                <p><router-link :to="{name:'TimelinePage'}">타임라인</router-link></p>
                <p><router-link :to="{name:'MinutesListPage'}">회의록</router-link></p>
                <p><router-link :to="{name:'Signin'}">&nbsp;&nbsp;&nbsp;&nbsp;- 회의록 목록</router-link></p>

            </div>
            <hr>
            <div class="online-userlist">
                <h5>이 팀에 소속된 팀원</h5>
                <img src="../img/offline.png"><button type="button" class="btn"  @mouseover="isActive= true" @mouseleave="isActive= false">{{name}}</button><br>
                    <ShowProfileForm v-bind:propsname="name" v-show="isActive"></ShowProfileForm>
                <img src="../img/offline.png"><button type="button" class="btn">user2</button>
            </div>
            <div class="chat-list">
                <h5>채팅방 목록<span><button type="button" class="img-button"><img src="../img/chat_add.png" @click="showCreateChatroomForm" ></button></span></h5>
                <div class="div-roominfo" v-for="(chatlist, index) in chatlist" :key="index" >
                    <button class="btn-chatitem" @click="showSelectedChatroom(chatlist)">{{chatlist}}</button>
                    <img @click="exitSelectedChatroom(chatlist)" class="img-close" src="../img/close_white.png"/>
                </div>
                <CreateChatroomForm v-if="isClicked" @close="closeCreateChatroomForm" @exit="closeCreateChatroomForm"></CreateChatroomForm>
            </div> -->

            <v-navigation-drawer class="v-navigation-drawer" permanent expand-on-hover>
                <v-list>
                    <v-list-item class="list-item" >
                    <v-list-item-avatar class="list-item-avatar">
                        <img class="img-profile" src="../img/default_profile.png" @mouseover="isActive= true" @mouseleave="isActive= false"/>
                        <!-- <ShowProfileForm v-bind:propsname="name" v-show="isActive"></ShowProfileForm> -->
                    </v-list-item-avatar>
                    </v-list-item>

                    <v-list-item class="list-item2" link>
                    <v-list-item-content class="list-content" >
                        <v-list-item-title class="title">User1</v-list-item-title>
                    </v-list-item-content>
                    </v-list-item>

                    <v-list-item class="list-team" link>
                        <v-list-item-content>
                            <v-list-item-title style="color:white;">{{teamname}}
                                <v-list-item-icon>
                                    <v-icon medium style="color:lightgray;">mdi-account-multiple</v-icon>
                                </v-list-item-icon>

                                <v-icon v-on:click="showDropMenu" large>mdi-menu-down</v-icon>
                                <v-list class="drop-list" style="background-color:white;"  v-if="isStatusOn" >
                                    <!-- Team name sample data -->
                                    <v-list-item v-for="(item, index) in items" :key="index">
                                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                                    </v-list-item>
                                    <!--  -->
                                </v-list>
                            </v-list-item-title>
                            <v-list-item-subtitle style="color:white;">http://{{teamname}}.dure.com</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                <v-divider></v-divider>

                <!-- <v-list-item link>
                    <v-list-item-icon>
                    <v-icon medium style="color:lightgray;">mdi-home</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>홈</v-list-item-title>
                </v-list-item> -->

                <v-list-item link>
                    <v-list-item-icon>
                        <v-icon medium style="color:lightgray;">mdi-align-horizontal-left</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>
                        &nbsp;&nbsp;<router-link :to="{name:'TimelinePage'}">타임라인</router-link>
                    </v-list-item-title>
                </v-list-item>

                <v-list-item link>
                    <v-list-item-icon>
                        <v-icon style="color:lightgray;">mdi-file</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>
                        &nbsp;&nbsp;<router-link :to="{name:'FileStoragePage'}">업무자료</router-link>
                    </v-list-item-title>
                </v-list-item>

                <v-list-item link>
                    <v-list-item-icon>
                        <v-icon style="color:lightgray;">mdi-record</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>
                        &nbsp;&nbsp;<router-link :to="{name:'MinutesListPage'}">회의록</router-link>
                    </v-list-item-title>
                </v-list-item>

                <br><br><br>
                <v-divider></v-divider>

                <v-list-item>
                    <v-list-item-title>
                        <div class="chat-list">
                            <br>
                            <v-icon style="color:lightgray;">mdi-chat</v-icon>&nbsp;&nbsp;채팅방 목록
                            <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <button type="button" class="img-button"><img src="../img/chat_add.png" @click="showCreateChatroomForm()" ></button>
                            </span>

                            <div class="div-roominfo" v-for="(chatlist, index) in chatlist" :key="index" >
                                <button class="btn-chatitem" @click="showSelectedChatroom(chatlist)">{{chatlist}}</button>
                                <img @click="exitSelectedChatroom(chatlist)" class="img-close" src="../img/close_white.png"/>
                            </div>
                        </div>
                    </v-list-item-title>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </v-container>
</div>
</template>
<script>
import ShowProfileForm from './ShowProfileForm'
import CreateChatroomForm from './CreateChatroomForm'
import {EventBus} from '../EventBus'

export default {
    name: 'SidebarMenu',
    components:{
      ShowProfileForm,
      CreateChatroomForm
    },
    created(){
      const teamname = this.$route.params.teamname;
      const team_key = this.$route.params.team_key;
      this.teamname = teamname;
      this.team_key = team_key;
    },
    data(){
        return {
            isStatusOn : false,
            isActive : false,
            name : 'user1',    // sample user,
            isClicked : false,
            isClosedOn : false,
            chatlist : '',
            teamname : '',
            team_key : '',

            //sample data
            items: [
                { title: 'Click Me' },
                { title: 'Click Me' },
                { title: 'Click Me' },
                { title: 'Click Me 2' },
            ],
        };
    },
    methods:{
        showDropMenu(){
            this.isStatusOn = !this.isStatusOn;
        },
        showCreateChatroomForm(){
            // 채팅방 생성하기
            this.isClicked = !this.isClicked;
            EventBus.$emit('clicked',{
                isClicked : this.isClicked,
                // team key 전달
                team_key : this.team_key
            });
        },
        showSelectedChatroom(roomname){

            EventBus.$emit('clickevent', {
                roomname : roomname,
                topic : localStorage.getItem(roomname)
            });
        },
        exitSelectedChatroom(roomname){

            localStorage.removeItem(roomname);
            alert('\''+roomname+'\''+' 채팅방이 삭제되었습니다.');

            // manually reload current page
            this.$router.go(0);
        }
    },
    beforeMount(){
        EventBus.$on('chatinfo',(obj)=>{
            this.chatlist= obj.roomlist;
        });
        // for(var i=0; i<localStorage.length; i++){
        //     this.chatlist.push(localStorage.key(i));
        // }
    }
}
</script>
<style scoped>

.v-navigation-drawer{
    position:fixed;
    z-index: 1;
    top:0;
    left:0;
    height: 100%;
    background-color: #32a852
}
.img-profile{
    width:55px;
    height:45px;
}
.list-item{
    position: absolute;
}
.list-item .list-item-avatar{
    margin-left: -20%;
}
.list-item2 .list-content{
    margin:50px 50px;
    position:absolute;
    color: white;
}
.drop-list{
    z-index : 1;
    position:fixed;
    margin-left:5%;
}
.list-team{
    position: relative;
}
.title{
    font-size:20px;
    margin-top:5px;
    font-weight: 500;
}
a{
    margin-top: 10%;
    color:white;
    text-decoration: none;
    font-weight: bold;
}
.drop-menu{
    margin-top:15px;
    width:140px;
    border-radius: 0.3rem;
    height:150px;
    font-size: 17px;
    padding-top: 5px;
    color:rgb(66, 66, 66);
    font-weight: 500;
    text-align:center;
    background-color: rgba(240, 240, 240, 0.952);
}
.sidebar-menu span{
    position: fixed;
    margin-top: 1.5%;
    color:white;
    font-weight:900;
    font-size: 23px;
}
.sidebar-menu p:nth-of-type(1){
    position: fixed;
    margin-top: -2%;
    margin-left: 77px;
    font-size: 12.5px;
    font-weight:600;
    color: white;
}
.route-menu{
    margin-top: 12%;
    margin-left: 10%;
    font-size: 28px;
    color:white;
}
hr{
    margin-top: 8%;
    border:1px solid rgb(131, 131, 131);
    width: 93%;
    opacity: 0.3;
}
.online-userlist h5{
    margin-top: 5%;
    margin-left: 9%;
    margin-bottom: 0;
    font-size: 15px;
    color:white;
}
.online-userlist p{
    color:white;
}
.online-userlist img{
    margin-left: 12%;
    height:8px;
    width:8px;
}
.online-userlist button{
    margin-left: 4%;
    margin-bottom: 0;
    color:white;
    background:#32a852;
    cursor: pointer;
}
.chat-list{
    color: white;
    font-weight: 600;
}
.chat-list h5{
    margin-top: 45%;
    margin-left: 9%;
    font-size: 15px;
    color:white;
}

.chat-list h5 button.img-button{
    margin-top: -50px;
    margin-left: 160%;
    border:none;
    height:50px;
    width: 50px;
    background:transparent;
}
button.img-button img{
    height:23px;
    width:23px;
}

.drop-menu-icon{
    margin-left:120px;
    width: 15px;
    height: 10px;
}

.div-roominfo{
    padding-left: 2rem;
}
.img-close{
    margin-left: 10px;
    width:9px;
    height:9px;
}
.btn-chatitem{
    background: transparent;
    text-decoration: underline;
    font-size:14px;
    color:#ffff;
    font-weight: 500;
}
</style>

