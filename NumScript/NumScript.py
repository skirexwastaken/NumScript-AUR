# --- NumScript ---

# --- Importing NumScript Virtual Machine from source ---
from NumScript.source.builder import NumScriptVirtualMachine

def main():
    # --- Launching the NumScript shell ---                
    engine = NumScriptVirtualMachine()
    
    # --- Removing KeyboardInterrupt error message ---
    try:
        engine.cli()
    
    except KeyboardInterrupt:
        pass
main()
