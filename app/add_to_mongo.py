from mongo_client import AtlasClient

client = AtlasClient()


# characters
src_list = [
    "/static/images/characters/crossroads.png",
    "/static/images/characters/inner_peace.png",
    "/static/images/store0.png",
    "/static/images/store1.png",
    "/static/images/store2.png",
    "/static/images/other/Life well lived.png"
]

title_list = [
    "Crossroads",
    "Inner Peace",
    "Sonder",
    "Achilles",
    "Perseus",
    "Life Well Lived"
]

content_list = [
    "",
    "",
    "I created this painting to symbolize the philosophy of profound pondering and attitude of contemplation. Different people have each have different understandings of art. You can interpret the meaning of this painting in your own way.",
    "This is a charcoal drawing of the Greek war hero Achilles. In Homer’s Iliad, he is well-known for slaying the Trojan prince Hector outside the gates of Troy. This piece is meant to symbolize loss and grief.",
    "In Greek mythology, Perseus is best known for slaying the Gorgon Medusa and rescuing Andromeda from the sea monster. In this drawing, Perseus, wearing the Cap of Invisibility given to him by war goddess Athena, holds up the severed head of Medusa (not shown). This piece symbolizes triumph and conquest.",
    ""
]


price_list = [
    "$350",
    "$600",
    "$200",
    "$200",
    "$150",
    "$250"
]

description_list = [
    "Sophia Zhang, oil painting 14X18 in",
    "Sophia Zhang, oil painting 20X24 in",
    "Sophia Zhang, Acrylic Painting, 9X12 in, Scholastic Art Award, Gold Key.",
    "Sophia Zhang, Charcoal Drawing.",
    "Sophia Zhang, Charcoal Drawing, 14X18 in.",
    "Sophia Zhang, Oil Painting 10X12 in, Fort Wayne Art League Scholarship Recipient"
]

category = [
    "characters"
]*6
    
# animals
src_list += [
    "static/images/animals/azureflock.png",
    "static/images/animals/saola.png",
    "static/images/animals/mangrove.png",
    "static/images/animals/skull.png",
    "static/images/animals/pride.png",
    "static/images/animals/canislupus.png"
]

title_list += [
    "Azure Flock",
    "Saola",
    "Mangrove Forest",
    "Smilondon Skull",
    "Pride",
    "Canis lupus"
]

content_list += [
    "The Spix’s macaw is a species of macaw native to Brazil. Due to deforestation, habitat loss, and illegal poaching, they are critically endangered and nearing extinction, with only about 160 left in captivity.",
    "The saola, also known as the spindlehorn, Asian unicorn, or vu kuang ox, is one of the world's rarest large mammals. Saola resemble antelope and inhabit the Annamite Mountains of Vietnam and Laos. They are critically endangered, as they are rarely seen in the wild, with none existing in captivity.",
    "Mangroves are trees or shrubs that grow in intertidal regions off tropical and subtropical coastlines. They are crucial to ecosystems, stabilizing coastlines and serving as a habitat to many species of aquatic wildlife, including parrotfish, which seek shelter and protection within the underwater roots of mangrove trees.",
    "Smilodon is a genus of extinct prehistoric predators, including the saber-toothed tiger. The skull of a saber-toothed cat can measure up to 35 cm long, with canines up to 18 cm long.",
    "",
    ""
]

price_list += [
    "Sold",
    "SOLD",
    "Sold",
    "$150",
    "$100",
    "$100"
]

description_list += [
    "Sophia Zhang, Charcoal and Pastel Chalk, 14X18 in, Scholastic Art Award, Silver Key.",
    "Sophia Zhang, Charcoal and Pastel Chalk, 14X18 in, Best in Show Award.",
    "Sophia Zhang, Charcoal and Pastel Chalk, 14X18 in. ",
    "Sophia Zhang, Color Pencil, 14X18 in.",
    "Sophia Zhang, Scratchboard, 8X11 in.",
    "Sophia Zhang, drawing, 13X20 in."
]

# animals 2
src_list += [
    "static/images/animals/tiger.png",
    "static/images/animals/wind.png",
    "static/images/animals/atelopus.jpg",
    "static/images/animals/iguana.jpg",
    "static/images/animals/sumatran.jpg",
    "static/images/animals/emerald.jpg",
    "static/images/animals/crab.jpg"
]

title_list += [
    "The Tiger",
    "Running in the Wind",
    "Atelopus varius",
    "Fiji Crested Iguana",
    "Wading Sumatran",
    "Hine’s Emerald Dragonfly",
    "Singapore Freshwater Crabs"
]

