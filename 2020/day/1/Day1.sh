#!/bin/bash
# Part 1
for a in $(cat input.txt); do
    for b in $(cat input.txt); do
        if [[ $((a+b)) == 2020 ]]; then
            echo $a, $b, $((a+b)), $((a * b))
            break 2
        fi
    done
done

# Part 2 
for a in $(cat input.txt); do
    for b in $(cat input.txt); do
        if [[ $((a+b)) -gt 2020 ]]; then
            continue
        fi
        for c in $(cat input.txt); do
            if [[ $((a+b+c)) == 2020 ]]; then
                echo $a, $b, $c, $((a+b+c)), $((a*b*c))
                break 3
            fi
        done
    done
done
