<template>
    <div class="main-page">
        <AppHeader/>
        <SidebarMenu/>
         <v-container >
      <v-layout row wrap>
        <v-flex xs12 sm6 md6 lg6>
          <v-card >
            <ChatroomForm/>
          </v-card>
        </v-flex>
        <v-flex xs12 sm6 md6 lg6>
          <v-card >
            <SelectedChatForm/>
          </v-card>
          <v-row >
            <v-col>
              <v-flex xs 24 sm12 md12 lg12>
                <v-card outlined>
                    <AIManagerForm/>
                </v-card>
              </v-flex>
            </v-col>
            <v-col>
              <v-flex xs 24 sm12 md12 lg12>
                <v-card outlined>
                    <AIKeywordListForm server="http://127.0.0.1:5000/corekeyword"></AIKeywordListForm>
                </v-card>
              </v-flex>
            </v-col>
          </v-row>
        </v-flex>

      </v-layout>
    </v-container>
    </div>
</template>
<script>
import SidebarMenu from '../components/SidebarMenu'
import ChatroomForm from '../components/ChatroomForm'
import SelectedChatForm from '../components/SelectedChatForm'
import AIKeywordListForm from '../components/AIKeywordListForm'
import AIManagerForm from '../components/AIManagerForm'
import AppHeader from '../components/AppHeader'

export default {
    name:'MainPage',
    data(){
      return{
          props: ['msgs']
      }
    },
    components:{
        SidebarMenu,
        ChatroomForm,
        SelectedChatForm,
        AIKeywordListForm,
        AIManagerForm,
        AppHeader
    }
}
</script>
<style scoped>

</style>