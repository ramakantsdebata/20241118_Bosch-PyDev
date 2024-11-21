def div(num, den):
    print("Entering div...")
    # raise StopIteration("StopIteration raised")
    if num > 50:
        raise ValueError("Numerator should never be more than '50'")
    
    try:
        res = num/den
        print("Caluclation done...")
    except Exception:
        print("Release connections")
        raise   # Raise the exception again
    print("Exiting div...")
    return res


def Main():
    a = 26
    b = 0

    res:float = None
    try:
        print("Starting div...")
        res = div(a, b)
        print("Finshed div...")
        # file = open("Test.txt", "w")
        # File operations
        
    except (ZeroDivisionError, ValueError) as ex:
        # print(f"EXCEPTION --> {repr(ex)}")
        print(f"EXCEPTION --> {ex!r}")
    # except ValueError as ex:
    #     print(f"EXCEPTION --> {ex!r}")
    except Exception as ex:
        print(f"EXCEPTION --> Other than ZDE/VE [{ex!r}]")
    else:
        print("All statements in try executed properly")
    finally:
        # Resources should be released here
        # file.close()
        pass

    print(res)
    print("All done")

Main()
