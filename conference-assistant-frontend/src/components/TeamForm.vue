<template>
    <div class="team-form">
      <v-layout column>
            <router-link clsss="router-main" :to="{name: 'MainPage', params:{user_key : user_key.toString(), teamname : teaminfo.teamname.toString(), team_key : teaminfo.team_key.toString()}}">
                <v-flex>
                    <div class="team-item" v-for="(team, index) in teamitem" :key="index" @click="selectedTeamname(team.name, team.team_key)">
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
import jwtDecode from 'jwt-decode'

export default {
    name : 'TeamForm',
    props : ['teamlist'],
    data(){
      const token = localStorage.usertoken
      const decoded = jwtDecode(token)
        return{
            teaminfo : {
                teamname : '',
                team_key : '',
            },
            teamitem : '',
            url : '',
            created_by : '',
            user_key : decoded.identity.user_key
        }
    },
    beforeMount(){
        EventBus.$on('teamitem',(obj)=>{
         this.teamitem = obj.teamitem;
        })
    },
    methods:{
        selectedTeamname(name, team_key){
            this.teaminfo.teamname = name;
            this.teaminfo.team_key = team_key;

            sessionStorage.setItem("teaminfo", JSON.stringify(this.teaminfo))
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