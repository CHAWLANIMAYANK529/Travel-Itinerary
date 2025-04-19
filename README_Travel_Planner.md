
# India Travel Itinerary Planner

## Overview

**India Travel Itinerary Planner** is a Python-based console application that provides travel destination suggestions and activity recommendations based on a user's interests, travel duration, and travel style (budget/average/luxury). The application integrates detailed data from five popular destinations across India: Jaipur, Udaipur, Amritsar, Jammu & Kashmir, and Rishikesh.

---

## Features

- 🏞️ Suggests destinations across India based on number of days and interests.
- 🏛️ Recommends top attractions, including historical landmarks, spiritual sites, and natural wonders.
- 🗓️ Provides best times to visit, estimated budget, and accommodation suggestions.
- 🥘 Lists vegetarian food recommendations for each city.
- 🚗 Suggests transportation options based on location.

---

## Destinations Covered

- Jaipur 🕌
- Udaipur 🏞️
- Amritsar 🙏
- Rishikesh 🧘‍♂️
- Jammu & Kashmir 🏔️

---

## Project Structure

```
travel_itinerary_planner/
│
├── travel.py                        # Main application logic
├── jaipur_data.py                   # Attractions and info for Jaipur
├── udaipur_data.py                  # Attractions and info for Udaipur
├── amritsar_data.py                 # Attractions and info for Amritsar
├── rishikesh_data.py                # Attractions and info for Rishikesh
├── jammu_kashmir_data.py           # Attractions and info for Jammu & Kashmir
├── README.md                        # Project documentation
```

---

## How It Works

1. User inputs:
   - Number of travel days
   - Personal interests (e.g., history, nature, food)
   - Travel style (budget, average, luxury)

2. System suggests matching cities.

3. For each city:
   - Top attractions based on interests
   - Attraction details: location, opening hours, entry fees, interests
   - Best time to visit
   - Vegetarian food and stay recommendations
   - Budget estimates and transport options

---

## Running the Program

1. Ensure all `.py` data files are in the same directory.

2. Run the application:
```bash
python travel.py
```

3. Follow the prompts to receive personalized travel recommendations.

---

## Example

```plaintext
How many days do you plan to travel? 5
What are your interests? history, culture, photography
What is your preferred travel style? average
```

---

## Requirements

- Python 3.x
- No additional libraries required

---

## Future Enhancements

- 🌍 Add more destinations
- 📱 GUI or mobile interface
- 💬 Multilingual support
- ✈️ Integration with booking services (transport, hotels)
- 📊 Advanced interest profiling using machine learning

---

## Authors

- Project Developer: [Your Name]
- Data Curator: [Your Name]

---

## License

This project is open-source and available under the MIT License.

