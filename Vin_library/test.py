from vininfo import Vin

def get_vin_info(vin):
    """Function to get information from the VIN number using vininfo"""
    try:
        vehicle = Vin(vin)
        return vehicle.make, vehicle.model, vehicle.year, vehicle.engine
    except Exception as e:
        print(f"Error with VIN '{vin}': {e}")
        return None, None, None, None

def main():
    # Prompt the user to enter a VIN number
    vin_number = input("Enter the VIN number: ").strip()

    # print(f"vin info: {Vin(vin_number)}")

    # Get the information from the VIN
    make, model, year, engine = get_vin_info(vin_number)

    # Display the results
    if make and model and year and engine:
        print(f"Car Make: {make}")
        print(f"Car Model: {model}")
        print(f"Car Year: {year}")
        print(f"Car Engine: {engine}")
    else:
        print("Failed to retrieve information. Please check the VIN number.")

if __name__ == "__main__":
    main()
