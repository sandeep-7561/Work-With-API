import requests

url = requests.get("https://isro.vercel.app/api/spacecrafts")

response = url.json()
try:
    useinput = int(input("Enter ID: "))
    for i in range(len(response["spacecrafts"])):
        if useinput == int(response["spacecrafts"][i]["id"]):
            print(f"your id is: {useinput}. \nspace-craft name: {response['spacecrafts'][i]['name']}")
            break
    else:
        print("id not found")
except:
    print('Syntex error')
    
