Class Oliver.Test
{

ClassMethod RPA() As %Status
{
	Set py = ##class(%SYS.Python).Import("webdriver")
	Do py.test()
	Quit $$$OK
}

}
