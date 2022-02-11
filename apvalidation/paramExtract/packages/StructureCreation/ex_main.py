from PIL import Image

import smiles_validation


validated_smiles, img_path = smiles_validation.validate_smiles('	OC[C@@H](O1)[C@@H](O)[C@H](O)[C@@H]2[C@@H]1c3c(O)c(OC)c(O)cc3C(=O)O2')
print(validated_smiles)
img = Image.open(img_path)
img.show()
