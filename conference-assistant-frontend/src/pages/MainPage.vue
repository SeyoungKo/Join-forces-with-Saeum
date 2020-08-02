<template>
    <div class="main-page">
        <AppHeader/>
        <SidebarMenu/>
        <ChatroomForm/>
        <SelectedChatForm/>
        <AIManagerForm/>
        <AIKeywordListForm server="http://127.0.0.1:5000/corekeyword"></AIKeywordListForm>

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