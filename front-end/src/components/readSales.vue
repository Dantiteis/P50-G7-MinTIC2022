<template>
<div class="wrapper3 container">
  <table   class="table text-center table-bordered caption-top table-hover">
    <thead class="thead-inverse">
      <tr>
        <!-- <th sortable:true scope="col">Id</th>-->
        <th>ID</th>
        <th scope="col">idCliente</th>
        <th scope="col">idProducto</th>
        <th scope="col">cantidad</th>
        <th scope="col">fecha_venta</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(venta, index) in Ventas" :key="index">
        <!-- <td>{{ p.id }}</td>-->
        <th scope="row">{{venta.id}}</th>
        <td>{{ venta.idCliente }}</td>
        <td>{{ venta.idProducto }}</td>
        <td>{{ venta.cantidad }}</td>
        <td>{{ venta.fecha_venta }}</td>
      </tr>
    </tbody>
  </table>
  <div class="Ventas">
    <button
      class="btn btn-success btn-lg btn-block"
      v-on:click="readingSales"
      type="button"
    >
      Mostrar Ventas
    </button>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "readVentas",

  data: function() {
    return {
      Ventas: [
        {
            id: "",
            idCliente: "",
            idProducto: "",
            cantidad: "",
            fecha_venta: "",
        },
      ],
    };
  },

  methods: {
    readingSales() {
      axios
        .get(`https://computer-shop-mintic2022.herokuapp.com/registro_ventas/`)

        .then((sales) => {
          this.Ventas = sales.data;
          console.log(JSON.stringify(sales));
        })
        .catch((error) => {
          console.log(error);
          alert("Error  al momento de leer los registros");
        });
    },

    sort: function(s) {
      //if s == current sort, reverse
      if (s === this.currentSort) {
        this.currentSortDir = this.currentSortDir === "asc" ? "desc" : "asc";
      }
      this.currentSort = s;
    },
  },
};
</script>

<style>
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

.Ventas {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: bottom;
  justify-content: center;
  align-items: center;
}

.Ventas h2 {
  color: #283747;
}

.Ventas form {
  width: 90%;
}

.Ventas input {
  height: 25px;
  width: 100%;

  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;

  border: 1px solid #283747;
}

.Ventas button {
  width: 50%;
  height: 40px;

  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.Ventas button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 2px solid #283747;
}
</style>
