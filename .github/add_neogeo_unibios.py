import json
import zipfile

with open('db.json', 'r') as file:
    data = json.load(file)

del data['base_files_url']
del data['db_url']

data['zips'] = {
    "neogeo_unibios": {
        "contents_file": {
            "hash": "1986c39676354d19ae648a914bd914f7",
            "size": 101498,
            "url": "http://unibios.free.fr/download/uni-bios-40.zip"
        },
        "description": "Extracting NeoGeo UniBios from http://unibios.free.fr",
        "internal_summary": {
            "files": {
                "|games/NEOGEO/uni-bios.rom": {
                    "hash": "4f0aeda8d2d145f596826b62d563c4ef",
                    "size": 131072,
                    "tags": [
                        data['tag_dictionary']['bios'],
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ],
                    "zip_id": "neogeo_unibios",
                    "zip_path": "uni-bios.rom"
                }
            },
            "folders": {
                "|games/NEOGEO": {
                    "zip_id": "neogeo_unibios",
                    "tags": [
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ]
                }
            }
        },
        "kind": "extract_single_files",
    },
    "neogeo_unibioscd": {
        "contents_file": {
            "hash": "e2ec14752f65aef00fc33e68cf2fc301",
            "size": 381292,
            "url": "http://unibios.free.fr/download/uni-bioscd-33.zip"
        },
        "description": "Extracting NeoGeo CD UniBios from http://unibios.free.fr",
        "internal_summary": {
            "files": {
                "|games/NeoGeo-CD/uni-bioscd.rom": {
                    "hash": "08ca8b2dba6662e8024f9e789711c6fc",
                    "size": 524288,
                    "tags": [
                        data['tag_dictionary']['bios'],
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ],
                    "zip_id": "neogeo_unibioscd",
                    "zip_path": "uni-bioscd.rom"
                }
            },
            "folders": {
                "|games/NeoGeo-CD": {
                    "zip_id": "neogeo_unibioscd",
                    "tags": [
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ]
                }
            }
        },
        "kind": "extract_single_files",
    }
}

with open('bios_db.json', 'w') as output_file:
    json.dump(data, output_file)

with zipfile.ZipFile('bios_db.json.zip', 'w', zipfile.ZIP_DEFLATED) as zipped_file:
    zipped_file.writestr('bios_db.json', json.dumps(data))
