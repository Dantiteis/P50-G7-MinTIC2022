<template>
  <div class="producto_user">
    <div class="container_producto_user">
      <h2>Producto</h2>
      <form v-on:submit.prevent="AddingProducts">
        <div class="input-group mb-2 mr-sm-2">
          <div class="col">
            <input
              type="number"
              class="form-control"
              v-model="producto.id"
              placeholder="Id"
            />
            <input
              type="text"
              class="form-control"
              v-model="producto.tipo"
              placeholder="Tipo"
            />
            <input
              type="text"
              class="form-control"
              v-model="producto.salidas"
              placeholder="Salidas"
            />

            <input
              type="text"
              class="form-control"
              v-model="producto.pantalla_resolucion"
              placeholder="Resolucion de pantalla"
            />
            <input
              type="text"
              class="form-control"
              v-model="producto.software_incluido"
              placeholder="Software incluido"
            />
            <input
              type="text"
              class="form-control"
              v-model="producto.capacidad_disco"
              placeholder="Capacidad del disco (GB)"
            />
          </div>
          <div class="col">
            <input
              type="text"
              class="form-control"
              v-model="producto.modelo"
              placeholder="Modelo"
            />
            <input
              type="text"
              class="form-control"
              v-model="producto.entradas"
              placeholder="Entradas"
            />

            <input
              type="text"
              class="form-control"
              v-model="producto.pantalla_tamaño"
              placeholder="Tamaño pantalla"
            />

            <input
              type="text"
              class="form-control"
              v-model="producto.bateria"
              placeholder="Bateria"
            />

            <input
              type="text"
              class="form-control"
              v-model="producto.tipo_disco"
              placeholder="Tipo de disco (GB)"
            />

            <input
              type="text"
              class="form-control"
              v-model="producto.memoria_ram"
              placeholder="Memoria RAM (GB)"
            />
          </div>
        </div>

        <input
          type="text"
          class="form-control"
          v-model="producto.procesador"
          placeholder="Procesador"
        />
        <input
          type="number"
          class="form-control"
          v-model="producto.precio"
          placeholder="Precio en USD$"
        />
        <button
          class="btn-lg btn-block"
          v-on:click="AddingProducts"
          type="button"
        >
          Agregar producto
        </button>
        <button
          class="btn-lg btn-block"
          v-on:click="loadProducts"
          type="button"
        >
          Ver todos los productos
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "producto",

  data: function() {
    return {
      producto: {
        id: "",
        modelo: "",
        tipo: "",
        entradas: "",
        salidas: "",
        pantalla_tamaño: "",
        pantalla_resolucion: "",
        bateria: false,
        software_incluido: "",
        tipo_disco: "",
        capacidad_disco: "",
        memoria_ram: "",
        procesador: "",
        precio: "",
      },
    };
  },

  methods: {
    AddingProducts: function() {
      axios
        .post(
          `https://computer-shop-mintic2022.herokuapp.com/producto/`,
          this.producto,
          { headers: {} }
        )
        .then((result) => {
          let addProduct = {
            id: this.producto.id,
            modelo: this.producto.modelo,
            tipo: this.producto.tipo,
            entradas: this.producto.entradas,
            salidas: this.producto.salidas,
            pantalla_tamaño: this.producto.pantalla_tamaño,
            pantalla_resolucion: this.producto.pantalla_resolucion,
            bateria: this.producto.bateria,
            software_incluido: this.producto.software_incluido,
            tipo_disco: this.producto.tipo_disco,
            capacidad_disco: this.producto.capacidad_disco,
            memoria_ram: this.producto.memoria_ram,
            procesador: this.producto.procesador,
            precio: this.producto.precio,
          };
          this.$emit("addedProduct", addProduct);
          alert("El producto fue registrado de manera exitosa");

          console.log(result);
          this.clearForm();
        })
        .catch((error) => {
          console.log(error);
          alert("Error  al momento de registrar los datos del producto.");
        });
    },

    clearForm: function() {
      this.id = "";
      this.modelo = "";
      this.tipo = "";
      this.entradas = "";
      this.salidas = "";
      this.pantalla_tamaño = "";
      this.pantalla_resolucion = "";
      this.bateria = "";
      this.software_incluido = "";
      this.tipo_disco = "";
      this.capacidad_disco = "";
      this.memoria_ram = "";
      this.procesador = "";
      this.precio = "";
    },

    loadProducts: function() {
      this.$router.push({ name: "readProducts" });
    },
  },
};
</script>

<style>
.producto_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  margin-top: 70px !important;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container_producto_user {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 45%;
  height: 90%;

  display: flex;
  flex-direction: column;
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

.producto_user button {
  width: 100%;
  height: 45px;

  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.producto_user button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 2px solid #283747;
}
</style>
