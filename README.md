This is an node.js api that serves information about uiuc apartments that were scrapped using python.
Currently we are only trying to get the basic information such as address, beds, bathrooms, price.
Eventually we hope to get information like amenities, utilities, landlord contact information.

apartment schema: { link: String,
                     address: String,
                     beds: Integer,
                     bathrooms: Integer,
                     rate: Integer,
                     pictures: String[],
                 }
