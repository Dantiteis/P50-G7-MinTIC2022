<template>

<div class="wrapper">
    <h1 class="login text-center">Registrarse</h1>
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
        <div class="form-group">
            <div class="input-field"> 
                <span class="far fa-user p-2"></span> 
                <input type="text" v-model="user.name" placeholder="Nombre" required>
            </div>
        </div>
        <div class="form-group">
            <div class="input-field"> 
                <span class="far fa-envelope p-2"></span> 
                <input type="email" v-model="user.email" placeholder="Email" required>
            </div>
        </div>
        
        <button type="button" v-on:click="processSignUp" class="btn btn-block text-center">Registrarse</button>
    </form>
</div>
</template>




<script>
import axios from 'axios';

export default {
    name: "SignUp",

    data: function(){
        return {
            user: {
                username: "",
                password: "",
                name: "",
                email: "",
                account: {
                    lastChangeDate: (new Date()).toJSON().toString(),
                    balance: 0,
                    isActive: true
                }
            }
        }
    },

    methods: {
        processSignUp: function(){
            axios.post(
                "https://computer-shop-mintic2022.herokuapp.com/user/", 
                this.user,  
                {headers: {}}
            )
                .then((result) => {
                    let dataSignUp = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    
                    this.$emit('completedSignUp', dataSignUp)
                    alert("El producto fue registrado de manera exitosa");

                    console.log(sales);
                })
                .catch((error) => {
                    console.log(error)
                    alert("Error en el resgistro.");  
                });
        }
    }
}
</script>






<style>
.wrapper{
  font-family:'Hind', sans-serif;
  max-width: 700px;
  border-radius: 10px;
  margin: auto !important;
  margin-top: 70px !important;
  padding: 7px 30px; 
  border: 3px solid #05021f;
}
.input-field{
  border-radius: 5px;
  padding: 8px;
  display: flex;
  align-items: center;
  cursor: pointer;
  margin-bottom: 10px;
  color: #05021f;
  font-size: 17px;
  background: #F5F5F5;
  border: 1px solid #05021f;
}
</style>