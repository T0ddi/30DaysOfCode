// Print "Hello World" at the first line and a stringValue at the second line

package main
import "fmt"
import "bufio"
import "os"

func main() {
	
	inputReader := bufio.NewReader(os.Stdin)
    input, _ := inputReader.ReadString('\n')
	
	fmt.Println("Hello, World.")
	fmt.Println(input)

}