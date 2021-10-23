<template>
    <div class="wrapper1">
        <h1 class="text-center">Registrar clientes</h1>
        <form class="pt-3" v-on:submit.prevent="processCliente">
            <div class="form-group">
                <div class="input-field"> 
                    <span class="far fa-user p-2"></span> 
                    <input type="text" v-model="cliente.name" id="name" name="name" placeholder="Nombre" required>
                </div>
            </div>
            <div class="form-group">
                <div class="input-field">
                    <span class="fas fa-user p-2"></span>  
                    <input type="text" v-model="cliente.surname" id="surname" name="surname" placeholder="Apellido" required>
                </div>
            </div>
            <div class="form-group">
                <div class="input-field"> 
                    <span class="fas fa-phone p-2"></span>
                    <input type="tel" v-model="cliente.phone" id="phone" name="phone" placeholder="Numero telefónico" required>
                </div>
            </div>
            <div class="form-group">
                <div class="input-field"> 
                    <span class="far fa-envelope p-2"></span>
                    <input type="email" v-model="cliente.email" id="email" name="email" placeholder="Correo electrónico"> 
                </div>
            </div>
            <div class="form-group">
              <div class="input-field"> 
                  <span class="fas fa-map-marker-alt p-2"></span> 
                  <input type="text" v-model="cliente.direccion" id="direccion" name="direccion" placeholder="Dirección de residencia"> 
              </div>
            </div>
            <div class="group">
                <button type="submit" class="btn btn-enviar">Registrar cliente</button>
                <a class="btn btn-lista" @click="listCliente">Lista de clientes</a>
            </div>
            
        </form>
        <br>
        <br>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "RegistroClientes",
    data: function(){
        return {
            cliente: {
                name: "",
                surname: "",
                phone: "",
                name: "",
                email: "",
                direccion: ""
            }
        }
    },
    methods: {
        processCliente: function(){
            axios.post(
                "https://computer-shop-mintic2022.herokuapp.com/cliente/",
                this.cliente
            ).then((result) => {
                let addCliente = {
                        name: this.cliente.name,
                        surname: this.cliente.surname,
                        phone: this.cliente.phone,
                        email: this.cliente.email,
                        direccion: this.cliente.direccion,
                };
                this.$emit('completedCliente', addCliente);
                console.log(result);
                alert("El producto fue registrado de manera exitosa");

            }).catch((error) => {
                console.log(error)
                alert("Error en el resgistro.");  
            });
        },
        listCliente: function(){
            this.$router.push({name: "listClientes"})
        }
    }
}


</script>


<style >
@import url('https://fonts.googleapis.com/css2?family=Hind:wght@300&family=Montserrat&display=swap');
.wrapper1 {
  font-family:'Hind', sans-serif;
  max-width: 700px;
  margin: auto !important;
  margin-bottom: 20px !important;
  margin-top: 50px !important;
  padding: 30px 40px;
}

.group{
    width: 350px;
    margin-left: 50%;
    border-radius: 20px;
    transform: translateX(-50%);
    flex-direction: row;
    display: flex;
  justify-content: center;
}

.btn-enviar{
    margin-right: 20px;
    border-radius: 20px;
    background-color: #05021f;
    color: #fff;
    font-size: 20px;
}

.btn-lista{
   border-radius: 20px;
   border-top-right-radius: 20px;
   background-color: #05021f;
   color: #fff;
   font-size: 20px;
}

 .btn-lista:hover {
      background-color: #7E91C0;
  }

  .btn-enviar:hover {
      background-color: #7E91C0;
  }

h1 {
  color: #05021f;
  text-align: center;
  font-size: 45px !important;
  font-family: 'Anton', sans-serif;
}

</style>