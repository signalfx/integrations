package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
)

type remappingType string

const (
	addResultType remappingType = "ADD_RESULT"
	queryDimType  remappingType = "QUERY_DIM"
	simpleType    remappingType = "SIMPLE"
)

var validTypes = map[remappingType]bool{
	addResultType: true,
	queryDimType:  true,
	simpleType:    true,
}

type mappings struct {
	Remappings      map[string]remapping `json:"remappings"`
	SimpleRenames   map[string]string    `json:"simpleRenames"`
	PropertyRenames map[string]string    `json:"propertyRenames"`
}

type remapping struct {
	Type           remappingType     `json:"type",required`
	MetricName     string            `json:"metric"`
	DimensionName  string            `json:"dimName"`
	DimensionValue string            `json:"dimValue"`
	Remappings     []remappingsInner `json:"remappings"`
}

type remappingsInner struct {
	MetricName     string `json:"metric"`
	DimensionValue string `json:"dim"`
}

func unmarshalMappingRules(filePath string) (*mappings, error) {
	jsonFile, err := ioutil.ReadFile(filePath)
	if err != nil {
		return nil, fmt.Errorf("failed to read file: %v", err)
	}

	var mappings mappings
	err = json.Unmarshal(jsonFile, &mappings)
	if err != nil {
		return nil, fmt.Errorf("failed to unmarshal to struct: %v", err)
	}
	return &mappings, nil
}
