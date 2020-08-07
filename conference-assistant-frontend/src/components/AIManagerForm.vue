<template>
    <div class="aimanager-form" style="height: 47vh;">
            <!-- <img src="../img/ai.png"> -->
            <h4>회의 매니저&nbsp;&nbsp;&nbsp;
                <toggle-button v-if="flag==true" @change="onChangeEventHandler" :value="true" :labels="{checked: 'ON', unchecked:'OFF'}"></toggle-button>
                <toggle-button v-else-if="flag==false" :disabled=true :value="true" :labels="{checked: 'ON', unchecked:'OFF'}"></toggle-button>
            </h4>
        <div v-if="onChanged==true && flag==true" class="welcome-div">
                <p class="info-p"> '{{ res_roomname }}' 주최자는 user1<br>참여 예정자는 user2, user3입니다.
                    <br><br>
                    오늘의 주요 안건은 {{res_topic}} 입니다.
                </p>
                <div v-for="(start, index) in start_msg" :key="index" >
                    <p class="start-div">{{start}}</p>
                    <p class="start-div"> 회의 시작 일시는 {{ moment().format('YYYY년 MM월 DD일 HH:mm')}} 입니다.</p>
                </div>
                <div v-if="add != '' && add_msg !=''">
                    <p>{{add_msg}}</p>
                </div>
        </div>
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

</style>