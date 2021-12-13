# Capstone-project

 """House Price Prediction
    Note: Only for houses with Latitude Ranging from: 24.93 - 24.97 , Longitude: 121.47 - 121.54
    ---
    parameters:
        - name: House Age
          in: query
          type: number
          description: "0 - 43"
          required: true
        - name: Distance_to_the_nearest_MRT_station
          in: query
          type: number
          description: "24 - 4k"
          required: true
        - name: number_of_convenience_stores
          in: query
          type: number
          description: "0-10"
          required: true
        - name: Latitude
          in: query
          type: number
          description: "24.93-25"
          required: true
        - name: Longitude
          in: query
          type: number
          description: "121.47 - 121.57"
          required: true
    responses:
          200:
              description: The output values
    """
