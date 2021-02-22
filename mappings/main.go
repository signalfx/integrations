package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("expecting mapping rules json as argument")
		os.Exit(1)
	}

	filePath := os.Args[1]
	mappings, err := unmarshalMappingRules(filePath)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	table := makeTable(mappings)

	outputFilepath := "mappings.md"
	file, err := os.Create(outputFilepath)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()

	_, err = io.WriteString(file, table)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
