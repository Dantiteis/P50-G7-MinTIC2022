<template>
  <div class="wrapper4">
    <h1 class="text-center">Registro de Venta</h1>
    <div class="form-group">
      <div class="input-field"> 
        <span class="fas fa-id-card-alt fa-sm p-2"></span> 
        <input type="text" v-model="registroVenta.idCliente" placeholder="Id del cliente" required>
      </div>
    </div>
    <div class="form-group">
      <div class="input-field"> 
        <span class="fas fa-shopping-cart fa-sm p-2"></span> 
        <input type="text" v-model="registroVenta.idProducto" placeholder="Id del producto" required>
      </div>
    </div>
    <div class="form-group">
      <div class="input-field"> 
        <span class="fa fa-hashtag fa-sm p-2"></span> 
        <input type="number" v-model="registroVenta.cantidad"  placeholder="Cantidad de unidades">
      </div>
    </div>
    <div class="form-group">
      <label for="fecha">Fecha de compra</label>
      <div class="input-field"> 
        <input type="date" v-model="registroVenta.date" id="fecha" required>
      </div>
    </div>

    <div class="group2">
      <button type="button" class="btn btn-enviar text-center" v-on:click="AddingSale">Registrar Venta</button>
      <button type="button" class="btn btn-enviar text-center" v-on:click="loadSales">Ver todas las ventas</button>
    </div>
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
    }
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

.wrapper4 {
  font-family:'Hind', sans-serif;
  max-width: 700px;
  border-radius: 10px;
  height: auto;
  margin: auto !important;
  margin-top: 80px !important;
  padding: 30px 40px;
  border: 3px solid #05021f;
}

label{
  font-size: 20px;
  padding: 0px 2px;
  font-family: 'Poppins', sans-serif
}
.group2{
  width: 600px;
    margin-left: 50%;
    border-radius: 20px;
    transform: translateX(-50%);
    flex-direction: row;
    display: flex;
    margin-top: 15px;
    margin-bottom: -10px !important;
  justify-content: center;
}

</style>