import pandas as pd

rows = [
# Outdoors
("Popham Beach State Park","Outdoors","Phippsburg","Wide, dynamic beach with tidal pools and a sandbar walk to Fox Island at low tide; pair with a stroll through historic Bath afterward.","$","Year-round","https://maps.app.goo.gl/sKGgujWZeJGm8zDZ8",43.7362436,-69.797943),
("Reid State Park","Outdoors","Georgetown","Two beaches and a 3-mile loop trail, with a warm shallow pond that's great for kids.","$","Summer","https://maps.app.goo.gl/iuAFSAc6mXDpB8oZ9",43.7751155,-69.7327073),
("Bonyun Preserve","Outdoors","Westport Island","A quiet, lesser-visited loop trail just off the beaten path.","Free","Year-round","https://maps.app.goo.gl/S7bzZ7kHcrwHM3UX7",43.8769741,-69.7188058),
("Camden Hills State Park","Outdoors","Camden","Family-friendly hiking and trail running with sweeping views of Penobscot Bay from Mount Battie.","$","Year-round","https://maps.app.goo.gl/fTGMvZhfwEhfeZFWA",44.2310537,-69.0482997),
("Monhegan Island","Outdoors","Monhegan","17 miles of hiking trails on a dramatic, artist-favorite island; reachable by ferry from Boothbay Harbor via Balmy Day Cruises, Hardy Boat Cruises, or Mohegan Boat Line, with options for a day trip or overnight stay.","$$ (ferry)","Summer-Fall","https://www.google.com/maps/place/Monhegan+Island",43.7651835,-69.3194104),
("North Haven (Turner Farm)","Outdoors","North Haven","Idyllic island community; Turner Farm hosts rave-reviewed family-style dinners in their barn, with farmhouse lodging on-site.","$$$","Summer","https://maps.app.goo.gl/YvLiLodyoRFCBuFUA",44.1473499,-68.8514458),
("Lawson's Quarry","Outdoors","Vinalhaven","A clean, deep granite quarry with carved steps into the water; reach it via water taxi from North Haven.","Free","Summer","https://maps.app.goo.gl/VMhTrpnTyAKxvaPw6",44.057195,-68.8364586),
("Sand Beach (Deer Isle)","Outdoors","Deer Isle","A small, sandy cove on Maine's rocky coast, reached by a short forested walk.","Free","Summer","https://maps.app.goo.gl/ZRzuoXijRFFcELEn6",44.154697,-68.6900993),
("Barred Island Preserve","Outdoors","Deer Isle","A 2.5-mile woodland walk out to a sandbar that's only crossable a few hours around low tide.","Free","Year-round","https://maps.app.goo.gl/nhYSJ1EpgBJKFfww5",44.180517,-68.7120252),
("Acadia National Park","Outdoors","Mount Desert Island","Cadillac Mountain, Jordan Pond, and Little Long Pond connect via hiking trails; best visited September and October when crowds thin out. The Carriage Roads are great for gravel biking or cross-country skiing.","$ (park pass)","Fall","https://maps.app.goo.gl/wWbixstY8ASGHSft7",44.3525816,-68.2251036),
("Mount Desert Campground","Outdoors","Mount Desert","Tent platforms with sunset views over Somes Harbor, near Acadia.","$$","Summer","https://maps.app.goo.gl/K2YAkewvJ7576cYs8",44.3665487,-68.3178199),
("Acadia Outdoor Center","Outdoors","Seal Harbor","Rents bikes for exploring Acadia's Carriage Roads.","$$ (rental)","Summer-Fall","https://maps.app.goo.gl/MonKKuymKwx5iSgF8",44.2982708,-68.2404317),
("Schoodic Peninsula","Outdoors","Winter Harbor","Same dramatic scenery as Mount Desert Island but far less crowded; the National Park Service runs Schoodic Woods Campground here.","Free","Summer","https://maps.app.goo.gl/FoJvqYgWgcESWhZJ6",44.3813546,-68.0643703),
# Food & Dining
("Solo Pane","Food & Dining","Bath","Italian pastry shop and cafe in the historic shipbuilding town of Bath.","$$","Year-round","https://maps.app.goo.gl/ghSPxTtR7nxdEVCV8",43.9127725,-69.8149601),
("Five Islands Lobster Co","Food & Dining","Georgetown","Window-service lobster shack on the water, BYOB, with a general store next door for beer.","$$","Summer","https://maps.app.goo.gl/xZeYqk7aPBrREAJu7",43.8238374,-69.7094639),
("Sasanoa Brewing","Food & Dining","Westport Island","Farm-set brewery with Maine-herb-infused saisons; open weekends May through November, often with food trucks and live music.","$$","Spring-Fall","https://maps.app.goo.gl/58tn6aWQ2RaZebdN7",43.8821819,-69.7264834),
("The Place Bakery","Food & Dining","Camden","Tiny specialty bakery; order ahead online, since they sell out fast.","$","Year-round","https://maps.app.goo.gl/HoPAwn5gwLA8NxNG7",44.2020963,-69.0758862),
("Alna Store","Food & Dining","Alna","Farm-to-table fusion restaurant 7 miles north of Wiscasset; reservations recommended.","$$$","Year-round","https://maps.app.goo.gl/pTxCJeGPf92G2rVD7",44.0999704,-69.6145339),
("In a Silent Way","Food & Dining","Wiscasset","Wine bar with natural wines, fresh oysters, and small plates in a peaceful, low-key setting.","$$$","Year-round","https://maps.app.goo.gl/TyjZdXRXfzWuKXTe9",44.0028001,-69.6641403),
("TREATS","Food & Dining","Wiscasset","Bakery and cafe with a wide selection of baked goods, plus a small wine shop.","$","Year-round","https://maps.app.goo.gl/UvLoHBC9KfnHsgyv5",44.0024453,-69.6650828),
("Odd Alewives","Food & Dining","Waldoboro","Wood-fired pizza, beer, and oysters; visit Sunday afternoons for open jam sessions with local musicians.","$$","Year-round","https://maps.app.goo.gl/fjY9QWstpaLVSdWWA",44.0991626,-69.3661015),
("Cafe Grazie","Food & Dining","Rockland","Excellent Italian breakfast and lunch spot with a bright, friendly space.","$$","Year-round","https://maps.app.goo.gl/QQuVvjkhYAWJMPtq5",44.0979162,-69.1109823),
("Sammy's Deluxe","Food & Dining","Rockland","Farm-to-table dinner spot with a quirky, homey vibe and a simple, memorable menu.","$$$","Year-round","https://maps.app.goo.gl/9pH8nyEmnziYQEJ6A",44.10602,-69.109575),
("McLoon's Lobster Shack","Food & Dining","South Thomaston","Lobster rolls on the harbor, about 20 minutes from Rockland; worth the drive in summer.","$$","Summer","https://maps.app.goo.gl/1qfhUw7evD9WxwLR6",43.9953505,-69.117899),
("Blanchard's Creamery","Food & Dining","Boothbay Harbor","Homemade ice cream near the Botanical Gardens, with a sample-first policy to help you choose.","$","Summer","https://blanchardscreamery.com/",43.9606501,-69.6300241),
("Tinder Hearth","Food & Dining","Brooksville","Farm-to-table bakery and pizza night on the Blue Hill peninsula; expect long bakery lines and call ahead for a pizza table.","$$","Year-round","https://maps.app.goo.gl/kdRgA2UN4BMQwoM98",44.3859097,-68.7532018),
("Humblebee Cafe","Food & Dining","Blue Hill","Family favorite for burritos and agua frescas on the Blue Hill peninsula.","$$","Year-round","https://maps.app.goo.gl/99wGybvWaZfJ32kh8",44.4259872,-68.5785903),
("Nebo Lodge","Food & Dining","North Haven","One of the few restaurants on North Haven, with rooms upstairs if you want to stay over.","$$$","Year-round","https://www.google.com/maps/place/Nebo+Lodge",44.128425,-68.8734055),
("Aragosta","Food & Dining","Deer Isle","Destination sunset dinner at Goose Cove on Deer Isle; reservations recommended.","$$$","Year-round","https://maps.app.goo.gl/itCxPTf2yaPTwJeFA",44.1717732,-68.7137888),
# Culture
("Wiscasset","Culture","Wiscasset","Once a sleepy stop on Route 1, now in the middle of a culinary renaissance, with a walkable village center.","Free","Year-round","https://maps.app.goo.gl/Bdj86MV3rzViX5ze9",44.0028921,-69.665583),
("Damariscotta","Culture","Damariscotta","Charming Route 1 town, fun to stop and walk around.","Free","Year-round","https://maps.app.goo.gl/KRbU77boi8ZSivdo8",44.0318909,-69.5295474),
("Waldoboro","Culture","Waldoboro","Gaining a reputation for a thriving small-town arts scene, with theater, galleries, and an inn at its center.","Free","Year-round","https://maps.app.goo.gl/RKiJT3e83y1igzQz5",44.0952725,-69.3756017),
("Rockland","Culture","Rockland","Midcoast hub with art museums, restaurants, and a walkable downtown; worth staying the night.","Free","Year-round","https://maps.app.goo.gl/U9fvBDdKQp1izFoy9",44.1036914,-69.1089293),
("Camden","Culture","Camden","Postcard harbor town along Route 1, with a small waterfront park and views over the bay.","Free","Year-round","https://maps.app.goo.gl/VqhuwERRN2ENvRUx9",44.2109695,-69.064174),
("Belfast","Culture","Belfast","Another fun Route 1 coastal town to stop and explore on foot.","Free","Year-round","https://maps.app.goo.gl/9vx7FfdmzNZk1i4A7",44.4259092,-69.0064234),
("Waldo Theatre","Culture","Waldoboro","Small-town theater hosting live music, indie film screenings, and community theater.","$$ (tickets)","Year-round","https://maps.app.goo.gl/VNdLHn4tUy6nx9YFA",44.0959449,-69.3751293),
("Gravedigger's Daughter","Culture","Waldoboro","Local art gallery and studio, open to the public on weekends.","Free","Year-round","https://maps.app.goo.gl/bjDFdEC8mdFmeG1W7",44.0953295,-69.3761108),
("Waldoboro Inn","Culture","Waldoboro","Newly restored inn in the village center, with a wine bar inside that's a fun place to meet locals.","$$$","Year-round","https://maps.app.goo.gl/B6Ld6u2d1Yu9GAqM6",44.0961522,-69.3749459),
("Farnsworth Art Museum","Culture","Rockland","Impressive 20th-century Maine art and sculpture collection.","$$","Year-round","https://maps.app.goo.gl/tJDgYwqDb6o6iJFt7",44.1035668,-69.109783),
("Center for Maine Contemporary Art","Culture","Rockland","Exciting rotating exhibits of modern art from Maine and beyond.","$$","Year-round","https://maps.app.goo.gl/eJR4f8j9B8Vyc1G37",44.1031641,-69.1082452),
("250 Main Hotel","Culture","Rockland","Light-filled, lofty rooms overlooking Rockland's town and harbor; a nice base for a Midcoast stay.","$$$","Year-round","https://maps.app.goo.gl/i3RKcP7L89gWqZtm7",44.10102,-69.1093749),
("Strand Theatre","Culture","Rockland","Catch a show or film in this restored historic theater.","$$ (tickets)","Year-round","https://www.google.com/maps/place/Strand+Theatre/@44.1031393,-69.1140693,16z",44.1030556,-69.1088888),
("Coastal Maine Botanical Gardens","Culture","Boothbay","Extensive trail network with giant wooden troll sculptures, making for a fun family scavenger hunt.","$$","Year-round","https://maps.app.goo.gl/mJyErAixPj76VYU38",43.8721277,-69.6589985),
("Boothbay Harbor","Culture","Boothbay Harbor","Charming harbor town with a footbridge over the water and a picturesque marina; good for lunch and a stroll.","Free","Year-round","https://maps.app.goo.gl/xc4Q89zKFSpG1utD9",43.851273,-69.6257123),
("Blue Hill","Culture","Blue Hill","Quiet peninsula village with a mostly-private coastline and a few destination restaurants; once home to E.B. White.","Free","Year-round","https://maps.app.goo.gl/ASCb2VBgWGtPaJhE7",44.4130216,-68.5883185),
("Blue Hill Fairgrounds","Culture","Blue Hill","Hosts the beloved Blue Hill Fair around Labor Day, said to have inspired the animal characters in Charlotte's Web.","$ (admission)","Fall","https://maps.app.goo.gl/rSHaaggU52JnMY7p8",44.430015,-68.5752775),
("Deer Isle","Culture","Deer Isle","Artist-favorite island connected to the mainland by causeway, with a growing culinary scene and pebble beaches.","Free","Year-round","https://maps.app.goo.gl/E2Sg6a7rR18in2EcA",44.2662477,-68.6727634),
("Haystack Mountain School of Crafts","Culture","Deer Isle","Renowned crafts school that draws artist residencies from around the country.","Free (to visit)","Year-round","https://maps.app.goo.gl/vnLMiJ5AFW3MC5ob8",44.1888824,-68.5844926),
("Stonington","Culture","Stonington","Working harbor village with local tour operators offering boat charters around the islands.","Free","Year-round","https://maps.app.goo.gl/k8enp3ty5ARbaQEj7",44.155676,-68.6659983),
("Good Tide Tours","Culture","Stonington","Harbor cruise around the Stonington archipelago with a knowledgeable local captain.","$$ (tour)","Summer","https://maps.app.goo.gl/PCnEMg1BCUi3sAfq7",44.1551466,-68.6630793),
]

df = pd.DataFrame(rows, columns=["name","category","town","description","price","season","maps_url","lat","lng"])
df.insert(0, "id", range(1, len(df)+1))
df.insert(2, "region", "Midcoast")

df.to_excel("/mnt/user-data/outputs/maine_locations_midcoast.xlsx", index=False, sheet_name="Locations")
print(f"Wrote {len(df)} rows")
print(df['category'].value_counts())
