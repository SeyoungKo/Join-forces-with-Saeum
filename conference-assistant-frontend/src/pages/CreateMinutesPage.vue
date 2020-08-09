<template>
    <div class="create-minutes-page">
        <AppHeader/>
        <SidebarMenu/>
        <v-layout column>
            <v-flex>
                <CreateMinutesForm/>
            </v-flex>
        </v-layout>
    </div>
</template>
<script>
import CreateMinutesForm from '../components/CreateMinutesForm'
import SidebarMenu from '../components/SidebarMenu'
import AppHeader from '../components/AppHeader'
export default {
    name: 'CreateMinutesPage',
    components:{
        CreateMinutesForm,
        SidebarMenu,
        AppHeader
    }
}
</script>
<style scoped>

</style>