import pkgutil 
import importlib 

package_name = "transformers"
package = importlib.import_module(package_name)
for importer, modname, ispkg in  pkgutil.iter_modules(package.__path__, package_name + '.'):
    print("Found submodule %s (is a package: %s)" % (modname, ispkg))