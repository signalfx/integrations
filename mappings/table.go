package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

const (
	addResultTypeTemplate         = "`${sourceMetric}` (metric) with dimension name `${sourceDimensionName}` equal to `${sourceDimensionValue}`"
	simpleTypeTemplate            = "`${sourceMetric}` (metric)"
	legacyMetricTemplate          = "`${legacyMetric}` (metric)"
	otelDimensionRenameTemplate   = "`${otelDimension}` (dimension)"
	legacyDimensionRenameTemplate = "`${legacyDimension}` (dimension)"
	otelPropertyRenameTemplate    = "`${otelProperty}` (property)"
	legacyPropertyRenameTemplate  = "`${legacyProperty}` (property)"
)

var (
	longestOTelRow   int
	longestLegacyRow int
)

func updateLongest(r row) {
	if len(r.otelColumn) > longestOTelRow {
		longestOTelRow = len(r.otelColumn)
	}
	if len(r.legacyColumn) > longestLegacyRow {
		longestLegacyRow = len(r.legacyColumn)
	}
}

type row struct {
	otelColumn   string
	legacyColumn string
}

func makeTable(m *mappings) string {
	var rows []row
	remappings := parseRemappings(m.Remappings)
	simpleRenames := parseSimpleRenames(m.SimpleRenames)
	propertyRenames := parsePropertyRenames(m.PropertyRenames)
	rows = append(rows, []row{
		{
			otelColumn:   "**OpenTelemetry Semantics**",
			legacyColumn: "**Legacy Semantics**",
		},
		{
			otelColumn:   dashes(longestOTelRow),
			legacyColumn: dashes(longestLegacyRow),
		},
	}...)
	rows = append(rows, remappings...)
	rows = append(rows, simpleRenames...)
	rows = append(rows, propertyRenames...)
	sort.Slice(rows[:], func(i, j int) bool {
		return rows[i].legacyColumn < rows[j].legacyColumn
	})
	return generateTable(rows)
}

func generateTable(rows []row) string {
	var finalTable string
	for i, m := range rows {
		if i == 1 {
			finalTable += fmt.Sprintf("|%s|%s|\n", m.legacyColumn, m.otelColumn)
			continue
		}
		finalRow := fmt.Sprintf(
			"| %s%s | %s%s |\n",
			m.legacyColumn,
			spaces(longestLegacyRow-len(m.legacyColumn)),
			m.otelColumn,
			spaces(longestOTelRow-len(m.otelColumn)),
		)
		finalTable += finalRow
	}

	return finalTable
}

func spaces(n int) string {
	var s string
	for i := 0; i < n; i++ {
		s += " "
	}
	return s
}

func dashes(n int) string {
	var s string
	for i := 0; i < n+2; i++ {
		s += "-"
	}
	return s
}

type metricTemplateHelper struct {
	sourceMetric         string
	sourceDimension      string
	sourceDimensionValue string
	targetMetric         string
	dimensionRenames     map[string]string
}

func (t *metricTemplateHelper) getTemplate(template string) string {
	return os.Expand(template, t.fill)
}

func (t *metricTemplateHelper) getDimensionRenames() string {
	withDims := " and with the following dimensions renamed: "
	for k, v := range t.dimensionRenames {
		withDims += fmt.Sprintf("`%v` to `%v`, ", k, v)
	}
	return withDims[:len(withDims)-2]
}

func (t *metricTemplateHelper) fill(s string) string {
	switch s {
	case "sourceMetric":
		return t.sourceMetric
	case "sourceDimensionName":
		return t.sourceDimension
	case "sourceDimensionValue":
		return t.sourceDimensionValue
	case "legacyMetric":
		return t.targetMetric
	}
	return ""
}

func skipMetricMapping(sourceMetric string) bool {
	if strings.HasPrefix(sourceMetric, "k8s.") ||
		strings.HasPrefix(sourceMetric, "container.") ||
		strings.HasPrefix(sourceMetric, "system.") {
		return false
	}
	return true
}

func parseRemappings(metricMappings map[string]remapping) []row {
	table := make([]row, 0, len(metricMappings))
	for sourceMetric, m := range metricMappings {
		if skipMetricMapping(sourceMetric) {
			continue
		}
		switch m.Type {
		case addResultType:
			for i := range m.Remappings {
				th := metricTemplateHelper{
					sourceMetric:         sourceMetric,
					sourceDimension:      m.DimensionName,
					sourceDimensionValue: m.Remappings[i].DimensionValue,
					targetMetric:         m.Remappings[i].MetricName,
					dimensionRenames:     m.SimpleRenames,
				}
				currentRow := row{}
				currentRow.otelColumn = th.getTemplate(addResultTypeTemplate)
				if th.dimensionRenames != nil {
					currentRow.otelColumn += th.getDimensionRenames()
				}
				currentRow.legacyColumn = th.getTemplate(legacyMetricTemplate)
				table = append(table, currentRow)
				updateLongest(currentRow)
			}
		case simpleType:
			th := metricTemplateHelper{
				sourceMetric:     sourceMetric,
				sourceDimension:  m.DimensionName,
				targetMetric:     m.MetricName,
				dimensionRenames: m.SimpleRenames,
			}
			currentRow := row{}
			currentRow.otelColumn = th.getTemplate(simpleTypeTemplate)
			currentRow.legacyColumn = th.getTemplate(legacyMetricTemplate)
			if th.dimensionRenames != nil {
				currentRow.otelColumn += th.getDimensionRenames()
			}
			table = append(table, currentRow)
			updateLongest(currentRow)
		case queryDimType:
			// currently only used to reverse map.
		}
	}
	return table
}

type dimensionTemplateHelper struct {
	sourceDimension string
	targetDimension string
}

func (t *dimensionTemplateHelper) getTemplate(template string) string {
	return os.Expand(template, t.fill)
}

func (t *dimensionTemplateHelper) fill(s string) string {
	switch s {
	case "otelDimension":
		return t.sourceDimension
	case "legacyDimension":
		return t.targetDimension
	case "otelProperty":
		return t.sourceDimension
	case "legacyProperty":
		return t.targetDimension
	}
	return ""
}

func skipSimpleRenaming(sourceDimension string) bool {
	if strings.HasPrefix(sourceDimension, "k8s.") ||
		strings.HasPrefix(sourceDimension, "container.") ||
		strings.HasPrefix(sourceDimension, "host.") {
		return false
	}
	return true
}

func parseSimpleRenames(simpleRenames map[string]string) []row {
	table := make([]row, 0, len(simpleRenames))
	for otelName, legacyName := range simpleRenames {
		if skipSimpleRenaming(otelName) {
			continue
		}
		th := dimensionTemplateHelper{
			sourceDimension: otelName,
			targetDimension: legacyName,
		}
		currentRow := row{
			otelColumn:   th.getTemplate(otelDimensionRenameTemplate),
			legacyColumn: th.getTemplate(legacyDimensionRenameTemplate),
		}
		table = append(table, currentRow)
		updateLongest(currentRow)
	}
	return table
}

func parsePropertyRenames(propertyRenames map[string]string) []row {
	table := make([]row, 0, len(propertyRenames))
	for otelName, legacyName := range propertyRenames {
		if skipSimpleRenaming(otelName) {
			continue
		}
		th := dimensionTemplateHelper{
			sourceDimension: otelName,
			targetDimension: legacyName,
		}
		currentRow := row{
			otelColumn:   th.getTemplate(otelPropertyRenameTemplate),
			legacyColumn: th.getTemplate(legacyPropertyRenameTemplate),
		}
		table = append(table, currentRow)
		updateLongest(currentRow)
	}
	return table

}
