<template>
    <div class="minutes-list-page">
        <AppHeader/>
        <SidebarMenu/>
        <v-layout column wrap>
            <MinutesListForm/>
        </v-layout>
    </div>
</template>
<script>
import MinutesListForm from '../components/MinutesListForm'
import SidebarMenu from '../components/SidebarMenu'
import AppHeader from '../components/AppHeader'
export default {
    name : 'MinutesListPage',
    components:{
        MinutesListForm,
        SidebarMenu,
        AppHeader
    }
}
</script>
<style scoped>

</style>