import pandas as pd

rows = [
# OUTDOORS (24)
("Thompson Lake Marina","Outdoors","Casco","Rents pontoon boats, kayaks, and tubes for a full day on one of Maine's most pristine lakes.","$$","Summer","https://www.google.com/maps/place/Thompson+Lake+Marina",44.0202949,-70.4736028),
("Diana's Baths","Outdoors","Bartlett, NH","Easy half-mile walk to a cascading series of rocky waterfall pools perfect for wading; $5 parking fee.","$","Summer","https://maps.app.goo.gl/TMaco28VAPDhg24p8",44.0747132,-71.1637945),
("Small Falls","Outdoors","Madrid","Accessible roadside swimming hole with a short walk to waterfalls and cliff jumping; free parking with bathrooms.","Free","Summer","https://maps.app.goo.gl/WdsBrwm9AP1WoCAq7",44.8589461,-70.516734),
("Tobey Falls","Outdoors","Willimantic","Short, easy hike to a beautiful waterfall with a calm swimming hole at its base.","Free","Summer","https://maps.app.goo.gl/KpCLCxgeyzvutHwX6",45.312551,-69.4162523),
("Screw Auger Falls","Outdoors","Newry","Water-sculpted gorge in Grafton Notch with pools you can wade into right from the roadside; picnic tables nearby.","Free","Summer","https://maps.app.goo.gl/8VKVNJXPyk7LcG1dA",44.5720034,-70.910074),
("Step Falls Preserve","Outdoors","Newry","Short family-friendly hike up a long cascade of natural water slides and swimming pools set in granite.","Free","Summer","https://maps.app.goo.gl/Y8tR65bwQVWbDbPNA",44.5726073,-70.8680992),
("Frenchman's Hole","Outdoors","Newry","Roadside swimming hole with a waterfall and cold, deep pool right off Sunday River Road.","Free","Summer","https://maps.app.goo.gl/7SrGsuStAA2Rs8Mz8",44.510095,-70.9185135),
("Emerald Pool","Outdoors","Chatham, NH","Emerald-green mountain pool off the Baldface Circle Trail in Evans Notch; 20-minute hike in.","Free","Summer","https://maps.app.goo.gl/JhENXxEZcKzr9eJr6",44.2377689,-71.0292057),
("Poplar Stream Falls","Outdoors","Carrabassett Valley","One-mile hike to a beautiful multi-tiered waterfall near Sugarloaf; bring bug spray in summer.","Free","Summer","https://maps.app.goo.gl/hovkVnCZYg1mwqsc8",45.101166,-70.193955),
("Big Falls","Outdoors","North Oxford","A quiet, little-known swimming hole and waterfall on the Cupsuptic River, accessible by car with walk-in camping nearby.","Free","Summer","https://maps.app.goo.gl/nZFk6YRbhfy7otXt9",45.081996,-70.892570),
("The Cataracts","Outdoors","Andover","About a 20-minute hike to a series of waterfalls with swimming pools along a wooded ravine.","Free","Summer","https://maps.app.goo.gl/WVkmhy8fYtNP6AoVA",44.6386696,-70.8603504),
("Slugundy Falls","Outdoors","Northeast Piscataquis","A remote, hike-in waterfall in the 100 Mile Wilderness — worth it on a clear summer day.","Free","Summer","https://maps.app.goo.gl/VraK9JfwUyP2unCP6",45.4139364,-69.4203286),
("Gauntlet Falls","Outdoors","Northeast Piscataquis","A hidden wilderness waterfall requiring a 1-2 mile hike through deep Maine woods.","Free","Summer","https://maps.app.goo.gl/3RBzgKsLuZJkhQ6j7",45.5386592,-69.0353219),
("Carrabassett Valley","Outdoors","Carrabassett Valley","Pristine valley with miles of hiking, mountain biking, and cross-country ski trails near Sugarloaf; the AMC maintains the Bigelow Preserve ridgeline trails here.","Free","Year-round","https://maps.app.goo.gl/8UV5qLBgYjseejhW6",45.073601,-70.261687),
("Sugarloaf","Outdoors","Carrabassett Valley","Maine's favorite ski resort among locals, with terrain for all levels; summer and fall bring great hiking and mountain biking.","$$$","Year-round","https://maps.app.goo.gl/cCSDsKF9M6JcCzg6A",45.054105,-70.308528),
("Bigelow Preserve","Outdoors","Stratton","The Appalachian Trail crosses this stunning ridge with 360-degree views; excellent backcountry camping.","Free","Year-round","https://maps.app.goo.gl/bigelowpreserve",45.1546312,-70.2869197),
("Mount Chocorua","Outdoors","Conway, NH","A classic White Mountains summit with panoramic 360° views; a favorite for hiking and trail running near the Maine border.","Free","Summer-Fall","https://maps.app.goo.gl/jo8NfUFvdTTe1wLi8",43.9540,-71.2740),
("Rangeley Lakes Trail Center","Outdoors","Rangeley","Extensive trail network for cross-country skiing, skijoring, snowshoeing, and summer hiking near Saddleback.","$","Year-round","https://maps.app.goo.gl/6rmG1bNcvpZJRLUt8",44.9564326,-70.5658954),
("Saddleback","Outdoors","Rangeley","Beloved, low-key ski mountain with exceptional terrain; a locals' favorite, quieter than Sugarloaf or Sunday River.","$$$","Year-round","https://maps.app.goo.gl/xpoEuGTJYEQshSVf6",44.9462173,-70.5270815),
("Moosehead Lake","Outdoors","Greenville","Maine's largest lake, surrounded by wilderness; a 4-hour drive from Portland best paired with an overnight at the AMC Gorman Chairback cabins.","Free","Year-round","https://maps.app.goo.gl/X3dvWVaSqcBfKnaf6",45.655049,-69.6506172),
("AMC Gorman Chairback Lodge","Outdoors","Greenville","Backcountry AMC lodge on Long Pond, accessible by ski or foot in winter; a gateway to Gulf Hagas, The Hermitage, and 100 Mile Wilderness peaks.","$$$","Year-round","https://www.outdoors.org/destinations/maine/gorman-chairback/",45.461695,-69.316778),
("The Hermitage","Outdoors","Brownville","A small preserve protecting a stand of old-growth white pine trees, some of the largest in Maine.","Free","Year-round","https://maps.app.goo.gl/YKpLo9LoSnvpeYqw5",45.479758,-69.287451),
("Gulf Hagas","Outdoors","Monson","Maine's 'Little Grand Canyon' — a dramatic 5-mile gorge hike past seven waterfalls; one of the state's most spectacular trails.","$ (access fee)","Summer-Fall","https://maps.app.goo.gl/H9NnhoNAWqYR55zQ6",45.496280,-69.357731),
("White Cap Mountain","Outdoors","Northeast Piscataquis","A remote Appalachian Trail peak in the 100 Mile Wilderness with summit views across hundreds of miles of unbroken forest.","Free","Summer-Fall","https://maps.app.goo.gl/dr9ZLJns7hd7ZLEt7",45.554769,-69.246160),
# FOOD & DINING (9)
("Gemini Cafe & Bakery","Food & Dining","Bethel","Top-tier coffee and fresh-made bagels inside a beautiful old bank building; one of the best bakeries in western Maine.","$","Year-round","https://maps.app.goo.gl/fZ3aLQCsBFM1J3KZ8",44.4075668,-70.7893125),
("Le Mu Eats","Food & Dining","Bethel","Creative Asian-fusion rice bowls, sandwiches, and cocktails — a surprisingly excellent find in a small mountain town.","$$","Year-round","https://maps.app.goo.gl/VfrVzqBQ5FEJCj6e7",44.4083345,-70.7882789),
("Steam Mill Brewing","Food & Dining","Bethel","Family-friendly brewpub near Sunday River with hearty food, good beer, and frequent live music.","$$","Year-round","https://maps.app.goo.gl/RnDCCMdPkWkXRtAN6",44.4533562,-70.8133355),
("Rolling Fatties","Food & Dining","Kingfield","Whimsical, garden-fresh burrito and bowl restaurant with locally sourced ingredients and a cult following.","$","Year-round","https://maps.app.goo.gl/mxaEEq1H6u6VC1vd9",44.9589855,-70.1567899),
("Orchard Girls Cidery","Food & Dining","Kingfield","Small-batch cider tasting room with locally made fruit ciders in a cozy, communal setting.","$","Year-round","https://maps.app.goo.gl/Q9AKzDyLctya5McY6",44.9625,-70.1603082),
("Loon Lodge Inn","Food & Dining","Rangeley","The best dinner in Rangeley — a classic log lodge on the lake serving refined, locally-sourced fare.","$$$","Year-round","https://maps.app.goo.gl/698U7Qvom5TsDf728",44.9462738,-70.6384124),
("Furbish Brew House","Food & Dining","Rangeley","Wood-fired pizza and house beers on the Rangeley Lake waterfront; great outdoor patio for a post-ski beer.","$$","Year-round","https://maps.app.goo.gl/5L2cWcwLD7oZWWrV6",44.9664016,-70.6439788),
("The Shed","Food & Dining","Rangeley","Low-key BBQ and bar with regular live music; a beloved local hangout in the heart of Rangeley.","$$","Year-round","https://maps.app.goo.gl/AWAS1NUYnsBmoAWo6",44.9669292,-70.6492822),
("The Quarry","Food & Dining","Monson","James Beard-recognized destination restaurant serving an exceptional multi-course dinner in a tiny wilderness town — worth the drive.","$$$","Year-round","https://maps.app.goo.gl/UrJFp4wQbCVzLA9C6",45.2854068,-69.4994256),
# CULTURE (7)
("Bethel","Culture","Bethel","Artsy mountain hamlet near Sunday River with a walkable Main Street; a great base for exploring the White Mountains foothills.","Free","Year-round","https://maps.app.goo.gl/jYYnA4LoJzes47cT6",44.4044586,-70.7898806),
("Sunday River","Culture","Newry","Major ski resort with varied terrain for all levels; beautiful in fall for foliage, and growing as a summer mountain biking destination.","$$$","Year-round","https://maps.app.goo.gl/wUricRqUJisjVvPcA",44.4684091,-70.8774107),
("Kingfield","Culture","Kingfield","Quaint foothills village at the gateway to the Carrabassett Valley and Sugarloaf, with a few good restaurants and a sauna retreat.","Free","Year-round","https://maps.app.goo.gl/hUghtoQV3NjuUqJ2A",44.9592231,-70.1539542),
("Maine Huts & Trails","Culture","Carrabassett Valley","Backcountry lodge network for hut-to-hut hiking, skiing, and snowshoeing through the western Maine wilderness.","$$$","Year-round","https://maps.app.goo.gl/LKuHxwzjXhtk6Y7SA",45.100938,-70.301563),
("Santosha","Culture","Kingfield","Yoga retreat, sauna, and bed & breakfast set on a hilltop estate in the heart of town; a perfect rest after a big ski day.","$$$","Year-round","https://maps.app.goo.gl/hYddUw4AT4cnX7mk7",44.9592067,-70.1599366),
("Rangeley","Culture","Rangeley","The most charming of Maine's mountain resort towns — small, walkable, and set on a lake surrounded by peaks.","Free","Year-round","https://maps.app.goo.gl/afLNCodWQamCaSWh6",44.9656821,-70.6427102),
("Monson","Culture","Monson","Remote trail town at the edge of the 100 Mile Wilderness, with an artist residency, gallery, and a James Beard-winning restaurant.","Free","Year-round","https://maps.app.goo.gl/xh7up98Po1vP7V3P6",45.2869936,-69.5011619),
]

df = pd.DataFrame(rows, columns=["name","category","town","description","price","season","maps_url","lat","lng"])
df.insert(0, "id", range(1, len(df)+1))
df.insert(2, "region", "Western Mountains & Foothills")

df.to_excel("/mnt/user-data/outputs/maine_locations_western_mountains.xlsx", index=False, sheet_name="Locations")
print(f"Wrote {len(df)} rows")
print(df['category'].value_counts())
