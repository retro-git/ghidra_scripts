#TODO Dump symbol of current function
#@author
#@category _NEW_
#@keybinding 
#@menupath Tools.Dump Symbol
#@toolbar 


f = getFunctionContaining(currentAddress)

if f != None:
	print(f.getSignature().getPrototypeString() + ";")
	print(f.getName() + " = 0x" + f.getEntryPoint().toString().split("::")[-1] + ";")

