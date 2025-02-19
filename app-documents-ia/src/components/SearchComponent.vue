<template>
  <v-container>
    <v-row >
      <v-col cols="12" class="mx-auto text-center">
        <v-card :loading = loadingResult :text=textOutputOpenai></v-card>
      </v-col>
    </v-row>
  </v-container>
  
   <v-row align="center" justify="center">
    <v-col cols="8">
      <v-text-field label="Search" v-model="textInputOpenai"></v-text-field>
    </v-col>
    <v-col cols="3">
      <v-btn color="primary" @click="obterDados()">Search</v-btn>
    </v-col>
  </v-row>
</template>
<script>
import axios from "axios";
export default {
  name: "SearchComponent",
  props: {
    nomeDaTabela: String ?? "",
  },
  data() {
    return {
      
      textInputOpenai: '',
      textOutputOpenai: '',
      loadingResult:Boolean = false,
    };
  },
  mounted() {
    
  },
  methods: {
        
        async obterDados() {
      const endpoint = `http://localhost:8000/test-openai`;
      
      this.loadingResult=true
      try {
        const response = await axios.post(endpoint, {
          text: this.textInputOpenai
        });
        
        this.textOutputOpenai=response.data
        

      } catch (error) {
        console.error(error);
      }
    },
    },
};
</script>