<template>
<div class="wrapper3 container">
  <table   class="table text-center table-bordered caption-top table-hover">
    <caption><h1>Lista de Comentarios</h1></caption>
    <thead class="thead-inverse">
      <tr>
        <th>ID</th>
        <th scope="col">idCliente</th>
        <th scope="col">Comentario</th>
        
      </tr>
    </thead>
    <tbody>
      <tr v-for="(comentario, index) in Comentarios" :key="index">
        <th scope="row">{{comentario.id}}</th>
        <td>{{ comentario.idCliente }}</td>
        <td>{{ comentario.comentario }}</td>
        
      </tr>
    </tbody>
  </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "readComentarios",

  data: function() {
    return {
      Comentarios: [],
    }
  },

  created () {
      axios.get(`https://computer-shop-mintic2022.herokuapp.com/comentarios/`)
      .then((coments) => {
          this.Comentarios = coments.data;
      })
  },

  methods: {

    readingComents() {
      axios
        .get(`https://computer-shop-mintic2022.herokuapp.com/comentarios/`)

        .then((coments) => {
          this.Comentarios = coments.data;
          console.log(JSON.stringify(coments));
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

.Comentarios {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: bottom;
  justify-content: center;
  align-items: center;
}

.Comentarios h2 {
  color: #283747;
}

.Comentarios form {
  width: 90%;
}

.Comentarios input {
  height: 25px;
  width: 100%;

  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;

  border: 1px solid #283747;
}

.Comentarios button {
  width: 50%;
  height: 40px;

  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.Comentarios button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 2px solid #283747;
}
</style>

