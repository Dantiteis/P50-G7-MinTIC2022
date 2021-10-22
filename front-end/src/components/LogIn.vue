<template>
<div class="wrapper2">
    <h1 class="login text-center">Iniciar Sesión</h1>
    <form class="pt-3" v-on:submit.prevent="processLogInUser" >
        <div class="form-group">
            <div class="input-field"> 
                <span class="fas fa-user p-2"></span> 
                <input type="text" v-model="user.username" placeholder="Username" required>
            </div>
        </div>
        <div class="form-group">
            <div class="input-field"> 
                <span class="fas fa-lock p-2"></span> 
                <input type="password" v-model="user.password" placeholder="Password" required>
            </div>
        </div>
        <button type="submit" class="btn btn-block text-center">Iniciar sesión</button>
    </form>
</div>
</template>




<script>
import axios from 'axios';

export default {
    name: "LogIn",

    data: function(){
        return {
            user: {
                username:"",
                password:""
            }
        }
    },

    methods: {
        processLogInUser: function(){
            axios.post(
                "https://computer-shop-mintic2022.herokuapp.com/login/", 
                this.user,  
                {headers: {}}
                )
                .then((result) => {
                    let dataLogIn = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    
                    this.$emit('completedLogIn', dataLogIn)
                })
                .catch((error) => {
                    
                    if (error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                    
                });
        }
    }
}
</script>






<style>
@import url('https://fonts.googleapis.com/css2?family=Hind:wght@300&family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Poppins&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

.wrapper2 {
  font-family:'Hind', sans-serif;
  max-width: 700px;
  border-radius: 10px;
  margin: auto !important;
  margin-top: 100px !important;
  padding: 30px 40px;
  border: 3px solid #05021f;
}

.input-field{
  border-radius: 5px;
  padding: 8px;
  display: flex;
  align-items: center;
  cursor: pointer;
  margin-bottom: 20px;
  color: #05021f;
  font-size: 17px;
  background: #F5F5F5;
  border: 1px solid #05021f;
}

.input-field:hover {
      color: #7E91C0;
      font-size: 17px;
      border: 1px solid #7E91C0	
  }

  input {

    border: none;
    outline: none;
    box-shadow: none;
    width: 100%;
    padding: 0px 2px;
    background: #F5F5F5;
    font-size: 20px;
    font-family: 'Poppins', sans-serif
}

.btn.btn-block {
  width: auto;
  margin-left: 50%;
  transform: translateX(-50%);
  flex-direction: column;
  display: flex;
  justify-content: center;
  margin-bottom: 5px;
  border-radius: 20px;
  background-color: #05021f;
  color: #fff;
  font-size: 20px;
}

  .btn.btn-block:hover {
      background-color: #7E91C0;
  }
     
.login{
  color: #05021f;
  text-align: center;
  font-size: 45px !important;
  font-family: 'Anton', sans-serif;
}

</style>
