import datetime

from src.domain.geo_data import GeoData

geo_data_log = [
    GeoData(
        ip='109.123.18.84',
        city='Ruše',
        region='Ruše',
        country='SI',
        loc='46.5394,15.5158	',
        org='AS58056 siaIT d.o.o.',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
