<template>
  <v-container>
    <v-row>
      <v-col id="graphcol" :cols="(collapseSidebar) ? 11 : 8">
        <div id="graph"></div>
      </v-col>
      <v-col v-if="collapseSidebar" cols="1">
        <v-btn variant="outlined" block @click="collapseSidebar=false">Expand</v-btn>
      </v-col>
      <v-col v-if="!collapseSidebar" cols="4">
        <v-btn variant="outlined" block @click="collapseSidebar=true">Collapse</v-btn>
        <InfoDisplay 
          :fullData="data" 
          :selectedNode="selectedNode" 
          ></InfoDisplay>
          <v-card flat>
            <v-btn @click="showNewPersonForm=true">Calculate Relationships</v-btn>
          </v-card>
      </v-col>
    </v-row>
  </v-container>
  <v-overlay 
    v-model="showNewPersonForm"
    class="align-center justify-center"
  >
    <v-card style="border: 15px solid white;" class="overlay-form"> 
      <v-card-title>New Person Form</v-card-title>
      <v-card-actions>
        <v-btn
          variant="text"
          @click="closeAndClearNewPersonForm()"
        >
          Close
        </v-btn>
        <v-btn
          variant="text"
          @click="$refs.newPersonForm.submitData(); closeAndClearNewPersonForm();"
        >
          Submit
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-overlay>
</template>

<script setup>
import { usePeopleStore } from '@/stores/people'
import { ref, onMounted } from 'vue'
import ForceGraph from 'force-graph';
import InfoDisplay from '@/components/InfoDisplay.vue'

const store = usePeopleStore()
const data = ref([])
const graph = ref(null)
const collapseSidebar = ref(true)
const showNewPersonForm = ref(false)
const nodeSize = ref(2);
const selectedNode = ref(null);


function getGraphData(initialData) {
    const nodes = initialData.map((person) => {
        return {
            Name: person.Name,
            props: Object.entries(person),
        }
    });

    const links = [];

    for (const person of initialData) {
        person.Relationships.forEach(relationship => {
            links.push({ source: person.Name, target: relationship.name, type: relationship.type });
        });
    }

    return { nodes, links };
}

function getInitials(name) {
    return name.split(/\s+/).map(word => word[0]).join('');
}

function setupGraph() {
    const graphElement = document.getElementById('graph');

    graph.value = ForceGraph()(graphElement)
        .nodeId('Name')
        .nodeCanvasObject(nodeCanvasObjectFn)
        .nodeCanvasObjectMode(() => 'after')
        .nodeVal(nodeSize.value)
        .nodeLabel('Name')
        .linkLabel(linkLabelFn)
        .linkDirectionalArrowLength(linkDirectionalArrowLengthFn)
        .linkDirectionalArrowRelPos(0.9)
        .onNodeClick(onNodeClickFn)
        .graphData(data.value);

}

function onNodeClickFn(node) {
    if (node.Name === selectedNode.value?.Name) {
    selectedNode.value = null
    console.log('clear selected node')
    } else {
    selectedNode.value = node
    console.log('new selected node')
    }
    graph.value.d3ReheatSimulation();
}
    
function nodeCanvasObjectFn(node, ctx, globalScale) {
    const label = getInitials(node.Name);
    const fontSize = 14 / globalScale
    ctx.font = `${fontSize}px Sans-Serif`

    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    ctx.fillStyle = 'black'
    ctx.fillText(label, node.x, node.y)

    if (node.Name === selectedNode.value?.Name) {
    ctx.strokeStyle = 'yellow'
    ctx.lineWidth = 2
    ctx.beginPath()
    ctx.arc(node.x, node.y, nodeSize.value * graph.value.nodeRelSize(), 0, Math.PI * 2)
    ctx.stroke()
    }
}

function linkLabelFn(link) {
    return `${getInitials(link.source.Name)}-${getInitials(link.target.Name)}: ${link.type}`
}

function linkDirectionalArrowLengthFn(link) {
    // only parent links should be directional
    return link.type === 'parent' ? 5 : 0
}

onMounted(() => {
    data.value = getGraphData(store.people);
    console.log(data.value);
    setupGraph();
})

</script>
