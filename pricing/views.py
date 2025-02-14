from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .pricing_engine import calculate_fare
from .models import RideRequest
from .serializers import RideRequestSerializer

from django.contrib.auth import get_user_model

# Fetch the user model
User = get_user_model()


class CalculateFareView(APIView):
    """
    API View to calculate ride fare dynamically based on distance, traffic, and demand.
    """

    # Allow public access (no authentication required)
    permission_classes = [AllowAny]

    def get(self, request):
        """
        Handles GET requests to calculate fare.
        
        Query Parameters:
            - distance (float): Distance of the ride in kilometers.
            - traffic_level (str): Traffic condition ('low', 'normal', 'high').
            - demand_level (str): Demand condition ('low', 'normal', 'peak').

        Returns:
            JSON response containing the fare breakdown or an error message.
        """
        try:
            # Retrieve query parameters with default values if missing
            distance = request.GET.get('distance')
            traffic_level = request.GET.get('traffic_level', 'normal')
            demand_level = request.GET.get('demand_level', 'normal')

            # Validate input: Ensure distance is provided and is a positive float
            if not distance:
                return Response({"error": "Distance parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                distance = float(distance)
                if distance <= 0:
                    return Response({"error": "Distance must be greater than zero."}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                return Response({"error": "Invalid distance value. Must be a number."}, status=status.HTTP_400_BAD_REQUEST)

            # Calculate fare using the pricing engine
            fare_data = calculate_fare(distance, traffic_level, demand_level)

            # Save ride request data to the database
            ride = RideRequest.objects.create(
                distance_km=distance,
                traffic_level=traffic_level,
                demand_level=demand_level,
                calculated_fare=fare_data["total_fare"]
            )

            return Response(fare_data, status=status.HTTP_200_OK) 

        except Exception as e:
            # Catch unexpected errors and return an appropriate error message
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
