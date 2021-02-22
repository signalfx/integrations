package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestUnmarshalMappingRules(t *testing.T) {
	mappings, err := unmarshalMappingRules("./testdata/mappings.json")
	require.NoError(t, err)
	require.NotNil(t, mappings)

	require.Equal(t, 3, len(mappings.Remappings))
	require.Equal(t, remapping{
		Type:          "ADD_RESULT",
		DimensionName: "direction",
		Remappings: []remappingsInner{
			{
				MetricName:     "pod_network_receive_errors_total",
				DimensionValue: "receive",
			},
			{
				MetricName:     "pod_network_transmit_errors_total",
				DimensionValue: "transmit",
			},
		},
	}, mappings.Remappings["k8s.pod.network.errors"])
	require.Equal(t, remapping{
		Type:       "SIMPLE",
		MetricName: "kubernetes.replication_controller.available",
	}, mappings.Remappings["k8s.replication_controller.available"])
	require.Equal(t, remapping{
		Type:           "QUERY_DIM",
		MetricName:     "k8s.pod.network.errors",
		DimensionName:  "direction",
		DimensionValue: "transmit",
	}, mappings.Remappings["pod_network_transmit_errors_total"])

	require.Equal(t, 1, len(mappings.SimpleRenames))
	require.Equal(t, map[string]string{
		"k8s.container.name": "container_spec_name",
	}, mappings.SimpleRenames)
}

func TestUnmarshalMappingRulesErrors(t *testing.T) {
	mappings, err := unmarshalMappingRules("")
	require.EqualError(t, err, "failed to read file: open : no such file or directory")
	require.Nil(t, mappings)

	mappings, err = unmarshalMappingRules("./testdata/invalid_mappings.json")
	require.Error(t, err)
	require.Nil(t, mappings)
}
