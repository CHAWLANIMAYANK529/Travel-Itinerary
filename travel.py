from jaipur_data import jaipur_data
from udaipur_data import udaipur_data
from amritsar_data import amritsar_data
from jammu_kashmir_data import jammu_kashmir_data
from rishikesh_data import rishikesh_data

def get_destination_info(location):
    """
    Function to retrieve destination information from the imported data.
    """
    destinations_data = {
        "Jaipur": jaipur_data,
        "Udaipur": udaipur_data,
        "Amritsar": amritsar_data,
        "Jammu & Kashmir": jammu_kashmir_data,
        "Rishikesh": rishikesh_data,
    }
    
    return destinations_data.get(location, None)

def suggest_activities(location, interests):
    activities = []
    destination_data = get_destination_info(location)

    if destination_data:
        for attraction, details in destination_data["attractions"].items():
            for interest in details["Interests"]: 
                if interest in interests and attraction not in activities:
                    activities.append(attraction)
                    break
    return activities

def suggest_destinations(num_days, interests, traveler_type="average"):
    suggested_destinations = []

    print(f"DEBUG: Interests - {interests}")
    print(f"DEBUG: Number of days - {num_days}")

    if num_days <= 3:
        if "history" in interests:
            suggested_destinations.append("Jaipur")
        if "nature" in interests:
            suggested_destinations.append("Udaipur")
        if "religion" in interests:
            suggested_destinations.append("Amritsar")
        if "adventure" in interests or "relaxation" in interests:
            suggested_destinations.append("Rishikesh")  # Can be done in 2–3 days
        if "spirituality" in interests:
            suggested_destinations.append("Rishikesh")

    elif 4 <= num_days <= 5:
        if "history" in interests:
            suggested_destinations.extend(["Jaipur", "Udaipur"])
        if "culture" in interests:
            suggested_destinations.append("Amritsar")
        if "nature" in interests:
            suggested_destinations.extend(["Udaipur", "Rishikesh"])
        if "adventure" in interests:
            suggested_destinations.append("Rishikesh")
        if "relaxation" in interests:
            suggested_destinations.append("Rishikesh")
        if "religion" in interests or "spirituality" in interests:
            suggested_destinations.append("Rishikesh")
        if "wildlife" in interests or "mountains" in interests:
            suggested_destinations.append("Jammu & Kashmir")  # Just enough time

    elif num_days >= 6:
        if all(interest in interests for interest in ["history", "nature"]):
            suggested_destinations.extend(["Jaipur", "Udaipur", "Rishikesh"])
        if "history" in interests and "culture" in interests:
            suggested_destinations.extend(["Jaipur", "Amritsar", "Udaipur"])
        if "adventure" in interests and "nature" in interests:
            suggested_destinations.extend(["Rishikesh", "Jammu & Kashmir"])
        if "relaxation" in interests and "nature" in interests:
            suggested_destinations.extend(["Udaipur", "Rishikesh"])
        if "spirituality" in interests or "yoga" in interests:
            suggested_destinations.append("Rishikesh")
        if "wildlife" in interests or "mountains" in interests:
            suggested_destinations.append("Jammu & Kashmir")

    print(f"DEBUG: Suggested destinations - {suggested_destinations}")
    return list(set(suggested_destinations))


# Enhanced Example Interaction with Full Activity Details
print("Welcome to the India Itinerary Planner!")
num_days = int(input("How many days do you plan to travel? "))
interests_input = input("What are your interests (e.g., history, nature, adventure, food, relaxation, spirituality, yoga, photography, scenic views, wildlife, culture, mountains, religion, romance - separate by comma): ").lower().split(", ")
traveler_type_input = input("What is your preferred travel style? (budget/average/luxury): ").lower()

print(f"DEBUG: User interests: {interests_input}")
print(f"DEBUG: Traveler type: {traveler_type_input}")

suggested_locations = suggest_destinations(num_days, interests_input, traveler_type_input)

if suggested_locations:
    print(f"\nBased on your interests, duration, and travel style ({traveler_type_input}), you might consider visiting:")
    for location in suggested_locations:
        print(f"- {location}")

    for location in suggested_locations:
        print(f"\n--- Activities in {location} ---")
        suggested_activities_list = suggest_activities(location, interests_input)
        
        if suggested_activities_list:
            destination_info = get_destination_info(location)
            for activity in suggested_activities_list:
                attraction_details = destination_info["attractions"][activity]
                print(f"\nActivity: {activity}")
                print(f"Description: {attraction_details['Description']}")
                print(f"Location: {attraction_details['Location']}")
                print(f"Opening Hours: {attraction_details['Opening_Hours']}")

                # Safe handling of Entrance Fees
                fees = attraction_details.get("Entrance_Fees_INR", {})
                if isinstance(fees, dict):
                    indian_fee = fees.get("Indian", "N/A")
                    nri_fee = fees.get("NRI", "N/A")
                    print(f"Entrance Fees (INR): Indian: {indian_fee}, NRI: {nri_fee}")
                else:
                    print(f"Entrance Fees: {fees if isinstance(fees, str) else 'Free'}")

                print(f"Time Needed: {attraction_details['Time_Needed']}")
                print(f"Interests: {', '.join(attraction_details['Interests'])}")
        else:
            print("No specific activities found based on your interests in this location.")

        # Display additional info about the location
        destination_info = get_destination_info(location)
        if destination_info:
            print(f"\nBest time to visit {location}: {destination_info['best_time_to_visit']}")
            print(f"Available accommodation types in {location}: {destination_info['accommodation_types'].get(traveler_type_input, 'Varied')}")
            print(f"Transportation options in {location}: {', '.join(destination_info['transport_options'])}")
            print(f"Estimated daily budget for {location} ({traveler_type_input} travel): {destination_info.get('budget_info', {}).get(traveler_type_input, 'N/A')}")
else:
    print("Could not retrieve detailed information for this location.")
