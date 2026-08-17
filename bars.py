import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from scipy import stats

# Matcha figurens typsnitt och storlek mot LaTeX-dokumentet
# (fontsize: 10pt, geometry: margin=1in => textbredd 6.5in, se garb.qmd).
# Använder samma Latin Modern-typsnitt som dokumentet, buntat i fonts/.
for _f in ("lmroman10-regular.otf", "lmroman10-bold.otf", "lmroman10-italic.otf"):
    fm.fontManager.addfont(f"fonts/{_f}")

plt.rcParams.update({
    "font.family": "Latin Modern Roman",
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "hatch.linewidth": 0.6,
})

# Validerad, CVD-säker färgpalett samt linjebredd som delas mellan axlar,
# stänglar och punkter för ett enhetligt "handritat ingenjörsblock"-utseende.
FORE_COLOR, EFTER_COLOR = "#2f5f9e", "#ad3f37"
AXIS_LW = 1.0
SKETCH = dict(scale=0.45, length=170, randomness=1)

def sketch_spines(ax):
    for spine in ax.spines.values():
        spine.set_linewidth(AXIS_LW)
        spine.set_sketch_params(**SKETCH)

fore = [242, 248, 235, 251, 239, 246, 241, 253, 238, 249,
        244, 237, 250, 245, 243, 247, 240, 252, 236, 248,
        245, 241, 249, 243, 246, 238, 251, 244, 247, 242,
        248, 240, 249, 245, 243]

efter = [189, 185, 192, 187, 183, 190, 186, 188, 184, 191,
         187, 185, 189, 186, 188, 184, 190, 187, 185, 189,
         186, 188, 184, 190, 187, 185, 189, 186, 188, 184,
         190, 187, 185, 189, 186]

# Stapeldiagram (motsvarande tidigare 60% av textbredden, nu satt direkt;
# inkludera i LaTeX med width=3.9in för att matcha exakt)
fig, ax = plt.subplots(figsize=(3.9, 2.9))
ax.set_axisbelow(True)
ax.grid(True, axis='y', which='major', color='#a9c4e0', linewidth=0.5, alpha=0.4)
bars = ax.bar(['Före', 'Efter'], [np.mean(fore), np.mean(efter)],
               color=[FORE_COLOR, EFTER_COLOR], width=0.6,
               edgecolor='black', linewidth=AXIS_LW, hatch='///')
for bar in bars:
    bar.set_sketch_params(scale=0.6, length=130, randomness=1)
sketch_spines(ax)
ax.set_xlabel('Grupp')
ax.set_ylabel('Egenskap X (ms)')
plt.tight_layout()
plt.savefig('bars.pdf')
plt.close()