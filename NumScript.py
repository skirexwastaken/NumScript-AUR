from source.builder import NumScriptVirtualMachine

def main():
    engine = NumScriptVirtualMachine()
    try:
        engine.cli()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
