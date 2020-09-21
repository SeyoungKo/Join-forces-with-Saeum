<template>
  <transition name="modal-fade">
    <div class="add-team-modal">
      <v-layout class="modal" xs12 sm6 md5 lg3
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header
          class="modal-header"
          id="modalTitle"
          >
          <slot name="header">
              <div class="title">
              참여중인 팀
              <span class="phrase">이 있습니까?</span>
            </div>
            <button
              type="button"
              class="btn-close"
              @click="close"
              aria-label="Close modal"
            ></button>
          </slot>
        </header>
        <section
          class="modal-body"
          id="modalDescription"
        >
          <slot name="body">
            <v-text-field solo type="text" class="text-field" v-model="input_url" placeholder="   팀 URL을 입력해주세요."/>
          </slot>
        </section>

        <footer class="modal-footer">
          <slot name="footer">
            <button type="button" class="btn-green" @click="create" aria-label="Close modal">팀 생성하기</button>
            <button type="button" class="btn-gray" @click="close" aria-label="Close modal">OK</button>
          </slot>
        </footer>
      </v-layout>
    </div>
  </transition>
</template>

<script>
  export default {
    name: 'AddTeamModal',
    data(){
      return{
        input_url : ''
      }
    },
    methods: {
      close() {
        this.$emit('close', this.input_url);
      },
      create(){
        //  팀 생성하기 모달 창 연결
        this.$emit('create');
      }
    },
  };
</script>
<style scoped>
.modal-fade-enter,
  .modal-fade-leave-active {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .3s ease
  }
  .add-team-modal {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(143, 143, 143, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    height:40%;
    width:40%;
    margin:15%;
    border-radius: 0.5rem;
    background: rgb(235, 235, 235);
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color:#32a852;
    font-size: 23px;
    text-align:center;
    font-weight: 800;
    justify-content: space-between;
  }
.phrase{
      color:rgb(77, 77, 77);
  }
.text-field{
      margin-left:2%;
      max-width:95%;
}
  /* Device */
@media all and (max-width:765px) {
  .title{
        margin-top : 5px;
        text-align:center;
        margin-left:22.5%;
        font-size: 22px;
  }
  .modal-header,
  .modal-footer{
        margin-left: 5%;
        padding: 3px;
        display: flex;
  }
}
/* Tablet Device */
@media all and (min-width:768px) and (max-width:1024px) {
   .title{
        text-align: center;
        margin-left:22%;
        font-size: 25px;
   }
   .modal-header,
   .modal-footer{
        padding: 45px;
        display: flex;
  }
}
/* Desktop Device */
@media all and (min-width:1025px) {
  .title {
        margin-top : 6px;
        text-align: center;
        margin-left:34%;
        font-size: 28px;
  }
   .modal-header,
   .modal-footer{
        padding: 8px;
        display: flex;
  }
}
  .modal-body {
    position: relative;
    padding: 20px 10px;
  }
  p{
    margin-left: -5%;
    text-align: center;
    margin-top: -11%;
  }
  .btn-close {
    border: none;
    font-size: 100%;
    padding: 40px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

.modal-body input[type="text"]{
  margin-top: -5%;
  margin-left: 2%;
  height: 70px;
  border-radius: 0.3rem;
  width: 95%
}

button.btn-gray {
    margin-top: 7px;
    /* margin-left: 100px; */
    margin-right: 20px;
    height:50px;
    width:50%;
    background: rgb(173, 173, 173);
    font-size: 18px;
    color: #f3f2f2;
    font-weight: bold;
    border: 1px solid rgb(173, 172, 172);
    border-radius: 0.3rem;
  }
  button.btn-green {
    margin-top: 7px;
    margin-right: 10px;
    height:50px;
    width:50%;
    background: #32a852;
    font-size: 18px;
    color: #f3f2f2;
    font-weight: bold;
    border: 1px solid #32a852;
    border-radius: 0.3rem;
  }
</style>
