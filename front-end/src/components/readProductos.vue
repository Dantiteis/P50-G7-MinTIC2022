<template>
<div class="wrapper3 container">
  <table :sort-by="sortBy" :sort-desc="sortDesc" sort-icon-left responsive="sm" class="table text-center table-bordered caption-top table-hover">
    <caption><h1>Productos</h1></caption>
    <thead class="thead-inverse">
      <tr>
        <!-- <th sortable:true scope="col">Id</th>-->
        <th>Modelo</th>
        <th>Tipo</th>
        <th>Entradas</th>
        <th>Salidas</th>
        <th>Tamaño pantalla</th>
        <th>Resolución pantalla</th>
        <th>Batería</th>
        <th>Software</th>
        <th>Tipo disco</th>
        <th>Capacidad del disco</th>
        <th>Memoria RAM</th>
        <th>Procesador</th>
        <th>Precio</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(p, index) in producto" :key="index">
        <!-- <td>{{ p.id }}</td>-->
        <td>{{ p.modelo }}</td>
        <td>{{ p.tipo }}</td>
        <td>{{ p.entradas }}</td>
        <td>{{ p.salidas }}</td>
        <td>{{ p.pantalla_tamaño }}</td>
        <td>{{ p.pantalla_resolucion }}</td>
        <td>{{ p.bateria }}</td>
        <td>{{ p.software_incluido }}</td>
        <td>{{ p.tipo_disco }}</td>
        <td>{{ p.capacidad_disco }}</td>
        <td>{{ p.memoria_ram }}</td>
        <td>{{ p.procesador }}</td>
        <td>{{ p.precio }}</td>
      </tr>
    </tbody>
  </table>
  <div class="producto">
    <button class="btn btn-block" v-on:click="loadProduct" type="button">Detalle
    </button>
  </div>
  <br>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "readProducts",

  data: function() {
    return {
      sortBy: "id",
      sortDesc: false,
      fields: [{ key: "Id", sortable: true }],

      producto: [
        {
          id: "",
          modelo: "",
          tipo: "",
          entradas: "",
          salidas: "",
          pantalla_tamaño: "",
          pantalla_resolucion: "",
          bateria: "",
          software_incluido: "",
          tipo_disco: "",
          capacidad_disco: "",
          memoria_ram: "",
          procesador: "",
          precio: "",
        },
      ],
    };
  },

  created () {
      axios.get(`https://computer-shop-mintic2022.herokuapp.com/producto/`)

        .then((products) => {
          this.producto = products.data;
          console.log(JSON.stringify(products));
        })
  },

  methods: {
    readingProducts() {
      axios
        .get(`https://computer-shop-mintic2022.herokuapp.com/producto/`)

        .then((products) => {
          this.producto = products.data;
          console.log(JSON.stringify(products));
        })
        .catch((error) => {
          console.log(error);
          alert("Error  al momento de leer los registros");
        });
    },

    loadProduct() {
      this.$router.push({ name: "rudProducto" });
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
.producto {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: bottom;
  justify-content: center;
  align-items: center;
}


</style>
