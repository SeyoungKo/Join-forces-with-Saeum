<template>
    <div class="file-storage-form" style="position:relative; margin-top:2px;">
       <v-card class="v-card" outlined >
           <v-layout row>
            <!-- <v-select name="file-sort" solo v-model="selected" :options="options"> -->
            <select name="file-sort">
                <option value="">타입선택</option>
                <option value="등록일자">등록일자</option>
                <option value="위치">위치</option>
            </select>
            <div class="btn">
                <v-btn>다운로드</v-btn>
                <v-btn>삭제</v-btn>
            </div>
           </v-layout>
            <v-simple-table fixed-header class="table">
                <template v-slot:default>
                    <thead>
                        <tr class="table-header-tr">
                            <th style="background-color:lightgray;">작성자</th>
                            <th style="background-color:lightgray;;">파일명</th>
                            <th style="background-color:lightgray;;">위치</th>
                            <th style="background-color:lightgray;;">등록일자</th>
                            <th style="background-color:lightgray;">내려받기</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="sample in samples" :key="sample.name">
                            <td>&nbsp;{{sample.name}}</td>
                            <td>{{sample.filename}}</td>
                            <td>{{sample.location}}</td>
                            <td>{{sample.date}}</td>
                            <td>
                                <v-icon style="color:#4CAF50;">mdi-download</v-icon>
                            </td>
                        </tr>
                    </tbody>
                    <!-- <tr>
                        <td></td>
                        <td style="text-align:center; padding-left:15px; font-weight:600;">    데이터가 없습니다.</td>
                    </tr> -->
                </template>
            </v-simple-table>
       </v-card>
    </div>
</template>
<script>
export default {
    name : 'FileStorageForm',
    data(){
        return{
            samples:[
                {
                    name : 'User1',
                    filename: 'doc1',
                    location: '전공종합설계(1)',
                    date : '2020-08-01'
                },
                 {
                    name : 'User2',
                    filename: 'doc2',
                    location: '전공종합설계(2)',
                    date : '2020-08-01'
                }
            ]
        }
    }

}
</script>
<style scope>
.v-card{
    overflow-y: scroll;
}
.file-storage-form{
    position: relative;
    height:auto !important; /* cross-browser */
    top:4vh;
    margin-left: 15%;
    margin-right: -8%;
}
.v-sheet.v-card{
    height:75vh;
    width:88%;
    margin-top: 7%;
}
select{
    position: absolute;
    margin-left: 20px;
    margin-top:15px;
    width: 200px;
    padding: .8em .5em;
    border: 1px solid rgb(223, 223, 223);
    border-radius:1rem;
    font-family: inherit;
    background: url('https://api.iconify.design/mdi:menu-down.svg') no-repeat 93% 40% ;
    border-radius: 0px;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}

.table{
    position: absolute;
    top: 15%;
    margin-left: 7%;
    width:85%;
    overflow-y: scroll;
    background-color:#f5f5f5;
}

.btn{
    position: absolute;
    margin-left:83%;
    margin-top: 1%;
}
</style>