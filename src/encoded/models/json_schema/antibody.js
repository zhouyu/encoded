{
    "title": "Antibody",
    "type": "object",
    "properties": {
        "source": {
            "type": "string"
        },
        "product_id": {
            "type": "string"
        },
        "lot_id": {
            "type": "string"
        },
        "target": {
            "description": "Target of the antibody",
            "type": "reference",
        }
        "validations": [
            "type": "reference"
        ]
    },
    "required": ["source", "product_id"]
}