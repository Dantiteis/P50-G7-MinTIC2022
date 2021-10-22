<template>
<div>
  <b-table
    :sort-by="sortBy"
    :sort-desc="sortDesc"
    sort-icon-left
    responsive="sm"
    class="table table-striped table-hover"
  >
    <thead class="thead-dark">
      <tr>
        <!-- <th sortable:true scope="col">Id</th>-->
        <th scope="col">idCliente</th>
        <th scope="col">idProducto</th>
        <th scope="col">cantidad</th>
        <th scope="col">fecha_venta</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(p, index) in Ventas" :key="index">
        <!-- <td>{{ p.id }}</td>-->
        <td>{{ p.idCliente }}</td>
        <td>{{ p.idProducto }}</td>
        <td>{{ p.cantidad }}</td>
        <td>{{ p.fecha_venta }}</td>
      </tr>
    </tbody>
  </b-table>
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
  name: "readSales",

  data: function() {
    return {
      Ventas: [
        {
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
