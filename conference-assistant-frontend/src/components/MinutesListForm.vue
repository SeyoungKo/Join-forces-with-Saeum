<template>
    <div class="minutes-list-form">
        <v-container grid-list-xl>
            <v-layout row style="margin-top: 6.5%;">
                <v-flex>
                    <v-card class="v-card-minutes">
                        <div class="clicked-minutes">
                            <div class="v-btns">
                                <v-btn large class="delete-btn" type="text">삭제</v-btn>
                                <v-btn large class="modify-btn" type="text">수정</v-btn>
                            </div>
                            <div class="clicked-contents-div">
                                <h3>회의명 : {{roomname}}&nbsp;#1</h3>
                                <h3 class="agenda-h2">회의 안건 :</h3><span>{{title}}</span>
                                <h3>회의 일시 : {{moment().format('YYYY년 MM월 DD일')}}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                &nbsp;&nbsp;&nbsp;&nbsp;13:00-14:00</h3>
                                <hr>
                                <!-- <textarea>{{contents}}</textarea> -->
                            </div>
                            <v-flex>
                                <v-card outlined class="v-card-comment">
                                    <!--sample data  -->
                                    <v-layout row>
                                        <img class="profile-img" src="../img/default_profile.png">
                                        <v-layout column >
                                            <v-card class="message-text">
                                            <p><span class="font-weight-bold"></span>&nbsp;&nbsp;댓글테스트</p>
                                            <p class="p-date">{{moment().format('MM-DD HH:mm')}}</p>
                                            <div></div>
                                            </v-card>
                                        </v-layout>
                                    </v-layout>
                                     <p class="user-name-p">&nbsp;&nbsp;user1</p>
                                      <!--sample data  -->
                                    <v-layout row>
                                        <v-text-field class="text-input" type="text" v-model="message" @keyup.enter="sendMessage()" outlined placeholder="댓글을 입력하세요."></v-text-field>
                                        <v-flex>
                                            <v-btn large class="btn-send">입력</v-btn>
                                        </v-flex>
                                    </v-layout>
                                </v-card>
                            </v-flex>
                        </div>
                    </v-card>
                </v-flex>
                <v-flex xs12 sm4 md4 lg4>
                    <v-card class="v-card-list" >
                        <h3>&nbsp;&nbsp;&nbsp;&nbsp;회의록 목록</h3>
                            <select name="minutes-sort">
                            <option value="">이름순</option>
                            <option value="등록일자">등록일자</option>
                            <option value="위치">위치</option>
                        </select>
                        <!-- sample data -->
                        <div class="minutes-list">
                            <div class="minutes-item"><p class="chatname-p">{{roomname}} #1</p>
                                <p class="content-p">{{title}} </p>
                                <p class="sub-content-p">&nbsp;&nbsp;&nbsp;&nbsp;생성일 : {{moment().format('MM-DD HH:mm')}}</p>
                            </div>
                        </div>
                        <div class="minutes-list">
                            <div class="minutes-item"><p class="chatname-p">전공종합설계 #1</p>
                                <p class="content-p">{{title}} </p>
                                <p class="sub-content-p">&nbsp;&nbsp;&nbsp;&nbsp;생성일 : {{moment().format('MM-DD HH:mm')}}</p>
                            </div>
                        </div>
                        <!--  -->
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>
<script>
import moment from 'vue-moment'
export default {
    name : 'MinutesListForm',
    created(){
        const title = this.$route.params.info.title;
        const contents = this.$route.params.info.contents;
        const roomname = this.$route.params.info.roomname;

        this.title = title;
        this.contents = contents;
        this.roomname = roomname;
    },
    data(){
        return{
            title :'',
            contents:'',
            roomname : ''
        }
    }
}
</script>
<style scoped>

