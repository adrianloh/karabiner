import re
import os

file_template = """
<?xml version="1.0"?>
<root>
	<item>
    <name>Mine</name>
    <identifier>Unique Identifier of Setting</identifier>
    <autogen>__KeyToKey__ KeyCode::A, ModifierFlag::SHIFT_R, KeyCode::SHIFT_R</autogen>
    <autogen>__KeyToKey__ KeyCode::B, ModifierFlag::OPTION_L, KeyCode::OPTION_L</autogen>
    REPLACE_ME
  </item>
</root>
"""

template = "<autogen>__KeyToKey__ KeyCode::%s, KeyCode::%s</autogen>"
mappings = {}
for row in open("mappings.txt").read().split("\n"):
	original, new = row.split(":")
	original = original.split(",")
	new = new.split(",")
	for (i,a) in enumerate(original):
		old_alpha = original[i].upper()
		new_alpha = new[i].upper()
		if re.search("^\d$", old_alpha):
			old_alpha = "KEY_" + str(old_alpha)
		if re.search("^\d$", new_alpha):
			new_alpha = "KEY_" + str(new_alpha)
		mappings[old_alpha] = new_alpha

definitions = [template % (k,v) for (k,v) in mappings.items()]

pp = re.sub("REPLACE_ME", "\n".join(definitions), file_template)

t_file = os.environ['HOME'] + "/Library/Application Support/Karabiner/private.xml"

with open(t_file, "w") as f:
	f.write(pp)