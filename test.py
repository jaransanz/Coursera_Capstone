def check_london_area(geopoint, geojson):
    with open(geojson) as f:
        js = json.load(f)
        point = Point(geopoint[1],geopoint[0])
        # check each polygon to see if it contains the point
        result=False
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                return True
                break
    return result    
for point in mesh_points:
    point_a = [point[0], point[1] + radius/110.574]
    point_b = [point[0] + math.sqrt(3)*radius/(2*111.32*math.cos(math.radians(boroughs_boundary_df['Latitude'].mean()))), point[1] + radius/(2*110.574)]
    point_c = [point[0] + math.sqrt(3)*radius/(2*111.32*math.cos(math.radians(boroughs_boundary_df['Latitude'].mean()))), point[1] - radius/(2*110.574)]
    point_d = [point[0], point[1] - radius/110.574]
    point_e = [point[0] - math.sqrt(3)*radius/(2*111.32*math.cos(math.radians(boroughs_boundary_df['Latitude'].mean()))), point[1] - radius/(2*110.574)]
    point_f = [point[0] - math.sqrt(3)*radius/(2*111.32*math.cos(math.radians(boroughs_boundary_df['Latitude'].mean()))), point[1] + radius/(2*110.574)]
    
    folium.CircleMarker(point_a, radius=2, color='blue', fill=True, fill_color='blue', fill_opacity=0.7, parse_html=False).add_to(map_london)
    folium.CircleMarker(point_b, radius=2, color='blue', fill=True, fill_color='blue', fill_opacity=0.7, parse_html=False).add_to(map_london)
    folium.CircleMarker(point_c, radius=2, color='blue', fill=True, fill_color='blue', fill_opacity=0.7, parse_html=False).add_to(map_london)
    folium.CircleMarker(point_d, radius=2, color='blue', fill=True, fill_color='blue', fill_opacity=0.7, parse_html=False).add_to(map_london)
    folium.CircleMarker(point_e, radius=2, color='blue', fill=True, fill_color='blue', fill_opacity=0.7, parse_html=False).add_to(map_london)
    folium.CircleMarker(point_f, radius=2, color='blue', fill=True, fill_color='blue', fill_opacity=0.7, parse_html=False).add_to(map_london)
