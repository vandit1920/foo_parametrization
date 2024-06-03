from foo_parameterization.foo_parameterization import FooParameterization # type: ignore
#main function
def main():
    try:
        radius = float(input("Enter the radius of the sphere: "))
        foo = FooParameterization(radius)
        volume = foo.calculate_volume()
        print(f'Volume of the sphere with radius {radius} is {volume}')
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
