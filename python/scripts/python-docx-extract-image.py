import docx


def extract_image_from_docx(docx_content):
    doc = docx.Document(docx_content)
    image_list = []

    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            image_list.append(rel.target_part.blob)

    return image_list
