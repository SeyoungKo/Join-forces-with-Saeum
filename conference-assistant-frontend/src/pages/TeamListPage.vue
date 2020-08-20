<template>
    <div class="team-list-page">
        <AppHeader/>
        <TeamList/>
    </div>
</template>
<script>
import TeamList from '../components/TeamList'
import AppHeader from '../components/AppHeader'
export default {
    name:'TeamListPage',
    components:{
        TeamList,
        AppHeader
    }
}
</script>
<style scoped>


</style>