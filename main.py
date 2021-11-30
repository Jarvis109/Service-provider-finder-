import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse("+919582173842")
print(geocoder.description_for_number(phone_number, 'en'))
from phonenumbers import carrier
service_provider = phonenumbers.parse("+919582173842")
print(carrier.name_for_number(service_provider, 'en'))