/* Device */
@media all and (max-width:765px) {
    .v-card-list{
        height: 30vh;
        margin-left: 15%;
        overflow-y: scroll;
    }
    .v-card-minutes{
        margin-top: 7%;
        height: 52vh;
        margin-left: 15%;
    }
    .v-btns{
        top: 7%;
        margin-left: 45%;
    }
    .v-card-comment{
        display: none;
    }
    .clicked-contents-div{
        margin-left: 2%;
        margin-top: 18%;
        width: 95%;
    }
}
/* Tablet Device */
@media all and (min-width:768px) and (max-width:1024px) {
    .v-card-list{
        margin-top: 25%;
        margin-left: 4%;
        height: 80vh;
        overflow-y: scroll;
    }
    .v-card-minutes{
        margin-top: 12%;
        margin-left: 10%;
        height: 80vh;
    }
    .v-btns{
        top:5%;
        margin-left: 63%;
    }
    .v-card-comment{
        position: absolute;
        margin-top : 50%;
        bottom: 1%;
        height: 28vh;
        width : 96%;
        overflow-y: scroll;
    }
    .message-text{
        background-color:#f7f7f7;
        width: 87%;
        margin-left: 6%;
        padding: 1% 1% 1% 1%;
    }
    .profile-img{
        margin-top : 6%;
        margin-left: 5%;
        max-width: 7%;
        max-height: 7%;
    }
    .p-date{
        margin-left:75%;
        color: gray;
    }
    .text-input{
        width: 67%;
        margin-left: 5%;
    }
    .btn-send{
        /* margin-left: 84%; */

    }
    .clicked-contents-div{
        margin-left: 2%;
        margin-top: 15%;
        width: 95%;
    }
}
/* Desktop Device */
@media all and (min-width:1025px) {
    .v-card-list{
        height: 80vh;
        overflow-y: scroll;
    }
    .v-card-minutes{
        height: 80vh;
    }
    .v-btns{
        top: 6%;
        margin-left: 76%;
    }
    .v-card-comment{
        position: absolute;
        margin-top : 50%;
        bottom : 1%;
        height: 26vh;
        width : 98%;
        overflow-y: scroll;
    }
    .message-text{
        background-color:#f7f7f7;
        width: 90%;
        margin-left: 3%;
        padding: 1% 1% 1% 1%;
    }
    .profile-img{
        margin-top : 2%;
        margin-left: 3%;
        max-width: 7%;
        max-height: 7%;
    }
    .user-name-p{
        margin-left:1%;
    }
    .p-date{
        margin-left:85%;
        color: gray;
    }
    .text-input{
        position: absolute;
        bottom: -13%;
        margin-top : 6%;
        margin-left: 5%;
        width: 85%;
    }
    .btn-send{
        margin-top: 5%;
        margin-left: 89%;
        height: 5vh;
    }
    .clicked-contents-div{
        margin-left: 2%;
        margin-top: 8%;
        width: 95%;
    }
}

.v-btns{
    position: absolute;
    color:gray;
    transform:translate(0%, -50%);
    -webkit-transform:translate(0%, -50%);
}
h3{
    margin-top: 3%;
}
select{
    margin-left: 3%;
    margin-top: 3%;
    width: 40%;
    padding: .8em .5em;
    border: 1px solid rgb(223, 223, 223);
    font-family: inherit;
    background: url('https://api.iconify.design/mdi:menu-down.svg') no-repeat 93% 40% ;
    border-radius: 0px;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}
.minutes-item{
    margin-top:20px;
    margin-left:20px;
    padding: 3% 4% 4% 3%;
    width: 90%;
    height: fit-content;
    background-color: #f0f0f0;
    box-shadow: 4px 5px 2px rgb(223, 223, 223);
    border-radius:0.2rem;
}
.chatname-p{
    margin-bottom: 1%;
    color:rgb(39, 39, 39);
    font-weight: 600;
    font-size: 17px;
}
.clicked-contents-div{
    position: absolute;
    color:gray;
    transform:translate(0%, -50%);
    -webkit-transform:translate(0%, -50%);
    overflow-y: scroll;
}
.v-layout{
    font-size:14px;
    color:rgb(39, 39, 39);
    font-weight: 500;
    background-color:rgb(208, 222, 230);
    border-radius : 0.5rem;
}
</style>