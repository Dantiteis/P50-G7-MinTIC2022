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
        <th scope="col">Modelo</th>
        <th scope="col">Tipo</th>
        <th scope="col">Entradas</th>
        <th scope="col">Salidas</th>
        <th scope="col">Tamaño pantalla</th>
        <th scope="col">Resolución pantalla</th>
        <th scope="col">Batería</th>
        <th scope="col">Software</th>
        <th scope="col">Tipo disco</th>
        <th scope="col">Capacidad del disco</th>
        <th scope="col">Memoria RAM</th>
        <th scope="col">Procesador</th>
        <th scope="col">Precio</th>
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
  </b-table>
  <div class="producto">
    <button
      class="btn btn-success btn-lg btn-block"
      v-on:click="readingProducts"
      type="button"
    >
      Mostrar productos
    </button>
    <button class="btn-lg btn-block" v-on:click="loadProduct" type="button">
      Detalle
    </button>
  </div>
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

.producto_user h2 {
  color: #283747;
}

.producto_user form {
  width: 90%;
}

.producto_user input {
  height: 25px;
  width: 100%;

  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;

  border: 1px solid #283747;
}

.producto button {
  width: 50%;
  height: 40px;

  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.producto button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 2px solid #283747;
}
</style>
