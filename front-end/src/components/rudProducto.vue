<template>
  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
    rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
    crossorigin="anonymous"
  />
  <div class="producto_user">
    <div class="container_producto_user">
      <h2>Producto</h2>
      <form>
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
        <button class="btn-lg btn-block" v-on:click="getProduct" type="button">
          Ver producto
        </button>
        <button
          class="btn-lg btn-block"
          v-on:click="updateProduct"
          type="button"
        >
          Editar producto
        </button>
        <button
          class=" btn-lg btn-block "
          v-on:click="deleteProduct"
          type="button"
        >
          Eliminar
        </button>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "rudProducto",

  data: function() {
    return {
      producto: [
        {
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
      ],
    };
  },

  methods: {
    getProduct() {
      let productoId = this.producto.id;
      axios
        .get(
          `https://computer-shop-mintic2022.herokuapp.com/producto/${productoId}`
        )

        .then((product) => {
          this.producto = product.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Error  al momento de leer el registro");
        });
    },

    updateProduct() {
      let idProducto = this.producto.id;
      if (idProducto != null) {
      }
      axios
        .put(
          `https://computer-shop-mintic2022.herokuapp.com/producto/${idProducto}`,
          this.producto
        )
        .then((result) => {
          let editProduct = {
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
          this.$emit("editProduct", editProduct);
          console.log(result);
        })
        .catch((error) => {
          console.log(error);
          alert("No se puede actualizar el registro");
        });
    },

    deleteProduct() {
      let idProducto = this.producto.id;
      axios
        .delete(
          `https://computer-shop-mintic2022.herokuapp.com/producto/${idProducto}`,
          this.producto
        )
        .then((result) => {
          this.producto = result;
          console.log(result);
          alert("El registro fue eliminado de manera exitosa");
        })
        .catch((error) => {
          console.log(error.result);
          alert("El registro no pudo ser eliminado");
        });
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

  border-radius: 12px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.producto button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 2px solid #283747;
}
</style>
