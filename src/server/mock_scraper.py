import requests
from modules.database import DatabaseClient

db = DatabaseClient("src/client/static", "server-store")
img = requests.get(
    "https://media.nedigital.sg/fairprice/fpol/media/images/product/XL/13038430_XL1_20220701.jpg"
).content

p_id = db.create_default_product(
    "Dahfa Dried Fish Fillet",
    "Snacks",
    [9_556353_970619],
    img,
)
print(p_id)
