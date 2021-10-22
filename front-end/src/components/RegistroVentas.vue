<template>
    <div class="wrapper2">
        <h1 class="login text-center">Iniciar Sesión</h1>
        <form class="pt-3" v-on:submit.prevent="processLogInUser" >
            <div class="form-group">
                <div class="input-field"> 
                    <span class="fas fa-user p-2"></span> 
                    <input type="text" v-model="user.username" placeholder="Username" required>
                </div>
            </div>
            <div class="form-group">
                <div class="input-field"> 
                    <span class="fas fa-lock p-2"></span> 
                    <input type="password" v-model="user.password" placeholder="Password" required>
                </div>
            </div>
            <button type="submit" class="btn btn-block text-center">Iniciar sesión</button>
        </form>
</div>
</template>

<script>

export default {
    name: "RegistroVentas",
    data: function(){
        return {
            username: localStorage.getItem('username') || "none"
        }
    },
    methods: {
        processShopRegister: function(){
            axios.post(
                "https://computer-shop-mintic2022.herokuapp.com/registro_ventas", 
                this.registro_ventas,  
                {headers: {}}
                )
                .then((result) => {
                    let dataLogIn = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    
                    this.$emit('completedLogIn', dataLogIn)
                })
                .catch((error) => {
                    
                    if (error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                    
                });
        }
    }
}

</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Hind:wght@300&family=Montserrat&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Poppins&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');
    .body2{
        /*background: red;*/
        display: block;
        justify-content: center;
        align-items: center;
        /*max-width: 55.9%;*/
        /*width: 90%;
        margin: auto;*/
    }
    /* ###################################################### */
    /* ####################### Título ####################### */
    /* ###################################################### */
    .PTítulo{
        position: relative;
    }
    .PTítulo h1{
        width: 400px;
        padding: 3%;
        margin: auto;
    }
    /* ###################################################### */
    /* ###################### Entradas ###################### */
    /* ###################################################### */
    .container1{
    position: relative;
    background-color: #4169E1;
    width: 80%;
    margin: auto;
    padding: 3%;
}
.container2{
    width: 70%;
    padding: 0%;
    margin: auto;
}
.container2 div{
    display: inline-block;
}
.LI1{
    width: 800px;
    padding: 0%;
    margin: auto;
}
.LI2{
    width: 300px;
    padding: 0%;
    margin: auto;
}

.LI1 div, .LI2 div{
    display: inline-block;
}


.pointerText{
    position: relative;
    /*background-color: red;*/
    padding: 3%;
    width: 200px;
    height: 4%;
    margin: 3%;
}
.inputBox{
    position: relative;
    /*background-color: green;*/
    padding: 3%;
    width: 200px;
    height: 4%;
    max-width: 20%;
    margin: 3%;
    /*border: 3px solid rgba(0, 0, 0, 0.9);*/
}


    /* ###################################################### */
    /* ######################## tabla ####################### */
    /* ###################################################### */

    .Table{
        max-width: 55.9%;
        margin: auto;
    }

    /* ###################################################### */
    /* ####################### Botones ###################### */
    /* ###################################################### */

    .Buttons div{
        display: inline-block;
    }
    .Buttons{
        max-width: 55.9%;
        margin: auto;
    }
    .Buttons button{
        background-color: #ADFF2F;
        padding: 10px 20px;
        border: 3px solid rgba(0, 0, 0, 0.9);
        color: black;
        font-weight: bold; 
        font-size: 16px;
    }
</style>