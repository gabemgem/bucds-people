import { defineStore } from "pinia";
import { ref } from "vue";

export const usePeopleStore = defineStore('people', () => {
    const people = ref([
        {
            "Name": "Gabe McDonnell-Maayan",
            "Pronouns": "He/Him",
            "Email": "gmaayan@bu.edu",
            "Type": "phd",
            "Cohort": 2022,
            "Research Tags": ["css","abm","sdm","suicide"],
            "Research Overview": "Builds models of rural and youth suicide",
            "Affiliations": ["CDS", "BU", "CMAC"],
            "Relationships": [ { "name": "Wesley Wildman", "type": "advisor" }],
            "Other Tags": [ "Office 1327" ],
        },
        {
            "Name": "Wesley Wildman",
            "Email": "wwildman@bu.edu",
            "Type": "faculty",
            "Cohort": null,
            "Research Tags": ["css","abm","sdm","suicide"],
            "Research Overview": "Builds models of rural and youth suicide",
            "Affiliations": ["CDS", "BU", "CMAC"],
            "Relationships": [ { "name": "Gabe McDonnell-Maayan", "type": "advisor" }],
            "Other Tags": [ "Office 1327" ],
        },
    ])

    return { people }
})