<template>
    <div class="app-header">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img src="../img/dure_logo.png"><span>Dure</span>
          <v-btn class="btn-logout" @click="logout()" text color="#63c29a">
      <v-icon left>mdi-logout</v-icon>로그아웃
    </v-btn>
    </div>
</template>
<script>
export default {
    name : 'AppHeader',
    methods:{
        logout(){
            localStorage.removeItem('usertoken')
            this.$router.push({name : 'Signin'})
        }
    }

}
</script>
<style scoped>
.app-header{
   position: fixed;
   top: 0;
   width: 100%;
   height: 70px;
   border-bottom: 1px solid #ededed;
   background-color: rgb(255, 255, 255);
}
img{
    margin: 13px 10px;
    width: 40px;
    height: 40px;
}
span{
    position:fixed;
    margin-top: 19px;
    font-size: 25px;
    font-weight: bold;
    color: #63c29a
}
.app-header a{
   margin-bottom: 2px;
   margin-left: 80%;
   color:black;
   width: fit-content;
}
 .btn-logout{
    margin-top: 2%;
    left: 88.5%;
    position: absolute;
}

</style>