from flask import Flask, render_template
import folium
import overpy
import json
app = Flask(__name__)

@app.route('/')
def display_map():
    user_lat = 40.7128
    user_lon = -74.0060

    api = overpy.Overpass()

    bounding_box = (
        user_lat - 0.1, user_lon - 0.1,
        user_lat + 0.1, user_lon + 0.1
    )

    query = (
        f"node['amenity'='doctors']['healthcare:speciality'='dermatology']"
        f"({bounding_box[0]}, {bounding_box[1]}, {bounding_box[2]}, {bounding_box[3]});"
        f"out;"
    )

    result = api.query(query)

    nearest_doctors = []
    for node in result.nodes:
        lat = float(node.lat)
        lon = float(node.lon)
        name = node.tags.get("name", "Doctor Name Unknown")  # Get the doctor's name, or use a default if not available
        address = node.tags.get("addr:street", "Address Unknown")  # Get the address, or use a default if not available
        phone = node.tags.get("contact:phone", "Phone Unknown")  # Get the phone number, or use a default if not available
        name = name.replace("'", " ")
        address = address.replace("'", " ")
        phone = phone.replace("'", " ")
        doctor_info = {
            "lat": lat,
            "lon": lon,
            "name": name,
            "address": address,
            "phone": phone
        }

        nearest_doctors.append(doctor_info)

    m = folium.Map(location=[user_lat, user_lon], zoom_start=14)

    for doctor in nearest_doctors:
        popup_content = f"<b>Name:</b> {doctor['name']}<br><b>Address:</b> {doctor['address']}<br><b>Phone:</b> {doctor['phone']}"
        folium.Marker([doctor['lat'], doctor['lon']], popup=popup_content).add_to(m)
    nearest_doctors_json = json.dumps(nearest_doctors, ensure_ascii=False)

    m = folium.Map(location=[user_lat, user_lon], zoom_start=14)

    return render_template('map.html', nearest_doctors_json=nearest_doctors_json, map=m._repr_html_())

if __name__ == '__main__':
    app.run(debug=True)