content_list += [
    "",
    "",
    "The Costa Rican variable harlequin toad, otherwise known by its scientific name Atelopus varius or simply the clown frog, is a species of poisonous amphibians native to the Talamanca Mountains, from Central Panama all the way up to Costa Rica. Dramatic declines in Atelopus varius populations began in the late 1980s, where they continue to rapidly decline. The variable harlequin frog is categorized as critically endangered by the International Union for Conservation of Nature, but breeding programs such as PARC are giving these frogs hope.",
    "The Fiji crested iguana is a critically endangered species of iguana native to some northwestern islands of the Fijiian archipelago, where it makes its habitat in the dry forest. They were originally found throughout 14 Fijian islands, but today are only found in 3, with 98% of all remaining iguanas (less than 6,000) living on just one island. The Fijian crested iguana is unique to Fiji, and today survives on only a few islands in western Fiji.",
    "The Sumatran tiger is a species of tiger native to the Indonesian island of Sumatra, and is the only surviving tiger species in the Sunda Islands. Habitat loss is the main cause the declining Sumatran tiger population, with their native rainforests being cut down for agriculture, plantations, and settlement. On many parts of the island, illegal timber harvesting and forest conversion are out of control.",
    "The Hine's emerald is an endangered dragonfly species found throughout the United States and Canada. Populations exist in Illinois, Michigan, Missouri, Ontario, and Wisconsin. Larvae are found in shallow, flowing water in fens and marshes. Major threats to the species include habitat loss and alteration. Luckily, the species is legally protected in both the United States and Canada",
    "The Singapore freshwater crab is a critically endangered species of freshwater crab native to Singapore. It’s on the smaller side, only growing to a size of 30 mm wide. It is a primarily nocturnal species that lives in streams in the forest, feeding on detritus and worms that live in the muddy stream bed. It has only ever been recorded from two locations in Singapore."
]

price_list += [
    "$200",
    "$150",
    "$200",
    "$200",
    "Sold",
    "Sold",
    "Sold"
]

description_list += [
    "Sophia Zhang, Color Pencil, 12X15 in, Scholastic Art Award, Gold Key",
    "Sophia Zhang, watercolor painting, 8x10 in, Scholastic Art Award, Silver Key",
    "Sophia Zhang, Charcoal and Chalk Pastel, 12X15 in",
    "Sophia Zhang, Charcoal and Chalk Pastel, 12X15 in",
    "Sophia Zhang, Charcoal and Chalk Pastel, 18X24 in",
    "Sophia Zhang, Charcoal and Chalk Pastel, 8X10 in",
    "Sophia Zhang, Charcoal and Chalk Pastel, 8X10 in"
]

category += ["animals"] * 13


# flowers
# List of image sources
src_list += [
    "static/images/scenery/thegarden.png",
    "static/images/scenery/incandescence.png",
    "static/images/scenery/wuther.png",
    "static/images/scenery/willow.png",
    "static/images/scenery/fields.png",
    "static/images/scenery/bouquet.jpg",
    "static/images/scenery/foxgloves.png"
]

# List of titles
title_list += [
    "The Garden of Live Flowers",
    "Incandescence",
    "Withering Bouquet",
    "Willow Over Lily Pond",
    "Scenic Fields",
    "Portrait of Bouquet",
    "Foxgloves"
]

# List of prices
price_list += [
    "$100",
    "Sold",
    "$65",
    "Sold",
    "Sold",
    "Sold",
    "$150"
]

# List of descriptions
description_list += [
    "Sophia Zhang, watercolor painting, 13X16 in, Scholastic Art Award, Silver Key",
    "Sophia Zhang, color pencil, 11X14, Published in the Art anthology by Celebrating Art, 2021",
    "Sophia Zhang, Watercolor painting, 13X16",
    "Sophia Zhang, acrylic paining, Sold",
    "Sophia Zhang, acrylic paining, Sold",
    "Sophia Zhang, Watercolor, Sold",
    "Sophia Zhang, Watercolor painting, 14X20"
]

category += ["flowers"] * 7
content_list += [""] * 7

# other
# List of image sources
src_list += [
    "static/images/news/suzhang11-06-12.png",
    "static/images/news/suzhang10-05-16.png",
    "static/images/other/Composition23,24.png",
    "static/images/other/Pancner.png"
]

# List of titles
title_list += [
    "A Peaceful Day",
    "Fall",
    "Composition number 23 and 24",
    "Donation by Ales Pancner"
]

# List of prices
price_list += [
    "$150",
    "$150",
    "SOLD",
    "$200"
]

# List of descriptions
description_list += [
    "Su Zhang, watercolor, 13X16 in",
    "Su Zhang, watercolor, 13X16 in",
    "Ales Pancner, abstract",
    "Ales Pancner, 9X12 in"
]
# List of image sources
src_list += [
    "static/images/other/shelter.png",
    "static/images/other/summer.png",
    "static/images/other/impression.png"
]

# List of titles
title_list += [
    "Shelter of Existence",
    "Summer of ’83",
    "Impression of Prague"
]

# List of prices
price_list += [
    "$200",
    "$100",
    "$200"
]

# List of descriptions
description_list += [
    "Sophia Zhang, drawing, 13X16 in, Scholastic Art Award, Silver Key",
    "Sophia Zhang, 12X16 in",
    "Sophia Zhang, watercolor, 12X18 in"
]
category += ["other"] * 7
content_list += [""] * 7

#a = client.get_card_list("other")
#print(a)
#client.update_card_list("other", a)
"""
# characters, animals, flowers, other
for cat in ["characters", "animals", "flowers", "other"]:
    index_offset = 0
    found_offset = False
    temp_cards = []
    for i in range(len(src_list)):
        if category[i] == cat and not found_offset:
            found_offset = True
            index_offset = i

        if not found_offset:
            continue

        card = {
            "index" : i-index_offset,
            "src" : src_list[i],
            "title" : title_list[i],
            "price" : price_list[i],
            "desc" : description_list[i],
            "content" : content_list[i]
        }
        temp_cards.append(card)
    
    client.add_card_list(temp_cards, cat)
"""