<template>

        <div class="body2">
            <div class="PTítulo">
                <h1 class="Título">Registrar Ventas</h1>
            </div>
            <div class="Contenedor1">
                <div class="LI1">
                    <div class="Vendedos">
                        <div class="NV"><p>Nombre del Vendedor: </p></div>
                        <div class="INV"><input type="text"></div>
                    </div>
                    <div class="Cliente">
                        <div class="Fecha"><p>fecha: </p></div>
                        <div class="IFecha"><input type="date"></div>
                    </div>
                </div>
            </div>    
            <div class="Contenedor2">
                <div class="LI2">
                    <div class="NC"><p>Nombre del Cliente: </p></div>
                    <div class="INC"><input type="text"></div>
                </div>
            </div>
            <div class="Table">
                <table>
                    <div class="TableHead">
                        <tr>
                            <th>Código</th>
                            <th>Producto</th>
                            <th>Cantidad</th>
                        </tr>
                    </div>
                    <div class="Content">
                        <tr>
                            <td>1111111</td>
                            <td>Producto de prueba</td>
                            <td>70</td>
                        </tr>
                    </div>
                </table>
            </div>
            <div class="Buttons">
                <div class="B1">
                    <button id="Sell_Historic">Histórico de Ventas</button>
                </div>
                <div class="Register">
                    <button id="Registrar">Registrar</button>
                </div>
            </div>
        </div>

</template>

<script>

export default {
    name: "RegistroVentas",
    data: function(){
        return {
            username: localStorage.getItem('username') || "none"
        }
    }
}

</script>

<style>
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
    .Contenedor1, .Contenedor2{
        position: relative;
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


    .NV{
        position: relative;
        /*background-color: red;*/
        padding: 3%;
        width: 200px;
        height: 4%;
        margin: 3%;
    }
    .INV{
        position: relative;
        /*background-color: green;*/
        padding: 3%;
        width: 200px;
        height: 4%;
        max-width: 20%;
        margin: 3%;
        /*border: 3px solid rgba(0, 0, 0, 0.9);*/
    }
    .Fecha{
        position: relative;
        /*background-color: red;*/
        width: 100px;
        height: 4%;
        margin: 6%;
    }
    .IFecha{
        position: relative;
        /*background-color: green;*/
        padding: 3%;
        width: 50%;
        height: 4%;
        max-width: 20%;
        margin: 3%;
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