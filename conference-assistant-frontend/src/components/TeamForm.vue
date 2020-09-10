<template>
    <div class="team-form">
      <v-layout column>
            <router-link clsss="router-main" :to="{name: 'MainPage', params:{teamname : teamname}}">
                <v-flex>
                    <div class="team-item" v-for="(team, index) in teamitem" :key="index" @click="selectedTeamname(team)">
                        <v-btn class="v-btn" style="height:80px;" x-large>
                            <img class="close" src="../img/close.png">
                            <v-layout row>
                                <img class="img-teamprofile" src="../img/dure_team_profile.png">
                                <v-layout column class="v-layout">
                                    <p class="team-name">{{team.name}}</p>
                                    <br>
                                    <p class="p-url">http://{{team.name}}.dure.com</p>
                                </v-layout>
                            </v-layout>
                        </v-btn>
                    </div>
                </v-flex>
            </router-link>
      </v-layout>
    </div>
</template>
<script>
import {EventBus} from '../EventBus'

export default {
    name : 'TeamForm',
    props : ['teamlist'],
    data(){
        return{
            teamname : '',
            teamitem : '',
            url : '',
            created_by : ''
        }
    },
    beforeMount(){
        EventBus.$on('teamitem',(obj)=>{
         this.teamitem = obj.teamitem
        })
    },
    methods:{
        selectedTeamname(team){
            this.teamname = team
        }
    }
}
</script>
<style scoped>
    .team-item{
        margin-top: 10px;
        margin-bottom: 20px;
        margin-left: 5%;
    }
    .img-teamprofile{
        position: relative;
        margin-left: -1%;
        width: 85px;
        height: 80px;
    }
    .close{
        position: absolute;
        margin-top: -2%;
        left: 100%;
        width: 21px;
        height: 21px;
    }
    .team-name{
        margin-left: 3%;
        position: absolute;
        margin-top: -14%;
        font-size: 22px;
        font-weight: 600;
        color:rgb(59, 59, 59);
    }
    .v-btn{
        text-transform: none !important;
        margin-left: 0;
        width: 95%;
    }
    .v-layout{
        margin-top: 30px;
        position: fixed;
        margin-left: 100px;
    }
    .p-url{
        text-decoration-line: underline;
        font-size: 14px;
    }
</style>