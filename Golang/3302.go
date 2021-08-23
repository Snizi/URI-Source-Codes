package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

func main() {
    var s []int

    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    input, _ := strconv.Atoi(scanner.Text())

    for i := 0; i < input; i++ {
        scanner.Scan()
        answers, _ := strconv.Atoi(scanner.Text())
        s = append(s, answers)
    }

    for i := 0; i < len(s); i++ {
        fmt.Printf("resposta %d: %d\n", i+1, s[i])
    }

}

