import pandas as pd

rows = [
    ("Baxter State Park","Outdoors","Millinocket","Maine's largest protected wilderness area and home to Mount Katahdin; register at the Baxter State Park Headquarters in Millinocket before heading in.","$ (park fee)","Year-round","https://maps.app.goo.gl/qub5i8epmaFG3YFE7",45.6567589,-68.6868523),
    ("Mount Katahdin","Outdoors","Millinocket","The highest peak in Maine and the northern terminus of the Appalachian Trail; a bucket-list summit accessible via Roaring Brook Campground. Plan far in advance — only ~60 daily permits.","$ (park fee)","Summer-Fall","https://maps.app.goo.gl/fVZgXY86UVdG15sC7",45.9044004,-68.9215652),
    ("Roaring Brook Campground","Outdoors","Millinocket","The trailhead campground for the best Katahdin summit routes, including the Cathedral Trail and the iconic Knife's Edge traverse.","$ (camping)","Summer-Fall","https://maps.app.goo.gl/dvnF744RgD94wxcz5",45.9193874,-68.8566853),
    ("Penobscot Whitewater Rafting","Outdoors","Millinocket","Well-reviewed guided whitewater rafting on the Penobscot River's eastern branch; lunch on the riverbank included.","$$ (tour)","Summer","https://maps.app.goo.gl/9nNLAnTuCuLqtKGSA",45.7295844,-68.8373508),
    ("Millinocket","Culture","Millinocket","The last town before Baxter State Park — 3 hours from Portland on I-95 — with outfitters, registered Maine guides, and a growing trail-town food and lodging scene.","Free","Year-round","https://maps.app.goo.gl/AC7A9W4vwhx7D1e56",45.6573651,-68.7091503),
    ("Gather Inn","Culture","Millinocket","A charming, beautifully restored B&B on Millinocket's main street; excellent breakfast and hosts who know the park well.","$$","Year-round","https://maps.app.goo.gl/s22chPqn6pyrvo159",45.6577622,-68.710532),
    ("New England Outdoor Center","Culture","Millinocket","Full-service outdoor resort with cabins, rafting, kayaking, and the Knife Edge Brewing Company restaurant; stunning views of Katahdin.","$$","Year-round","https://maps.app.goo.gl/8tZLhRDHRoNy6GZUA",45.7258365,-68.8187034),
]

df = pd.DataFrame(rows, columns=["name","category","town","description","price","season","maps_url","lat","lng"])
df.insert(0, "id", range(1, len(df)+1))
df.insert(2, "region", "Katahdin & Penobscot Headwaters")

df.to_excel("maine_locations_katahdin.xlsx", index=False, sheet_name="Locations")
print(f"Wrote {len(df)} rows")
