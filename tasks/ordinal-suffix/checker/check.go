package main
import ("flag"; "fmt"; "os"; "os/exec"; "path/filepath"; "runtime")
func main() {
    source := flag.String("solution", "", "candidate ordinal.go"); flag.Parse()
    if *source == "" { panic("--solution required") }
    _, own, _, _ := runtime.Caller(0)
    root, err := os.MkdirTemp("", "ordinal-check-"); if err != nil { panic(err) }; defer os.RemoveAll(root)
    for name, src := range map[string]string{"ordinal.go":*source,"ordinal_test.go":filepath.Join(filepath.Dir(own),"fixtures","ordinal_test.go")} {
        data, err := os.ReadFile(src); if err != nil { panic(err) }
        if err=os.WriteFile(filepath.Join(root,name),data,0600); err != nil { panic(err) }
    }
    if err=os.WriteFile(filepath.Join(root,"go.mod"),[]byte("module ordinal\n\ngo 1.23\n"),0600); err != nil { panic(err) }
    cmd:=exec.Command("go","test","-count=1","-timeout=10s","-v",".");cmd.Dir=root;cmd.Stdout=os.Stdout;cmd.Stderr=os.Stderr
    if err=cmd.Run();err!=nil { panic(err) }
    fmt.Println("PASS ordinal-suffix: trusted compiled cases and repeat probes")
}
