import phonenumbers
from phonenumbers import geocoder, carrier

def get_location(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)

        # Get the region and location information
        region = geocoder.description_for_number(parsed_number, "en")
        location = carrier.name_for_number(parsed_number, "en")

        return f"Location: {location}, Region: {region}"

    except phonenumbers.NumberParseException as e:
        return f"Invalid phone number: {e}"

# Example usage:
phone_number = "+919876543210"  # Replace with the phone number you want to look up
result = get_location(phone_number)
print(result)
