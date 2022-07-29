#Dump symbol of current function
#@author retro
#@category _NEW_
#@keybinding 
#@menupath
#@toolbar 


f = getFunctionContaining(currentAddress)

if f != None:
	print(f.getSignature().getPrototypeString() + ";")
	print(f.getName() + " = 0x" + f.getEntryPoint().toString().split("::")[-1] + ";")

