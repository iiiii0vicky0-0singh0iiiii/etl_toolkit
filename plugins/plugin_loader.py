import importlib

def apply_plugins(df, plugins):
    for plugin in plugins:
        try:
            module = importlib.import_module(f"plugins.{plugin}")

            if hasattr(module, "transform"):
                df = module.transform(df)
            else:
                print(f"Plugin {plugin} has no 'transform' function")

        except Exception as e:
            print(f"Error loading plugin {plugin}: {e}")

    return df