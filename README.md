This is an Node.js api that serves information about UIUC apartments that were scraped using Python libraries (and some self-made libraries).

current apartment schema: { link: String,
                     address: String,
                     beds: Integer,
                     bathrooms: Integer,
                     rate: Integer,
                     landlord: { email: String,
                                 name: String,
                                 phone: String },
                     pictures: String[],
                     info: String[]
                 }
