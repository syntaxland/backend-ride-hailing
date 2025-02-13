def calculate_fare(distance_km, traffic_level, demand_level):
    """
    Calculates the total fare for a ride based on distance, traffic level, and demand level.
    
    Parameters:
        distance_km (float): The distance of the ride in kilometers.
        traffic_level (str): The level of traffic congestion ('low', 'normal', 'high').
        demand_level (str): The level of demand ('low', 'normal', 'peak').
    
    Returns:
        dict: A dictionary containing the breakdown of the fare.
    """

    # Base fare (minimum fare charged for any ride)
    base_fare = 2.5

    # Cost per kilometer of travel
    per_km_rate = 1.0

    # Multiplier factors based on traffic conditions
    traffic_multipliers = {'low': 1.0, 'normal': 1.2, 'high': 1.5}

    # Multiplier factors based on demand (e.g., surge pricing)
    demand_multipliers = {'low': 1.0, 'normal': 1.0, 'peak': 1.8}

    # Calculate distance-based fare
    distance_fare = distance_km * per_km_rate

    # Retrieve multipliers, defaulting to 1.0 if invalid input is given
    traffic_multiplier = traffic_multipliers.get(traffic_level, 1.0)
    demand_multiplier = demand_multipliers.get(demand_level, 1.0)

    # Compute total fare, applying both traffic and demand multipliers
    total_fare = (base_fare + distance_fare) * traffic_multiplier * demand_multiplier

    # Return fare details rounded to 2 decimal places
    return {
        "base_fare": base_fare,
        "distance_fare": distance_fare,
        "traffic_multiplier": traffic_multiplier,
        "demand_multiplier": demand_multiplier,
        "total_fare": round(total_fare, 2)  # Ensure two decimal places for consistency
    }
