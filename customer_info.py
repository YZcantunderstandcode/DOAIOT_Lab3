customers = [
	{'name': 'Alice', 'email': 'alice@example.com', 'phone': '555-1234', 'address': '123 Main St'},
	{'name': 'Bob', 'email': 'bob@example.com', 'phone': '555-5678', 'address': '456 Maple Ave'},
	{'name': 'Charlie', 'email': 'charlie@example.com', 'phone': '555-9012', 'address': '789 Oak Rd'}
]

def display_all_records():
		print(("Name" + "\t" +"Email" +"\t" +"Phone" +"\t" +"Address" ).expandtabs(15))
		
		for item in customers:
			print((item["name"] + "\t" + item["email"] + "\t" + item["phone"] + "\t" + item["address"]).expandtabs(15))
		

def main():
    display_all_records()