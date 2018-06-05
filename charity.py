charities = {'Animals':
                ['American Humane Society',
                'Jane Goodall Institute',
                'Wildlife Conservation Society'
                ],
			'Cancer': 
                ['Cancer Research Institute',
                'National Breast Cancer Coalition Fund',
                'Prevent Cancer Foundation'
                ],
			'Environment': 
                ['Conservation Fund',
                'Earthworks',
                'Environmental Defense Action Fund'
                ],
			'Homelessness': 
                ['Center for Community Change',
                'Homes for Our Troops',
                'National Alliance to End Homelessness'
                ],
			'Women\'s Rights': 
                ['Center for Reproductive Rights',
                'Global Fund for Women',
                'Women for Women International U.S.'
                ]
            }
print("Looking for a charity to support? What are you interested in?")
category = input()
if category in charities.keys():
	print("Here are some charities you can support: ")
	for charity in charities[category]:
		print(charity)
else:
	print("Sorry, we do not have data for " + category + " yet!")

#for categories,charNames in charities.items():
#	print(categories)
#	print(charNames)
    
