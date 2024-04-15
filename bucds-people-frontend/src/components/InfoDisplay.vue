<script>
export default {
  props: ['selectedNode', 'fullData'],
  data() {
    return {
      tab: 'node',
    }
  }
}
</script>

<template>
  <v-card>
    <div class="d-flex flex-row">
      <v-tabs v-model="tab" direction="vertical" color="primary">
        <v-tab value="node"> Node</v-tab>
        <v-tab value="filter">Filter</v-tab>
      </v-tabs>
      <v-window v-model="tab">
        <v-window-item value="filter">
          <v-card flat>
            <v-card-title>
              {{ fullData?.title || 'General Information' }}
            </v-card-title>
            <v-card-text>
              {{
                fullData?.text || 'No general information has been added for this family tree.'
              }}
            </v-card-text>
          </v-card>
        </v-window-item>
        <v-window-item value="node">
          <v-card flat>
            <v-card-title>
              {{ selectedNode?.Name || 'Selected Node Info' }}
            </v-card-title>
            <v-card-text>
              <div v-if="!selectedNode">
                No node is selected.
              </div>
              <div v-if="selectedNode">
                <v-table>
                  <tbody>
                    <tr 
                      v-for="item in selectedNode.props"
                      :key="item[0]"
                    >
                      <td>{{ item[0] }}</td>
                      <td>{{ item[1] }}</td>
                    </tr>
                  </tbody>
                </v-table>
              </div>
            </v-card-text>
          </v-card>
        </v-window-item>
      </v-window>
    </div>
  </v-card>
</template>
