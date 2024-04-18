<template>
    <v-card class="person-card" variant="elevated">
        <v-card-title>{{ fullName }}</v-card-title>
        <v-card-subtitle>{{ props.person.Email }}</v-card-subtitle>

        <v-card-text>
        <v-container class="person-properties">
        <v-card class="ma-1" variant="outlined">
            <v-card-title>{{ `Position: ${props.person.Type.toUpperCase()}` }}</v-card-title>
        </v-card>

        <v-card v-if="hasProp('Cohort')" class="ma-1" variant="outlined">
            <v-card-title>{{ `Cohort: ${props.person.Cohort}` }}</v-card-title>
        </v-card>
        </v-container>
        </v-card-text>

        <v-card-actions>
            <v-btn :icon="expand ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="expand=!expand"></v-btn>
        </v-card-actions>

        <v-expand-transition>
            <div v-show="expand">
                <v-card-text>
                    <v-card v-if="hasProp('Research Tags')" class="ma-1" variant="outlined">
                        <v-card-text style="padding: 4px;">
                            {{ `Research Tags: ${props.person['Research Tags'].join(', ')}` }}
                        </v-card-text>
                    </v-card>
                    <v-card v-if="hasProp('Research Overview')" class="ma-1" variant="outlined">
                        <v-card-text style="padding: 4px;">
                            {{ `Research Overview: ${props.person['Research Overview']}` }}</v-card-text>
                    </v-card>
                    <v-card v-if="hasProp('Affifiliations')" class="ma-1" variant="outlined">
                        <v-card-text style="padding: 4px;">
                            {{ `Org Affiliations: ${props.person.Affiliations.join(', ')}` }}
                        </v-card-text>
                    </v-card>
                    <v-card v-if="hasProp('Relationships')" class="ma-1" variant="outlined">
                        <v-card-text style="padding: 4px;">
                            {{ `Relationships: ${relationships_string}` }}
                        </v-card-text>
                    </v-card>
                    <v-card v-if="hasProp('Other Tags')" class="ma-1" variant="outlined">
                        <v-card-text style="padding: 4px;">
                            {{ `Tags: ${props.person['Other Tags'].join(', ')}` }}
                        </v-card-text>
                    </v-card>

                </v-card-text>


            </div>
        </v-expand-transition>
    </v-card>
</template>

<script setup>
import { computed } from 'vue';
import { defineProps, ref } from 'vue';

const props = defineProps(['person']);
const expand = ref(false);

function hasProp(prop) {
    return props.person && props.person[prop] && props.person[prop] !== ''
}

const relationships_string = computed(() => {
    if(!hasProp('Relationships')) {
        return ''
    }
    return props.person.Relationships.map(r => `${r.name}: ${r.type}`).join(', ')
})

const fullName = computed(() => {
    if(!props.person) {
        return ''
    }
    if(props.person?.Pronouns && props.person.Pronouns !== '') {
        return `${props.person.Name} (${props.person.Pronouns})`
    }
    return props.person.Name
})

</script>

<style>
.person-card {
    max-width: 300px;
}

.person-properties {
  display: flex;
  flex-wrap: wrap;
}
</style>