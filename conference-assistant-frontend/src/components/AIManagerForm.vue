<template>
    <div class="aimanager-form" style="position:relative; min-height: 47vh;">
            <!-- <img src="../img/ai.png"> -->
            <h4>회의 매니저&nbsp;&nbsp;&nbsp;
                <toggle-button v-if="flag==true" @change="onChangeEventHandler" :value="true" :labels="{checked: 'ON', unchecked:'OFF'}"></toggle-button>
                <toggle-button v-else-if="flag==false" :disabled=true :value="true" :labels="{checked: 'ON', unchecked:'OFF'}"></toggle-button>
            </h4>
        <v-layout column class="v-layout-col" style="position: absolute; margin-top:20%;">
             <div v-if="onChanged==true && flag==true" class="welcome-div">
                <p class="info-p"> '{{ res_roomname }}' 주최자는 user1<br>참여 예정자는 user2, user3입니다.
                    <br><br>
                    오늘의 주요 안건은 {{res_topic}} 입니다.
                </p>
             </div>
                <v-flex v-if="onChanged==true && flag==true">
                    <div v-for="(start, index) in start_msg" :key="index" >
                        <p class="start-div">{{start}}</p>
                        <p class="start-div"> 회의 시작 일시는 {{ moment().format('YYYY년 MM월 DD일 HH:mm')}} 입니다.</p>
                    </div>
                    <div v-if="add != '' && add_msg !=''">
                        <p>{{add_msg}}</p>
                    </div>
                </v-flex>
        </v-layout>
    </div>
</template>
<script>
import moment from 'vue-moment';
import { EventBus } from '../EventBus';
export default {
    name : 'AIManagerForm',
    data(){
        return{
            onChanged : true,
            start_msg : '',
            event : '',
            res_roomname: '',
            res_topic: '',
            flag : false,
            add : '',
            add_msg : ''
        }
    },
    methods : {
        onChangeEventHandler(){
            this.onChanged = !this.onChanged;
        }
    },
    beforeMount(){
        EventBus.$on('chatinfo', (obj)=>{

            this.res_topic = obj.info.topic
            this.res_roomname = obj.info.roomname

            this.flag = true;

        });
        EventBus.$on('clickevent',(obj)=>{
            this.res_roomname = obj.roomname
            this.res_topic = obj.topic
            this.flag = true
        });
        EventBus.$on('addEvent',(obj)=>{
            this.add = obj.add
        })
    },
    mounted(){
        if(this.add!=''){
            this.add_msg= '새로운 회의록이 등록되었습니다.'
        }
        this.event = EventBus;

        this.event.$on('first', (info)=>{
            this.start_msg = info
        });
    }
}
</script>
<style scoped>
.aimanager-form{
    overflow-y: scroll;
}
h4{
    position: absolute;
    top: 4%;
    left: 5%;
    font-size: 20px;
    font-weight: 700;
}
.welcome-div{
    top: 20%;
    padding: 8px 3px 3px 10px;
    font-size: 14px;
    font-weight: 500;
    background: rgb(253, 239, 199);
    color:rgb(51, 51, 51);
    width: 90%;
    margin-left: 5%;
    height: fit-content;
    border-radius: 0.2rem;
    box-shadow: 4px 4px 2px rgb(204, 204, 204);
}
.start-div{
    padding: 8px 3px 3px 10px;
    font-size: 14px;
    font-weight: 500;
    background: rgb(253, 239, 199);
    color:rgb(51, 51, 51);
    margin-left: 1%;
    margin-bottom: 3%;
    width: 97%;
    border-radius: 0.2rem;
    box-shadow: 4px 4px 2px rgb(204, 204, 204);
}

</style>