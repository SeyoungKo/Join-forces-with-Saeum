<template>
    <div class="file-storage-page">
        <SidebarMenu/>
        <AppHeader/>
        <v-container>
          <v-flex xs12 sm12 md12 lg12>
                <FileStorageForm/>
          </v-flex>
        </v-container>
    </div>
</template>
<script>
import FileStorageForm from '../components/FileStorageForm'
import SidebarMenu from '../components/SidebarMenu'
import AppHeader from '../components/AppHeader'
export default {
    name : 'FileStoragePage',
    components:{
        FileStorageForm,
        SidebarMenu,
        AppHeader
    }
}
</script>
<style scoped>

</style>