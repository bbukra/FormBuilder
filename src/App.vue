<template>
  <div id="app">
  <router-link id="Home_Button" v-bind:to="'/'">Form Builder</router-link>
  <!-- the router outlet, where all matched components would ber viewed -->
  <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
}
</script>
<!-- styling for the component -->
<style>
html {
    background-color: #57c2da;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#Home_Button { 
    font-size: 2vw;
    color: #3182c8;
    background-color: #fff;
    font-family: HelveticaNeueW01-65Medi,HelveticaNeueW02-65Medi,HelveticaNeueW10-65Medi,Helvetica Neue,Arial,Helvetica,sans-serif;
    /* padding: .3em 1em; */
    border-radius: 0.6em;
    display: inline-block;
    line-height: 1.6;
    margin: 0 0 2px;
    position: absolute;
    top:0%;
    left:40%;
    width:20%;
    margin-bottom: 2px;
    cursor: pointer;
    text-align: center;
    -webkit-font-smoothing: antialiased;
    font-weight: 300;
}
#Home_Button:hover { 
    background-color: rgb(226, 226, 226);
}
</style>