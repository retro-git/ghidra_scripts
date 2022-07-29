#@author retro
#@category _NEW_
#@keybinding 
#@menupath Tools.Dump All Symbols
#@toolbar 

symbols = []
prototypes = []

fm = currentProgram.getFunctionManager()
functions = filter(lambda f: f.getSignature().getPrototypeString().find("FUN_") == -1 and f.getSignature().getPrototypeString().find("undefined") == -1, fm.getFunctions(True))
for f in functions:
	symbols.append(f.getName() + " = 0x" + f.getEntryPoint().toString().split("::")[-1] + ";")
  	prototypes.append(f.getSignature().getPrototypeString() + ";")

f = open("symbols.txt", "w")
f.write("\n".join(symbols))
f.close()

f = open("prototypes.c", "w")
f.write("\n".join(prototypes))
f.close()
