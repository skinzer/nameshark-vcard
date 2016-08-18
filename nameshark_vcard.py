import argparse
import sys
import vobject
import probablepeople as pp
import base64
import json
    
def vcard_to_nameshark(text, group_name):
    shark = {"name": group_name, "contacts": []}
    
    for v in vobject.readComponents(text):
        full_name = v.getChildValue('fn')
        photo = v.getChildValue('photo')
        
        full_name_dict = pp.tag(full_name)[0]

        if 'GivenName' in full_name_dict:
            first_name = full_name_dict['GivenName']
        else:
            first_name = full_name.split(" ")[0]
            
        if 'Surname' in full_name_dict:
            surname = full_name_dict['Surname']
        else:
            names = full_name.split(" ")
            if len(names) > 1:
                surname = names[1]
            else:
                surname = ""
        
        if photo is not None:
            photo_data = base64.b64encode(photo)
            photo_data = "data:image/jpeg;base64," + photo_data
        else:
            print("Warning: Missing photo for " + full_name + "...!")
            photo_data = ""
        
        entry = {"first": first_name, "last": surname, 
                 "photoData": photo_data, "details":""}

        shark["contacts"].append(entry)
    
    json_str = json.dumps(shark, separators=(',', ': '))
    
    return json_str

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="the input file")
    parser.add_argument("group", help="the output group name")

    args = parser.parse_args()

    with open(args.file, 'r') as f:
        text=f.read()
    
    json_str = vcard_to_nameshark(text, args.group)

    with open(args.group + ".json", 'w') as f:
        f.write(json_str)    

if __name__ == "__main__":
    main()


