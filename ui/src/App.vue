<script setup>
import Cbutton from './components/cbutton.vue';
import {ref} from 'vue'
import Title from "./components/title.vue"
import searchBar from './components/searchBar.vue';
import SearchBar from './components/searchBar.vue';

</script>

<template>
  <div>
   <Title>

   </Title>
   <SearchBar>

   </SearchBar>
   <div>
    <br>

   </div>
    <Cbutton @click="">
      Submit
    </Cbutton>
  </div>
</template>

<style>
#app {
  background-image: linear-gradient(beige,rgb(203, 160, 156),rgb(246, 214, 234));
  
}
</style>


