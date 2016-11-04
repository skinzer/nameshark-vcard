"""Convert vCard-formatted string to the JSON format expected by Name Shark."""
# coding=utf-8
import base64
import json
from collections import namedtuple

import argparse
import vobject
import probablepeople as pp

Names = namedtuple('Names', ['first_name', 'surname'])


def get_names(fn: str) -> Names:
    """
    Extract the first name and surname from a vCard 'fn' field.

    :param fn: the input vCard 'fn' field.
    :return: a namedtuple containing the first name and surname.

    >>> get_names('John Smith')
    Names(first_name='John', surname='Smith')
    """

    # Use probablepeople to tag the parts of the name.
    full_name_dict = pp.tag(fn)[0]

    if 'GivenName' in full_name_dict:
        # If probablepeople has successfully extracted the first name, use it.
        first_name = full_name_dict['GivenName']
    else:
        # Otherwise, assume it's the first part of the string.
        first_name = full_name.split(" ")[0]

    if 'Surname' in full_name_dict:
        # If probablepeople has successfully extracted the surname, use it.
        surname = full_name_dict['Surname']
    else:
        # Otherwise, assume it's the second part of the string, if it exists.
        names = fn.split(" ")
        if len(names) > 1:
            surname = names[1]
        else:
            surname = ""

    names = Names(first_name, surname)

    return names


def get_photo(photo: str) -> Names:
    """
    Extract the photo data (if it exists) from a vCard 'photo' field.

    :param photo: the input vCard 'photo' field.
    :return: a base64-encoded string containing the photo data.
    """
    # TODO: Add doctest above? or pytest
    photo =

    if photo is not None:
        photo_data = base64.b64encode(photo)
        photo_data = "data:image/jpeg;base64," + photo_data
    else:
        photo_data = ""

    return photo_data


def extract_contact_from_component(v: vobject.Component) -> dict:
    """
    Extract the contact info from a vCard component.

    :param v: the input vCard component text.
    :return: a dictionary containing the extracted contact info.
    """
    # TODO: Add doctest above? or pytest
    names = get_names(v.getChildValue('fn'))
    photo_data = get_photo(v.getChildValue('photo'))

    if photo_data == "":
        print("Warning: Missing photo for " + names.first_name + " " +
              names.surname + "...!")

    entry = {"first": names.first_name, "last": names.surname,
             "photoData": photo_data, "details": ""}

    return entry


def extract_contacts_from_vcard(vcard: str) -> list:
    """
    Extract the contact info from a vCard.

    :param vcard: the vCard text to convert.
    :return: a list containing the extracted contact info.
    """
    # TODO: Add doctest above? or pytest
    contacts = []

    for v in vobject.readComponents(vcard):
        entry = extract_contact_from_component(v)
        contacts.append(entry)

    return entry


def convert_to_nameshark(contacts: list, group_name: str, ) -> str:
    """
    Convert a list containing contact info into JSON for Name Shark.

    :param contacts:
    :param group_name: the Name Shark group to use.
    :return: the list containing contact info extracted from a vCard.
    """
    # TODO: Add doctest above? or pytest
    shark = {"name": group_name, "contacts": contacts}
    json_str = json.dumps(shark, separators=(',', ': '))

    return json_str


def vcard_to_nameshark(vcard: str, group_name: str) -> str:
    """
    Convert vCard-formatted string to the JSON format expected by Name Shark.

    :param vcard: the vCard text to convert.
    :param group_name: the Name Shark group to use.
    :return: JSON version of vCard input.
    """
    # TODO: Add doctest above? or pytest
    contacts = extract_contacts_from_vcard(vcard)
    json_str = convert_to_nameshark(group_name, contacts)

    return json_str


def main() -> None:
    """
    The main nameshark_vcard module.

    :return: None
    """
    # TODO: Add pytest?
    # TODO: Switch to using click, and apply click-man
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="the input file")
    parser.add_argument("group", help="the output group name")

    args = parser.parse_args()

    with open(args.file, 'r') as f:
        text = f.read()

    json_str = vcard_to_nameshark(text, args.group)

    with open(args.group + ".json", 'w') as f:
        f.write(json_str)


if __name__ == "__main__":
    main()
