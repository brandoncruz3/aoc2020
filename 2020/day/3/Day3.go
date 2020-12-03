package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
)

func ReadLines(filename string) ([][]byte, error) {
	rawInput, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	rawInput = bytes.TrimRight(rawInput, "\n")
	return bytes.Split(rawInput, []byte("\n")), nil
}

type Row struct {
	data []byte
}

func (r *Row) isTree(idx int) bool {
	return r.data[idx%len(r.data)] == '#'
}

func CountTrees(rows []Row, xSlope, ySlope int) int {
	totalTrees := 0
	x := xSlope
	for y := ySlope; y < len(rows); y += ySlope {
		if rows[y].isTree(x) {
			totalTrees++
		}
		x += xSlope
	}

	return totalTrees
}

func main() {
	lines, err := ReadLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	rows := make([]Row, len(lines))
	for i, line := range lines {
		rows[i] = Row{data: line}
	}

	slopes := [][]int{
		[]int{1, 1},
		[]int{3, 1},
		[]int{5, 1},
		[]int{7, 1},
		[]int{1, 2},
	}

	totals := 0
	for _, slope := range slopes {
		t := CountTrees(rows, slope[0], slope[1])
		fmt.Printf("X: %d, Y: %d, Trees: %d\n", slope[0], slope[1], t)
		if totals == 0 {
			totals = t
		} else {
			totals *= t
		}
	}

	fmt.Println("Total Trees: ", totals)
}
