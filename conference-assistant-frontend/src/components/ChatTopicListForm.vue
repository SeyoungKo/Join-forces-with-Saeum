<template>
    <div class="chat-topiclist-form">
        <div class="added-topic-div">
            <ChatroomInputForm @addChatInfo="addChatInfo"/>
                <ul class="topic-list">
                    <li v-for="(t, index) in info" :key="index" v-bind="handleChatInfo(t.topic, t.roomname)">
                        <div >&nbsp;&nbsp;&nbsp;{{t.topic}}</div>
                        <hr style="border : 1px solid #eeeeee; margin-top:15px;">
                    </li>
                </ul>
                <button class="ok-btn" type="button" @click="close">OK</button>
                <CreateChatAlertModal v-if="isModalVisible" @btnok="closeModal"></CreateChatAlertModal>
        </div>
    </div>
</template>
<script>
import ChatroomInputForm from './ChatroomInputForm'
import CreateChatAlertModal from '../modal/CreateChatAlertModal'
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
    name : 'ChatTopicListForm',
    props: ['selected_teamkey'],
    components:{
        ChatroomInputForm,
        CreateChatAlertModal
    },
    created(){
        const user_key = this.user_key;
        axios.get('http://localhost:8080/rooms/'+`${user_key}`+'/'+`${team_key}`,user_key, team_key).then(res=>{
            this.roomlist = res.data
        });
    },
    data(){
        const token = localStorage.usertoken
        const decoded = jwtDecode(token)

        return{
            info:[],
            isModalVisible : false,
            roomname : '',
            topic : '',
            user_key : decoded.identity.user_key,
            team_key : this.selected_teamkey
        };
    },
    methods:{
        //***** */
        handleChatInfo(t,r){
            // this.topics.push(t);
            this.topic = t;
            this.roomname  = r;
        },
        addChatInfo(payload){
            this.info.push(payload);

            // const last = this.info.slice(-1);

            // for(var i=0; i<this.info.length; i++){
            //     for(var j=0; j<this.info[i]['topic'].length; j++){
            //         this.topics.push(this.info.roomname[i]['topic'][j]);
            //         // this.roomname = this.info.roomname[this.info.length -1];
            //     }
            // }
            // this.roomname = payload[0].roomname
        },
        close(){
            if(this.topic != '' && this.roomname !=''){

                axios.post("http://localhost:8000/rooms/enroll",{
                    roomname : this.roomname,
                    user_key : this.user_key,
                    team_key : this.team_key
                }).then((res)=>{
                    // this.$router.go(0);

                }).catch((err)=>{
                    alert('다시 시도해주세요.')
                    console.log(err)
                })
            }else{
                this.showModal()
            }
            this.$emit('submit', {
                topic : this.topic,
                roomname : this.roomname,
                roomlist : this.roomlist
            });

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
.topic-list{
   overflow-y:scroll;
}
hr{
    border :2px solid rgb(219, 219, 219);
}
.added-topic-div{
    padding-top: 10px;
    margin-bottom: 5px;
    font-size:14px;
}
.ok-btn{
    position: absolute;
    bottom : 8%;
    height: 45px;
    width: 130px;
    top:100%;
    left:55%;
    margin-top:-100px;
    margin-left:-100px;
    border-radius: 0.3rem;
    background-color: #32a852;
    font-weight: 600;
    color:white;
}
</style>