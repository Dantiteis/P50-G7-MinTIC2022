<template>
  <div class="wrapper2">
    <h1 class="login text-center">Registro de Venta</h1>
    <form v-on:submit.prevent="AddingSale">
      <div class="form-group">
        <label for="clienteName">ID del cliente</label>
        <input type="number" class="form-control" id="clienteName" v-model="registroVenta.idCliente" placeholder="ingrese el id del cliente" required>
        <!--<small id="emailHelp" class="form-text text-muted">nombre sin rellenar</small>-->
      </div>
      <div class="form-group">
        <label for="productName">ID del producto</label>
        <input type="number" class="form-control" id="productName" v-model="registroVenta.idProducto" placeholder="ingrese el id del producto" required>
      </div>
      <div class="form-group">
          <label for="amount">Cantidad</label>
          <input type="number" class="form-control" id="amount" v-model="registroVenta.cantidad" placeholder="ingrese la cantidad" required>
      </div>
      <div class="form-group">
          <label for="dateInput">fecha</label>
          <input type="text" class="form-control" id="dateInput" v-model="registroVenta.date" placeholder="ingrese el Producto" required>
      </div>
      <button type="button" class="btn btn-block text-center" v-on:click="AddingSale">Registrar Venta</button>
       <button type="button" class="btn btn-block text-center" v-on:click="loadSales">Ver todas las ventas</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "registroVenta",
  data: function(){
    return {
      registroVenta: {
        idCliente: "",
        idProducto: "",
        cantidad: "",
        fecha_venta: "",
      },
    };
  },
  methods: {
    AddingSale: function() {
      axios
        .post(
          `https://computer-shop-mintic2022.herokuapp.com/registro_ventas/`,
          this.registroVenta,
          { headers: {} }
        )
        .then((sales) => {
          let addSale = {
            idCliente: this.registroVenta.idCliente,
            idProducto: this.registroVenta.idProducto,
            cantidad: this.registroVenta.cantidad,
            fecha_venta: this.registroVenta.fecha_venta,
          };
          this.$emit("addedSale", addSale);
          alert("La venta fue registrada de manera exitosa");

          console.log(sales);
          this.clearForm();
        })
        .catch((error) => {
          console.log(error);
          alert("Error  al momento de registrar los datos de la venta.");
        });
    },

    clearForm: function() {
      this.idCliente = ''
      this.idProducto = ''
      this.cantidad = ''
      this.fecha_venta = ''
    },

    loadSales: function() {
      this.$router.push({ name: "readSales" });
    },
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
    margin-top: 80px !important;
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
    margin-top: 10px;
    margin-left: 50%;
    transform: translateX(-50%);
    flex-direction: column;
    display: flex;
    justify-content: center;
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