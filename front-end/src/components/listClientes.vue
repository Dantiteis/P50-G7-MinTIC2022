<template>
    <div class="wrapper3 container">
        <table   class="table text-center table-bordered caption-top table-hover">
          <caption><h1>Clientes</h1></caption>
          <thead class="thead-inverse ">
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Apellido</th>
              <th>Numero telefónico</th>
              <th>Correo electrónico</th>
              <th>Dirección</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(cliente, index) in cliente" :key="index">
              <th scope="row">{{cliente.id}}</th>
              <td>{{cliente.name}}</td>
              <td>{{cliente.surname}}</td>
              <td>{{cliente.phone}}</td>
              <td>{{cliente.email}}</td>
              <td>{{cliente.direccion}}</td>
              <td>
                <div class="group-accion">
                <button class="btn eliminar" type="submit" @click="deleteCliente(cliente.id)">Eliminar</button>
                
            </div>
              </td>
            </tr>
          </tbody>
        </table>
        <br>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "listClientes",
    data: function(){
      return {
        cliente: []
      }
    },
    created () {
      axios.get("https://computer-shop-mintic2022.herokuapp.com/cliente/")
      .then((client) => {
          this.cliente= client.data;
      })
  },
  methods: {
    deleteCliente(id) {
      let idCliente = 1;
      axios.delete(
          `https://computer-shop-mintic2022.herokuapp.com/cliente/${id}`,
          this.cliente
        )
        .then((result) => {
          this.cliente = result;
          alert("El cliente fue eliminado de manera exitosa");
          this.$router.push({name: "listClientes"})
          axios.get("https://computer-shop-mintic2022.herokuapp.com/cliente/")
          .then((client) => {
            this.cliente= client.data;
            })
        })
        .catch((error) => {
          console.log(error.result);
          alert("El cliente no pudo ser eliminado");
        });
    }, 
  } 
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz&display=swap');

.wrapper3 {
  align-items: center !important;
  justify-content: center;
  margin-top: 35px !important;
  font-family:'Hind', sans-serif;
  max-width: auto !important;
  margin-bottom: 25px !important;
  margin: auto;
  padding: 30px 40px;
}

.table {
  align-items: center;
  justify-content: center;
  border: 2px solid #586da1!important;
  font-size: 15px !important;
  font-family: 'Montserrat', sans-serif !important;
}

.table thead th {
  align-items: center;
  justify-content: center;
  border: 2px solid #586da1!important;
  color: #05021f;
  font-family: 'Yanone Kaffeesatz', sans-serif !important;
  font-size: 20px !important;
}

.table td, th {
  align-items: center;
  justify-content: center;
  border: 2px solid #586da1!important;
}
.group-accion{
    width: auto;
    margin-left: 50%;
    transform: translateX(-50%);
    flex-direction: row;
    display: flex;
    justify-content: center;
}
.eliminar{
   margin-right: 5px;
    border-radius: 20px;
    background-color: #05021f;
    color: #fff;
    font-size: 12px;
}

.editar{
   border-radius: 20px;
   border-top-right-radius: 20px;
   background-color: #05021f;
   color: #fff;
   font-size: 12px;
}

 .eliminar:hover {
      background-color: #7E91C0;
  }

  .editar:hover {
      background-color: #7E91C0;
  }
</style>