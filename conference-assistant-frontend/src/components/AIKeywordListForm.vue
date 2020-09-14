<template>
    <div class="aikeyword-list-form">
        <v-container fluid class="v-container" grid-list-md >
            <h4>AI가 찾은 키워드</h4>
            <div v-if="keywords && keywords.length >0">
                <div class="keywords" v-for="(keyword, index) in rtn_keywords" :key="index" v-on:click="handleSelectedKeyword(keyword, index)" >
                    <button class="btn-item" >{{keyword}}</button>
                    <template v-if="click_obj.idx == index"><br>{{click_obj.item}}</template>
                    <template v-else></template>
                </div>
            </div>
            <div v-if="keywords && keywords.length ==0">
                <div class="p-alert">AI가 발견한 키워드가 없습니다.</div>
                 <div><v-icon class="iconify">mdi-alert-circle-outline</v-icon></div>
            </div>
        </v-container>
    </div>
</template>
<script>
import SocketIo from 'socket.io-client'
import {EventBus} from '../EventBus'
import axios from 'axios'

// const APIcore = axios.create({
//     baseURL : 'http://localhost:8080/api'
// });

export default {
    name: 'AIKeywordListForm',

    data(){
        return {
            room_idx : '',
            keywords : [],
            socket : null,
            keyword : '',
            rtn_keywords : [],
            rtn_chatdata : '',
            subwords : [],
            rtn_subwords : [],
            click_obj : {
                idx : '',
                item : []
            }
        }
    },
    props:{
      server:{
          type : String,
          required : true
      }
    },
    methods:{
        newSocket(){
            let socket = SocketIo(this.$props.server,{
                origins : 'http://localhost:*/* http://127.0.0.1:*/*'
            })
            this.socket = socket
            this.socket.on('response', (data)=>{
                if(data.room_idx.length !=0){
                this.keywords = [...this.keywords,data];
                this.subwords = [...this.subwords,data];
                this.doMath(this.keywords, this.subwords);
              }
            })
        },
        doMath(keywords, subwords){
            var arr = new Array();
            var arr2 = new Array();
            var tmp_arr = new Array();

            if(this.keywords != ''){
                for(var i=0; i<this.keywords.length; i++){
                    for(var j=0; j<this.keywords[i]['mainwords'].length; j++){

                            arr= arr.concat(this.keywords[i]['mainwords'][j]);
                            let filteredArray = arr.filter((item, index)=> // 중복 제거
                                arr.indexOf(item) === index
                            );
                            this.rtn_keywords = filteredArray;
                      }
                 }
            }
            if(this.subwords !=''){
                for(var i=0; i<this.subwords.length; i++){
                    for(var j=0; j<this.subwords[i]['subwords'].length; j++){
                        arr2= this.subwords[i]['subwords'][j];

                        tmp_arr.push(arr2);
                    }
                    this.rtn_subwords = tmp_arr;
                }

            }
        },
        handleSelectedKeyword(keyword, index){

            axios.get('http://127.0.0.1:5000/keyword/'+`${keyword}`, keyword).then(res=>{

                // return data
                 this.rtn_chatdata = res.data

                 if(this.rtn_subwords!=''){
                     this.click_obj.idx = index
                     this.click_obj.item = this.rtn_subwords[index]
                 }
            });
               EventBus.$emit('event', {
                   keyword : keyword,
                   msg : this.rtn_chatdata,
                   rtn_keywords : this.rtn_keywords
               });
        }
    },
    mounted(){
        this.newSocket()
    }
}
</script>
<style scoped>
.aikeyword-list-form{
    height: 47vh;
}
.p-alert{
    position: absolute;
    top: 40%;
    left: 11%;
    color : gray;
}
.iconify{
    margin-top:58%;
    left: 43%;
    color: rgb(196, 196, 196);
}
</style>
