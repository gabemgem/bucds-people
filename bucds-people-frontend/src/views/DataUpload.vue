<template>
  <v-card>
    <v-card-title>Bulk Data Upload</v-card-title>
    <v-card-subtitle><a href="UploadTemplate.csv" download>Download a template here</a></v-card-subtitle>
    <v-card-text style="max-width: 400px;">
      <v-file-input 
        clearable 
        label="Bulk Upload File"
        accept=".csv"
        v-model="file_upload"
      ></v-file-input>
    </v-card-text>
    <v-card-actions>
      <v-btn @click="uploadFile()" :disabled="!file_upload">Submit</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { watch } from 'vue';
import { ref } from 'vue';
import http from '@/plugins/axios';


const file_upload = ref(null)

watch(file_upload, async (new_file) => {
  console.log(new_file)
})

function uploadFile() {
  console.log(file_upload.value)
}
</script>
