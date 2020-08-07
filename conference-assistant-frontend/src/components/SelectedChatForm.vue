<template>
    <div class="selected-chat-form" grid-list-sm style="height: 33vh;">
        <v-container grid-list-md fluid class="v-container">
            <div v-if="clicked == false">
                <p class="p-checkinfo">키워드를 선택하면 회의 내용이 보여집니다.</p>
            </div>
            <div class="div-msg">
                <p class="p-selectedKeyword">{{selected_keyword}}</p><p class="p-msg">{{info_msg}}</p>
            </div>
            <div v-for="(m, index) in msg" :key="index">
                <span class="span-selectedUser">user1</span><p class="p-selectedMsg">{{m}}</p>
            </div>
            <p v-if="!msg.length && clicked==true" class="p-nullMsg">선택한 키워드에 대한 회의 내용이 없습니다.</p>
        </v-container>
        </div>
</template>
<script>
import {EventBus} from '../EventBus'

export default {
    name: 'SelectedChatForm',
    data(){
        return{
            selected_keyword:' ',
            key_index : '',
            info_msg : '',
            clicked : false,
            msg : '',
        }
    },
    beforeMount(){
    EventBus.$on('event', (obj)=>{
           this.selected_keyword = '\'' + obj.keyword + '\''
           this.info_msg = '에 대한 회의 내용입니다.'
           this.msg = obj.msg

           if(this.clicked == false){
               this.clicked = !this.clicked
           }
        })
    }
}
</script>
<style scoped>

.selected-chat-form{
    margin-top: 60px;
}
</style>