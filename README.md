This is an node.js api that serves information about uiuc apartments that were scrapped using python.

Nathan changed this


apartment schema: { link: String,
                     address: String,
                     rate: [LIST]{num_beds: Number,
                             monthly_rate: Number},
                     lat: String,
                     long: String,
                     landlord: { email: String,
                                 name: String,
                                 phone: String },
                     pictures: String[],
                     amenities: String[]
                 }
