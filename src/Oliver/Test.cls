Class Oliver.Test
{

ClassMethod Dict() As %Status
{
	Set mycar = ##class(%SYS.Python).Builtins().dict()
	do mycar.setdefault("make", "Toyota")
	Do mycar.setdefault("model", "RAV4")
	do mycar.setdefault("color", "blue")
	zwrite mycar
	/*
mycar=2@%SYS.Python  ; {'make': 'Toyota', 'model': 'RAV4', 'color': 'blue'}  ; <OREF>
 
USER>write mycar."__getitem__"("color")
blue
	*/
	Quit $$$OK
}

ClassMethod RPA() As %Status
{
	Set py = ##class(%SYS.Python).Import("webdriver")
	Do py.test()
	Quit $$$OK
}

}
